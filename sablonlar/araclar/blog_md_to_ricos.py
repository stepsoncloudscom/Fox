import re, json, glob, os, sys

SRC = "/Users/ayhanerden/Fox/raporlar/yayin-d-paketi"
OUT = os.path.join(os.path.dirname(__file__), "payloads.json")
MEMBER = "86add041-5b3a-474b-bc8a-cf6996f028da"
BASE = "https://www.ozgurprotez.com/post/"

def parse(path):
    t = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
    meta = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2).strip()

posts = [parse(p) + (os.path.basename(p),) for p in sorted(glob.glob(SRC + "/*.md"))]
title2url = {meta["title"]: BASE + meta["slug"] for meta, _, _ in posts}

missing = set()
def inline(s):
    out = []
    rx = re.compile(r"\[\[SERİ: ([^|\]]+)\|([^\]]+)\]\]|\[([^\]]+)\]\(([^)]+)\)|\*\*([^*]+)\*\*|\*([^*]+)\*")
    last = 0
    def push(text, dec):
        if text:
            out.append({"type": "TEXT", "textData": {"text": text, "decorations": dec}})
    for m in rx.finditer(s):
        push(s[last:m.start()], [])
        if m.group(1):
            url = title2url.get(m.group(1).strip())
            if not url:
                missing.add(m.group(1).strip())
            push(m.group(2), [{"type": "LINK", "linkData": {"link": {"url": url, "target": "SELF"}}}] if url else [])
        elif m.group(3):
            push(m.group(3), [{"type": "LINK", "linkData": {"link": {"url": m.group(4), "target": "SELF"}}}])
        elif m.group(5):
            push(m.group(5), [{"type": "BOLD", "fontWeightValue": 700}])
        else:
            push(m.group(6), [{"type": "ITALIC", "italicData": True}])
        last = m.end()
    push(s[last:], [])
    return out

def para(s):
    return {"type": "PARAGRAPH", "nodes": inline(s), "paragraphData": {}}

def build(body):
    nodes, faqs = [], []
    in_faq, q = False, None
    blocks = re.split(r"\n\s*\n", body)
    for b in blocks:
        b = b.strip()
        if not b:
            continue
        lines = b.split("\n")
        # heading lines may be followed by text in same block
        i = 0
        while i < len(lines):
            ln = lines[i].rstrip()
            if ln.startswith("### "):
                txt = ln[4:].strip()
                nodes.append({"type": "HEADING", "nodes": inline(txt), "headingData": {"level": 3}})
                if in_faq:
                    q = {"q": re.sub(r"\*", "", txt), "a": []}
                    faqs.append(q)
                i += 1
            elif ln.startswith("## "):
                txt = ln[3:].strip()
                nodes.append({"type": "HEADING", "nodes": inline(txt), "headingData": {"level": 2}})
                in_faq = txt.lower().startswith("sık sorulan")
                q = None
                i += 1
            elif ln.startswith("- "):
                items = []
                while i < len(lines) and lines[i].startswith("- "):
                    items.append({"type": "LIST_ITEM", "nodes": [{"type": "PARAGRAPH", "nodes": inline(lines[i][2:].strip()), "paragraphData": {}}]})
                    i += 1
                nodes.append({"type": "BULLETED_LIST", "nodes": items, "bulletedListData": {"indentation": 0}})
            else:
                rest = []
                while i < len(lines) and not lines[i].startswith(("#", "- ")):
                    rest.append(lines[i].strip())
                    i += 1
                txt = " ".join(rest)
                nodes.append(para(txt))
                if in_faq and q is not None:
                    q["a"].append(re.sub(r"\[\[SERİ: [^|\]]+\|([^\]]+)\]\]", r"\1", re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", txt)).replace("**", "").replace("*", ""))
    return nodes, faqs

payloads = []
for meta, body, fn in posts:
    nodes, faqs = build(body)
    tags = [
        {"type": "title", "children": meta["seoTitle"]},
        {"type": "meta", "props": {"name": "description", "content": meta["metaDescription"]}},
    ]
    faqs = [f for f in faqs if f["a"]]
    if faqs:
        schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": f["q"], "acceptedAnswer": {"@type": "Answer", "text": " ".join(f["a"])}} for f in faqs]}
        tags.append({"type": "script", "props": {"type": "application/ld+json"}, "children": json.dumps(schema, ensure_ascii=False)})
    payloads.append({
        "file": fn,
        "draftPost": {
            "title": meta["title"],
            "memberId": MEMBER,
            "excerpt": meta["excerpt"],
            "seoSlug": meta["slug"],
            "seoData": {"tags": tags, "settings": {"preventAutoRedirect": False, "keywords": []}},
            "richContent": {"nodes": nodes},
        },
        "faqCount": len(faqs),
    })

json.dump(payloads, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
print("posts", len(payloads), "bytes", os.path.getsize(OUT), "missing seri:", missing)
for p in payloads:
    d = p["draftPost"]
    n = d["richContent"]["nodes"]
    links = json.dumps(n, ensure_ascii=False).count('"LINK"')
    print(p["file"], "| nodes", len(n), "| links", links, "| faq", p["faqCount"], "| seo", len(d["seoData"]["tags"][0]["children"]), len(d["seoData"]["tags"][1]["props"]["content"]))
