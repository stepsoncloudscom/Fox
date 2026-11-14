# 02 CloudOne nedir — kare üretici. Izgara: 1080x1350, kenar 55, altın dikey 413/667, yatay 516/834.
# Punto (Fibonacci): başlık 233 / 144, alt satır 34. Yazı birebir metin.md "Kare üstü yazılar".
import sys, json
from PIL import Image, ImageDraw, ImageFont
F="/Users/ayhanerden/Fox/assets/fonts/"
W,H=1080,1350; M=55
def render(spec, src, out, grid=False, preview=None):
    im=Image.open(src); icc=im.info.get('icc_profile'); sw,sh=im.size
    s=spec.get('scale',1.0)            # kırpma genişliği / kaynak genişliği
    cw=round(sw*s); ch=round(cw*5/4)
    if ch>sh: ch=sh; cw=round(ch*4/5)
    x0=round((sw-cw)*spec.get('fx',0.5)); y0=round((sh-ch)*spec.get('fy',0.5))
    base=im.crop((x0,y0,x0+cw,y0+ch)).convert('RGB').resize((W,H),Image.LANCZOS)
    hs=spec['hsize']; hf=ImageFont.truetype(F+"BebasNeue-Regular.ttf",hs)
    sf=ImageFont.truetype(F+"Comfortaa-Regular.ttf",34)
    lh=round(hs*0.84); slh=51
    hl=spec['head']; sl=spec['sub']
    asc=hf.getbbox("H")[1]            # büyük harf üst boşluğu
    capb=hf.getbbox("H")[3]           # taban çizgisi (bbox altı)
    x=spec.get('x',M)
    if spec['zone']=='top':
        base_y=spec.get('line',516)                 # son başlık satırının tabanı altın çizgiye oturur
        tops=[base_y-capb-(len(hl)-1-i)*lh for i in range(len(hl))]
        sub_top=base_y+34
    else:
        sub_bottom=H-M
        sub_top=sub_bottom-len(sl)*slh+(slh-38)     
        base_y=sub_top-34
        tops=[base_y-capb-(len(hl)-1-i)*lh for i in range(len(hl))]
    # yumuşak gölge zemini (scrim): yalnız yazı bandında, kenara doğru sönen
    sc=spec.get('scrim',0.0)
    if sc>0:
        y_a=max(0,tops[0]+asc-140); y_b=min(H,sub_top+len(sl)*slh+120)
        mask=Image.new('L',(W,H),0); md=ImageDraw.Draw(mask)
        mid_a=tops[0]+asc-20; mid_b=sub_top+len(sl)*slh
        for y in range(y_a,y_b):
            if y<mid_a: a=(y-y_a)/max(1,mid_a-y_a)
            elif y>mid_b: a=1-(y-mid_b)/max(1,y_b-mid_b)
            else: a=1
            md.line([(0,y),(W,y)],fill=int(255*sc*max(0,min(1,a))))
        dark=Image.new('RGB',(W,H),(16,16,16))
        base=Image.composite(dark,base,mask)
    d=ImageDraw.Draw(base)
    for t,yt in zip(hl,tops): d.text((x-hf.getbbox(t)[0],yt),t,font=hf,fill=(255,255,255))
    for i,t in enumerate(sl): d.text((x,sub_top+i*slh-3),t,font=sf,fill=(255,255,255))
    if grid:
        g=(114,203,223)
        for gx in (413,667): d.line([(gx,0),(gx,H)],fill=g,width=2)
        for gy in (516,834): d.line([(0,gy),(W,gy)],fill=g,width=2)
        for gx in (M,W-M): d.line([(gx,0),(gx,H)],fill=g,width=1)
        d.line([(0,H-M),(W,H-M)],fill=g,width=1)
    if preview: base.resize(preview,Image.LANCZOS).save(out,quality=88)
    else:
        kw=dict(quality=95,subsampling=0,optimize=True)
        if icc: kw['icc_profile']=icc
        base.save(out,'JPEG',**kw)
    return dict(box=(x0,y0,x0+cw,y0+ch),tops=tops,base_y=base_y,sub_top=sub_top)
if __name__=='__main__':
    spec=json.loads(sys.argv[1]); print(render(spec,sys.argv[2],sys.argv[3],grid=len(sys.argv)>4 and sys.argv[4]=='g',preview=(540,675) if len(sys.argv)>4 else None))
