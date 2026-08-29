import json, os, cv2, numpy as np, sys
S=os.path.dirname(os.path.abspath(__file__))
L=json.load(open(S+"/dosya_listesi.json"))
clahe=cv2.createCLAHE(clipLimit=3.0,tileGridSize=(8,8))
def gri(bgr): return clahe.apply(cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY))
def yukle(p):
    a=cv2.imread(p,cv2.IMREAD_REDUCED_COLOR_4)          # 1/4 boyutta oku — yükleme hızlansın
    if a is None: a=cv2.imread(p,cv2.IMREAD_COLOR)
    return a
varyant=[]
for f in sorted(os.listdir(S+"/sablon_kabartma")):
    s=gri(cv2.imread(S+"/sablon_kabartma/"+f))
    for aci in (-18,-6,6,18,0):
        M=cv2.getRotationMatrix2D((s.shape[1]/2,s.shape[0]/2),aci,1.0)
        c,si=abs(M[0,0]),abs(M[0,1])
        nw=int(s.shape[0]*si+s.shape[1]*c); nh=int(s.shape[0]*c+s.shape[1]*si)
        M[0,2]+=nw/2-s.shape[1]/2; M[1,2]+=nh/2-s.shape[0]/2
        r=cv2.warpAffine(s,M,(nw,nh),borderValue=255)
        for gw in (50,70,95,130,175):
            o=gw/nw; w2,h2=int(nw*o),int(nh*o)
            if w2>=20 and h2>=10: varyant.append(cv2.resize(r,(w2,h2),interpolation=cv2.INTER_AREA))
print("varyant:",len(varyant),flush=True)
bulgu={}
for i,(d,f,p) in enumerate(L,1):
    b=yukle(p)
    if b is None: continue
    H,W=b.shape[:2]; ol=1000/max(W,H)
    g=gri(cv2.resize(b,(max(1,int(W*ol)),max(1,int(H*ol))),interpolation=cv2.INTER_AREA))
    aday=[]
    for t in varyant:
        if t.shape[0]>=g.shape[0] or t.shape[1]>=g.shape[1]: continue
        r=cv2.matchTemplate(g,t,cv2.TM_CCOEFF_NORMED)
        mx=float(r.max())
        if mx>=0.58:
            loc=np.unravel_index(int(r.argmax()),r.shape)
            aday.append({"x":int(loc[1]),"y":int(loc[0]),"w":int(t.shape[1]),"h":int(t.shape[0]),"skor":round(mx,3)})
    aday.sort(key=lambda z:-z["skor"]); kal=[]
    for z in aday:
        if all(not(abs(z["x"]-q["x"])<max(z["w"],q["w"])*0.5 and abs(z["y"]-q["y"])<max(z["h"],q["h"])*0.5) for q in kal): kal.append(z)
    if kal: bulgu[os.path.join(d,f)]=kal[:3]
    if i%25==0: print(f"  {i}/{len(L)} · bulgulu {len(bulgu)}",flush=True)
json.dump(bulgu,open(S+"/kabartma_v1.json","w"),ensure_ascii=False)
print(f"BITTI · {len(bulgu)}/{len(L)} görsel · {sum(len(v) for v in bulgu.values())} aday",flush=True)
