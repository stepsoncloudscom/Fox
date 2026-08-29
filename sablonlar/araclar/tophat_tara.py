"""Düşük kontrastlı marka izi (kabartma / gri baskı) — tophat + blackhat metin tespiti.
Parlaklık eşiği yerine YEREL KONTRAST kullanır, iki kutuplu (açık-üstü-koyu ve tersi)."""
import json, os, cv2, numpy as np
S=os.path.dirname(os.path.abspath(__file__))
L=json.load(open(S+"/dosya_listesi.json"))
def yukle(p):
    a=cv2.imread(p,cv2.IMREAD_UNCHANGED)
    if a is None: return None,None
    if a.ndim==3 and a.shape[2]==4:
        al=a[:,:,3]; b=a[:,:,:3].copy(); b[al<128]=(255,255,255); return b,al
    return (a if a.ndim==3 else cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)),None
def harf_dizisi(mask):
    n,lab,st,cen=cv2.connectedComponentsWithStats(mask,8)
    bl=[(st[i,0],st[i,1],st[i,2],st[i,3],st[i,4],cen[i]) for i in range(1,n) if 6<=st[i,4]<=4000]
    if len(bl)<3: return None
    yuk=np.array([b[3] for b in bl]); med=float(np.median(yuk))
    if med<4: return None
    sec=[b for b in bl if 0.5*med<=b[3]<=1.8*med and b[2]<=med*2.0]
    if len(sec)<3: return None
    cx=np.array([b[5][0] for b in sec]); cy=np.array([b[5][1] for b in sec])
    if cx.std()>cy.std():
        if cy.std()>med*0.4: return None
        yay=cx.max()-cx.min()
    else:
        if cx.std()>med*0.4: return None
        yay=cy.max()-cy.min()
    if yay < med*1.5: return None
    xs=[b[0] for b in sec]; ys=[b[1] for b in sec]
    xe=[b[0]+b[2] for b in sec]; ye=[b[1]+b[3] for b in sec]
    return (min(xs),min(ys),max(xe)-min(xs),max(ye)-min(ys),len(sec))
bulgu={}
for i,(d,f,p) in enumerate(L,1):
    b,al=yukle(p)
    if b is None: continue
    H,W=b.shape[:2]; ol=1000/max(W,H)
    s=cv2.resize(b,(int(W*ol),int(H*ol)),interpolation=cv2.INTER_AREA)
    g=cv2.cvtColor(s,cv2.COLOR_BGR2GRAY)
    cek=np.ones((9,9),np.uint8)
    th=cv2.morphologyEx(g,cv2.MORPH_TOPHAT,cek)      # koyu zeminde açık yazı
    bh=cv2.morphologyEx(g,cv2.MORPH_BLACKHAT,cek)    # açık zeminde koyu yazı
    kabul=[]
    for ad,resp in (("acik",th),("koyu",bh)):
        m=(resp>max(9,int(np.percentile(resp,99.4)))).astype(np.uint8)*255
        grup=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((5,17),np.uint8))
        n,lab,st,_=cv2.connectedComponentsWithStats((grup>0).astype(np.uint8),8)
        for j in range(1,n):
            x,y,w,h,alan=st[j]
            if max(w,h)<25 or max(w,h)>300 or min(w,h)<7: continue
            r=max(w,h)/min(w,h)
            if r<1.7 or r>8: continue
            sonuc=harf_dizisi(m[y:y+h, x:x+w])
            if not sonuc: continue
            hx,hy,hw,hh,adet=sonuc
            if max(hw,hh)<25: continue
            kabul.append({"x":int(x+hx),"y":int(y+hy),"w":int(hw),"h":int(hh),"harf":int(adet),"tip":ad})
    # örtüşenleri tekille
    kabul.sort(key=lambda z:-z["harf"]); kal=[]
    for z in kabul:
        if all(not(abs(z["x"]-q["x"])<max(z["w"],q["w"])*0.6 and abs(z["y"]-q["y"])<max(z["h"],q["h"])*0.6) for q in kal): kal.append(z)
    if kal: bulgu[os.path.join(d,f)]=kal[:5]
    if i%50==0: print(f"  {i}/{len(L)} · bulgulu {len(bulgu)}",flush=True)
json.dump(bulgu,open(S+"/tophat.json","w"),ensure_ascii=False)
print(f"BITTI · {len(bulgu)}/{len(L)} görsel · {sum(len(v) for v in bulgu.values())} aday",flush=True)
