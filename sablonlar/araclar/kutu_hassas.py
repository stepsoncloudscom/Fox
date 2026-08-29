"""Kaba kutuyu (gözle okunan) dar pencerede hassaslaştırır.
Renkli etiket: camgöbeği/mavi + içinde beyaz logo -> bileşenin bbox'ı.
Kabartma/baskı: yerel medyandan sapan en büyük bileşen."""
import json, os, cv2, numpy as np
S=os.path.dirname(os.path.abspath(__file__))
L=json.load(open(S+"/dosya_listesi.json")); B=json.load(open(S+"/bulgular.json"))

def yukle(p):
    a=cv2.imread(p,cv2.IMREAD_UNCHANGED)
    if a.ndim==3 and a.shape[2]==4:
        al=a[:,:,3]; b=a[:,:,:3].copy(); b[al<128]=(255,255,255); return b
    return a if a.ndim==3 else cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)

def hassas(bgr, kaba, pay=1.6):
    x,y,w,h=kaba
    cx,cy=x+w/2, y+h/2; W2,H2=w*pay, h*pay
    x0=max(0,int(cx-W2/2)); y0=max(0,int(cy-H2/2))
    x1=min(bgr.shape[1],int(cx+W2/2)); y1=min(bgr.shape[0],int(cy+H2/2))
    roi=bgr[y0:y1, x0:x1]
    if roi.size==0: return None,"bos"
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
    mavi=cv2.inRange(hsv,(85,70,50),(125,255,255))
    if mavi.mean()>6:                      # renkli etiket var
        m=cv2.morphologyEx(mavi,cv2.MORPH_CLOSE,np.ones((7,7),np.uint8))
        n,lab,st,_=cv2.connectedComponentsWithStats((m>0).astype(np.uint8),8)
        if n>1:
            i=1+int(np.argmax(st[1:,4]))
            bx,by,bw,bh,_=st[i]
            return (int(x0+bx), int(y0+by), int(bw), int(bh)), "etiket"
    g=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY).astype(np.float32)
    yerel=cv2.medianBlur(cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY),31).astype(np.float32)
    fark=np.abs(g-yerel)
    esik=max(8.0, float(np.percentile(fark,98))*0.45)
    m=(fark>esik).astype(np.uint8)*255
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((5,11),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats((m>0).astype(np.uint8),8)
    if n<=1: return None,"bulunamadi"
    # ROI merkezine en yakın, makul büyüklükte bileşen
    en=None
    for i in range(1,n):
        bx,by,bw,bh,alan=st[i]
        if alan<20: continue
        mx,my=bx+bw/2, by+bh/2
        d=((mx-roi.shape[1]/2)**2+(my-roi.shape[0]/2)**2)**0.5
        puan=alan/(1+d)
        if en is None or puan>en[0]: en=(puan,bx,by,bw,bh)
    if en is None: return None,"bulunamadi"
    _,bx,by,bw,bh=en
    return (int(x0+bx), int(y0+by), int(bw), int(bh)), "kabartma"

def main():
    cikti={}
    for k,v in B.items():
        if k.startswith("_"): continue
        d,f,p = L[int(k)-1]
        bgr=yukle(p); H,W=bgr.shape[:2]
        ol=1000/max(W,H); ox=(1000-W*ol)/2; oy=(1000-H*ol)/2
        liste=[]
        for (x,y,w,h) in v["kutular"]:
            kaba=(int((x-ox)/ol), int((y-oy)/ol), int(w/ol), int(h/ol))
            ince,tip=hassas(bgr,kaba)
            liste.append({"kaba":kaba,"ince":list(ince) if ince else None,"tip":tip})
        cikti[k]={"dosya":p,"boyut":[W,H],"izler":liste}
    json.dump(cikti,open(S+"/kutu_hassas.json","w"),ensure_ascii=False,indent=1)
    from collections import Counter
    print("görsel:",len(cikti),"· iz:",sum(len(v["izler"]) for v in cikti.values()))
    print(Counter(i["tip"] for v in cikti.values() for i in v["izler"]))
main()
