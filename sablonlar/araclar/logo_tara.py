"""Össur kurumsal marka izlerini (kelime markası + ikon) site boyutunda tarar.
Ölçü (Ayhan, 29 Ağu): görsel sitede 1000px gösterilir; bu boyutta uzun kenarı
>=25px olan iz 'okunabilir' sayılır ve silinir. Altı bırakılır.
Ürün adı kabartmaları (REBOUND, CTi, Formfit, Unloader) KAPSAM DIŞI."""
import os, json, sys, cv2, numpy as np

KOK=os.path.expanduser("~/Desktop/Ossur-Ortez-Gorselleri")
SITE=1000          # sitedeki gösterim genişliği
ESIK_PX=25         # site boyutunda okunabilirlik eşiği
SKOR=0.55

def beyaza_yatir(p):
    a=cv2.imread(p,cv2.IMREAD_UNCHANGED)
    if a is None: return None
    if a.ndim==2: return cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)
    if a.shape[2]==4:
        al=a[:,:,3]; b=a[:,:,:3].copy(); b[al<128]=(255,255,255); return b
    return a

def kenar(g):
    g=cv2.GaussianBlur(g,(3,3),0)
    return cv2.normalize(cv2.magnitude(cv2.Sobel(g,cv2.CV_32F,1,0,ksize=3),
                                       cv2.Sobel(g,cv2.CV_32F,0,1,ksize=3)),None,0,255,cv2.NORM_MINMAX).astype(np.uint8)

def varyantlar(sablon, acilar, hedef_genislikler):
    S=cv2.cvtColor(sablon,cv2.COLOR_BGR2GRAY); out=[]
    for a in acilar:
        M=cv2.getRotationMatrix2D((S.shape[1]/2,S.shape[0]/2),a,1.0)
        c,s=abs(M[0,0]),abs(M[0,1])
        nw=int(S.shape[0]*s+S.shape[1]*c); nh=int(S.shape[0]*c+S.shape[1]*s)
        M[0,2]+=nw/2-S.shape[1]/2; M[1,2]+=nh/2-S.shape[0]/2
        r=cv2.warpAffine(S,M,(nw,nh),borderValue=255)
        for gw in hedef_genislikler:
            o=gw/max(nw,nh)
            w2,h2=int(nw*o),int(nh*o)
            if w2<10 or h2<10: continue
            out.append((a,gw,kenar(cv2.resize(r,(w2,h2),interpolation=cv2.INTER_AREA))))
    return out

def main():
    sablonlar=[]
    for ad,yol in [("kelime","kirp_a_kelime_markasi.png"),("ikon_kelime","kirp_b_kadran_logo.png")]:
        s=cv2.imread(yol)
        sablonlar.append((ad, varyantlar(s, range(0,360,15), [25,35,50,70,100,140,190])))
        print(f"{ad}: {len(sablonlar[-1][1])} varyant", flush=True)

    dosyalar=[]
    for d in sorted(os.listdir(KOK)):
        y=os.path.join(KOK,d)
        if not os.path.isdir(y) or d in ("_Ikon-Piktogram","_orijinal-yedek"): continue
        for f in sorted(os.listdir(y)):
            if not f.startswith("."): dosyalar.append((d,f,os.path.join(y,f)))
    print("taranacak görsel:",len(dosyalar), flush=True)

    sonuc={}
    for i,(d,f,p) in enumerate(dosyalar,1):
        b=beyaza_yatir(p)
        if b is None: continue
        ol=SITE/max(b.shape[:2])                      # site boyutuna indir
        g=cv2.cvtColor(cv2.resize(b,(int(b.shape[1]*ol),int(b.shape[0]*ol)),interpolation=cv2.INTER_AREA),cv2.COLOR_BGR2GRAY)
        G=kenar(g); bulunan=[]
        for ad,vs in sablonlar:
            for a,gw,t in vs:
                if t.shape[0]>=G.shape[0] or t.shape[1]>=G.shape[1]: continue
                r=cv2.matchTemplate(G,t,cv2.TM_CCOEFF_NORMED)
                ys,xs=np.where(r>=SKOR)
                for x,y in zip(xs,ys):
                    if max(t.shape)<ESIK_PX: continue
                    bulunan.append({"tip":ad,"skor":round(float(r[y,x]),3),"aci":a,
                                    "sx":int(x),"sy":int(y),"sw":int(t.shape[1]),"sh":int(t.shape[0]),
                                    "ox":int(x/ol),"oy":int(y/ol),"ow":int(t.shape[1]/ol),"oh":int(t.shape[0]/ol)})
        bulunan.sort(key=lambda b:-b["skor"]); kalan=[]
        for b2 in bulunan:
            if all(not (abs(b2["sx"]-k["sx"])<max(b2["sw"],k["sw"])*0.5 and
                        abs(b2["sy"]-k["sy"])<max(b2["sh"],k["sh"])*0.5) for k in kalan):
                kalan.append(b2)
        if kalan: sonuc[os.path.join(d,f)]=kalan[:12]
        if i%20==0: print(f"  {i}/{len(dosyalar)} · iz bulunan {len(sonuc)}", flush=True)
    json.dump(sonuc,open("logo_eslesme.json","w"),ensure_ascii=False)
    print(f"BITTI · iz bulunan görsel {len(sonuc)}/{len(dosyalar)} · toplam bölge {sum(len(v) for v in sonuc.values())}", flush=True)

main()
