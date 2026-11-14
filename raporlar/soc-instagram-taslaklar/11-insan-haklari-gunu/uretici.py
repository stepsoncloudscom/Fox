import sys
F=sys.argv[1]; GRID=len(sys.argv)>2
# Altın oran ızgarası: 1080x1350. Dikey 413/667, yatay 516/834. Kenar 55. Ölçek (Fibonacci): 377/233/144/89/55/34/21
fr=[
 # zone, align, headline, size, sub
 ("top","l","20 YIL.",377,"BM Engelli Hakları Sözleşmesi<br>13 Aralık'ta 20 yaşında.<br>İçinde ne yazıyor?"),
 ("top","l","13 ARALIK<br>2006",233,"BM Genel Kurulu sözleşmeyi kabul etti.<br>3 Mayıs 2008'de yürürlüğe girdi."),
 ("top","l","194<br>TARAF",233,"Sözleşmeye bugün<br>194 taraf var.<br>Türkiye 30 Mart 2007'de<br>imzaladı, 28 Eylül 2009'da<br>onayladı."),
 ("top","l","MADDE<br>30",233,"Kültür, dinlenme, boş zaman ve spor.<br>Devletler engelli bireylerin her düzeyde<br>spora katılımını teşvik eder,<br>spor alanlarına erişimi sağlar."),
 ("bottom","c","OKULDA DA",233,"Aynı madde: engelli çocuklar oyuna, spora<br>ve dinlenmeye, okul dahil,<br>diğer çocuklarla eşit erişir."),
 ("bottom","l","MAKING<br>HUMANITY<br>TOGETHER",144,"10 Aralık İnsan Hakları Günü, 2026 teması.<br>Kaynak: un.org · treaties.un.org (14 Kasım 2026).<br>Madde özetleri bize ait, resmî çeviri değildir."),
]
css=f"""@font-face{{font-family:Bebas;src:url(file://{F}/BebasNeue-Regular.ttf)}}
@font-face{{font-family:Comf;src:url(file://{F}/Comfortaa-Regular.ttf)}}
html,body{{margin:0}} .f{{position:relative;width:1080px;height:1350px;overflow:hidden;color:#fff;background-size:cover;background-position:center}}
.sc{{position:absolute;left:0;width:100%}}
.sc.top{{top:0;height:834px;background:linear-gradient(180deg,rgba(0,0,0,.50) 0%,rgba(0,0,0,.30) 55%,rgba(0,0,0,0) 100%)}}
.sc.bottom{{bottom:0;height:834px;background:linear-gradient(0deg,rgba(0,0,0,.60) 0%,rgba(0,0,0,.34) 55%,rgba(0,0,0,0) 100%)}}
.blk{{position:absolute;left:55px;width:970px;display:flex;flex-direction:column}}
.blk.top{{top:0;height:516px;justify-content:flex-end}}
.blk.bottom{{bottom:55px;justify-content:flex-end}}
.blk.c{{align-items:center;text-align:center}}
.h{{font-family:Bebas;font-weight:400;line-height:.84;letter-spacing:-1px;margin:0}}
.s{{font:400 34px/1.5 Comf;margin:0;white-space:nowrap}}

.blk.top .s{{position:absolute;top:537px;left:0}}
.blk.bottom .h{{margin-bottom:34px}}
.small .s{{font-size:21px;line-height:1.62}}
.g{{position:absolute;background:#72CBDF;opacity:.9}}"""
grid='<div class="g" style="left:413px;top:0;width:2px;height:100%"></div><div class="g" style="left:667px;top:0;width:2px;height:100%"></div><div class="g" style="top:516px;left:0;height:2px;width:100%"></div><div class="g" style="top:834px;left:0;height:2px;width:100%"></div><div class="g" style="left:55px;top:0;width:1px;height:100%;opacity:.5"></div><div class="g" style="left:1025px;top:0;width:1px;height:100%;opacity:.5"></div>' if GRID else ''
for i,(z,a,h,fs,s) in enumerate(fr,1):
    small=' small' if i==6 else ''
    al=' c' if a=='c' else ''
    open(f"v4_{i}{'g' if GRID else ''}.html","w",encoding="utf-8").write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css}</style></head><body><div class="f" style="background-image:url(v4/b{i}.jpg)"><div class="sc {z}"></div><div class="blk {z}{al}{small}"><p class="h" style="font-size:{fs}px">{h}</p><p class="s">{s}</p></div>{grid}</div></body></html>')
