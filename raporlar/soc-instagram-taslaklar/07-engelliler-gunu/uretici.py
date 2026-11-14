import sys
F=sys.argv[1]
fr=[
 ("top","YARIN<br>KURMAYACAĞIMIZ<br>CÜMLELER",144,"Dört kalıp. Bizim hesabımızda yok.",False),
 ("top","“KUTLU<br>OLSUN”",233,"Bugün haklar konuşulur.<br>Kimsenin tebrik edilecek bir durumu yok.",True),
 ("top","“HEPİMİZ<br>ENGELLİ<br>ADAYIYIZ”",144,"Eşitlik, “bir gün bana da olur”<br>diye istenmez.",True),
 ("top","“SEVGİ HER<br>ENGELİ AŞAR”",144,"Merdiveni sevgi kaldırmaz.<br>Rampa yapılır.",True),
 ("top","“BUNA RAĞMEN<br>ÇOK İYİSİN”",144,"“Buna rağmen”i çıkar.<br>Cümle yine doğru.",True),
 ("bottom","3 ARALIK",233,"Dünya Engelliler Günü.<br>Yarın bu dört cümle bizde yok.",False),
]
css=f"""@font-face{{font-family:Bebas;src:url(file://{F}/BebasNeue-Regular.ttf)}}
@font-face{{font-family:Comf;src:url(file://{F}/Comfortaa-Regular.ttf)}}
html,body{{margin:0}} .f{{position:relative;width:1080px;height:1350px;overflow:hidden;color:#fff;background-size:cover;background-position:center}}
.sc{{position:absolute;left:0;width:100%}}
.sc.top{{top:0;height:900px;background:linear-gradient(180deg,rgba(0,0,0,.62) 0%,rgba(0,0,0,.42) 60%,rgba(0,0,0,0) 100%)}}
.sc.bottom{{bottom:0;height:900px;background:linear-gradient(0deg,rgba(0,0,0,.66) 0%,rgba(0,0,0,.40) 60%,rgba(0,0,0,0) 100%)}}
.blk{{position:absolute;left:55px;width:970px;display:flex;flex-direction:column}}
.blk.top{{top:0;height:516px;justify-content:flex-end}}
.blk.bottom{{bottom:55px;justify-content:flex-end}}
.h{{font-family:Bebas;font-weight:400;line-height:1.0;letter-spacing:-1px;margin:0}}
.h.x{{text-decoration:line-through;text-decoration-color:#72CBDF;text-decoration-thickness:8px}}
.s{{font:400 34px/1.5 Comf;margin:0;white-space:nowrap}}
.blk.top .s{{position:absolute;top:550px;left:0}}
.blk.bottom .h{{margin-bottom:34px}}"""
for i,(z,h,fs,s,x) in enumerate(fr,1):
    open(f"e7_{i}.html","w",encoding="utf-8").write(f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>{css}</style></head><body><div class="f" style="background-image:url(e7/b{i}.jpg)"><div class="sc {z}"></div><div class="blk {z}"><p class="h{" x" if x else ""}" style="font-size:{fs}px">{h}</p><p class="s">{s}</p></div></div></body></html>')
