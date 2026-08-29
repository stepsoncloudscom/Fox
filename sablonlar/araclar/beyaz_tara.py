"""Koyu malzeme üzerine BEYAZ ÖSSUR yazısı — harf dizisi testiyle.
Bileşen içinde benzer yükseklikte, aynı hat üzerinde >=3 harf bloğu arar.
Kutu, harf bloklarının sınırından üretilir (bileşenin tamamından değil)."""
import json, os, cv2, numpy as np
S=os.path.dirname(os.path.abspath(__file__))
L=json.load(open(S+"/dosya_listesi.json"))
def yukle(p):
    a=cv2.imread(p,cv2.IMREAD_UNCHANGED)
    if a is None: return None
    if a.ndim==3 and a.shape[2]==4:
        al=a[:,:,3]; b=a[:,:,:3].copy(); b[al<128]=(255,255,255); return b
    return a if a.ndim==3 else cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
def harf_dizisi(parlak_roi):
    """ROI içindeki parlak blobları harf dizisi olarak değerlendir."""
    n,lab,st,cen=cv2.connectedComponentsWithStats(parlak_roi,8)
    bl=[(st[i,0],st[i,1],st[i,2],st[i,3],st[i,4],cen[i]) for i in range(1,n) if st[i,4]>=6]
    if len(bl)<3: return None
    yuk=np.array([b[3] for b in bl]); med=np.median(yuk)
    sec=[b for b in bl if 0.45*med<=b[3]<=1.9*med and b[2]<=med*2.2]
    if len(sec)<3: return None
    cx=np.array([b[5][0] for b in sec]); cy=np.array([b[5][1] for b in sec])
    # yatay mı dikey mi hizalı: bir eksende yayılım, diğerinde darlık
    if cx.std()>cy.std():
        if cy.std()>med*0.45: return None
    else:
        if cx.std()>med*0.45: return None
    xs=[b[0] for b in sec]; ys=[b[1] for b in sec]
    xe=[b[0]+b[2] for b in sec]; ye=[b[1]+b[3] for b in sec]
    return (min(xs),min(ys),max(xe)-min(xs),max(ye)-min(ys),len(sec))
bulgu={}
for i,(d,f,p) in enumerate(L,1):
    b=yukle(p)
    if b is None: continue
    H,W=b.shape[:2]; ol=1000/max(W,H)
    s=cv2.resize(b,(int(W*ol),int(H*ol)),interpolation=cv2.INTER_AREA)
    g=cv2.cvtColor(s,cv2.COLOR_BGR2GRAY)
    koyu_g=cv2.dilate((g<110).astype(np.uint8),np.ones((25,25),np.uint8))
    parlak=((g>145)&(koyu_g>0)).astype(np.uint8)*255
    blok=cv2.morphologyEx(parlak,cv2.MORPH_CLOSE,np.ones((7,19),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats((blok>0).astype(np.uint8),8)
    kabul=[]
    for j in range(1,n):
        x,y,w,h,alan=st[j]
        if max(w,h)<25 or max(w,h)>320 or min(w,h)<7: continue
        sonuc=harf_dizisi(parlak[y:y+h, x:x+w])
        if not sonuc: continue
        hx,hy,hw,hh,adet=sonuc
        if max(hw,hh)<25: continue
        oran=max(hw,hh)/max(1,min(hw,hh))
        if oran<1.6 or oran>8: continue
        kabul.append({"x":int(x+hx),"y":int(y+hy),"w":int(hw),"h":int(hh),"harf":int(adet)})
    if kabul: bulgu[os.path.join(d,f)]=sorted(kabul,key=lambda z:-z["harf"])[:4]
    if i%50==0: print(f"  {i}/{len(L)} · bulgulu {len(bulgu)}",flush=True)
json.dump(bulgu,open(S+"/beyaz_baski.json","w"),ensure_ascii=False)
print(f"BITTI · {len(bulgu)}/{len(L)} görsel · {sum(len(v) for v in bulgu.values())} aday",flush=True)
