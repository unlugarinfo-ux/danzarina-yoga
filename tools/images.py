import sys, json
from PIL import Image, ImageFilter, ImageEnhance, ImageOps
import numpy as np
SRC='assets/images/originals/'; OUT='assets/images/optimized/'
def arr(im): return np.asarray(im).astype(np.float32)/255
def img(a): return Image.fromarray((np.clip(a,0,1)*255+0.5).astype(np.uint8))
def lift_shadows(im, amt):
    a=arr(im); L=a.mean(2,keepdims=True)
    boost=amt*(1-L)**2.2   # mostly affects darks
    return img(a+boost*(1-a)*0.9)
def ctrl_highlights(im, amt):
    a=arr(im); L=a.mean(2,keepdims=True)
    return img(a-amt*(L**4)*a*0.5)
def warm(im, r=1.0,g=1.0,b=1.0):
    a=arr(im); a[...,0]*=r; a[...,1]*=g; a[...,2]*=b; return img(a)
def soft_contrast(im, f): return ImageEnhance.Contrast(im).enhance(f)
def sat(im,f): return ImageEnhance.Color(im).enhance(f)
def local(im, pct=12, r=30): return im.filter(ImageFilter.UnsharpMask(radius=r, percent=pct, threshold=2))
def common(im):
    # very subtle shared grade: warm whites, basalt shadows
    a=arr(im); L=a.mean(2,keepdims=True)
    hi=np.clip((L-0.6)/0.4,0,1); lo=np.clip((0.35-L)/0.35,0,1)
    a=a+hi*np.array([0.012,0.006,-0.008])+lo*np.array([-0.004,0.0,0.006])
    return img(a)
manifest={}
def export(im, name, widths, q=(60,78,80)):
    im=im.convert('RGB'); W,H=im.size; out=[]
    for w in widths:
        if w>W: continue
        h=round(H*w/W); r=im.resize((w,h),Image.LANCZOS)
        base=f'{OUT}{name}-{w}'
        r.save(base+'.avif',quality=q[0]); r.save(base+'.webp',quality=q[1],method=6); r.save(base+'.jpg',quality=q[2],optimize=True,progressive=True)
        out.append(w)
    manifest[name]={'widths':out,'ratio':[W,H]}
def crop_ratio(im, rw, rh, cx=None, cy=None, box=None):
    if box: return im.crop(box)
    W,H=im.size
    if W/H>rw/rh: nw=round(H*rw/rh); x=(W-nw)//2 if cx is None else max(0,min(W-nw,cx-nw//2)); return im.crop((x,0,x+nw,H))
    nh=round(W*rh/rw); y=(H-nh)//2 if cy is None else max(0,min(H-nh,cy-nh//2)); return im.crop((0,y,W,y+nh))
O=lambda f: Image.open(SRC+f).convert('RGB')
# A hero
a=O('a-hero-couple-danse-prairie.jpg')
# version retouchée fournie par la propriétaire (11-11) : optimisation seule
export(a.crop((0,117,1076,722)),'hero-danse-a-deux-16x9',[768,1076])
export(a.crop((246,0,824,722)),'hero-danse-a-deux-4x5',[480,578])
# B BW
b=O('b-archive-nb-canape-champ.jpg')  # version retouchée fournie (sépia N&B)
export(b,'parcours-noir-et-blanc',[480,800,1200])
# C
c=O('c-danse-canape-paysage.jpg')
export(c.crop((0,50,1017,622)),'danse-canape-paysage',[480,800,1017])
# D
d=O('d-mouvement-sous-le-ciel.jpg')
export(d.crop((0,150,1600,950)),'mouvement-sous-le-ciel-2x1',[768,1280,1600])
export(d.crop((120,0,1080,1200)),'mouvement-sous-le-ciel-4x5',[480,800])
# E
e=O('e-danse-fleurs-violettes.jpg')
export(e.crop((0,120,1592,1182)),'danse-fleurs-violettes',[480,800,1200])
# F editorial portrait (only optimise)
f=O('f-portrait-editorial-julieta.png')
export(f,'portrait-editorial-julieta',[480,800,896])
# H real portrait
h=O('h-portrait-julieta-interieur.jpg')
export(h.crop((0,120,732,1035)),'julieta-portrait-interieur',[480,732])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
print(json.dumps(manifest))
# L : image artistique de Julieta (pose de danse) — optimisation seule
l=O('l-julieta-pose-danse-artistique.png')
export(l,'julieta-pose-danse-artistique',[480,800,896])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
# N : image d'accueil retenue par la propriétaire (11-11) — optimisation seule
n=O('n-hero-julieta-voile-terracotta.png')
export(n,'accueil-julieta-voile-terracotta',[720,1076])
export(n.crop((0,0,578,722)),'accueil-julieta-voile-terracotta-4x5',[480,578])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
# O : danse à deux sur terrasse face à la mer (image artistique fournie, 11-11) ; P-U : ambiances fournies (sans personnes identifiables)
export(O('o-danse-terrasse-mer.png'),'danse-terrasse-mer',[768,1280,1531])
export(crop_ratio(O('o-danse-terrasse-mer.png'),4,5,cx=820),'danse-terrasse-mer-4x5',[480,800])
for f,n in [('p-ambiance-bougie-lotus.png','ambiance-bougie-lotus'),('q-jardin-zen.png','ambiance-jardin-zen'),('r-eau-calme.png','ambiance-eau-calme'),('s-serviette-frangipanier.png','ambiance-frangipanier'),('t-sable-ondes.png','ambiance-sable-ondes'),('u-yoga-tapis-mains.png','ambiance-yoga-tapis')]:
    export(O(f),n,[720,1076])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
# X : danse sur le canapé, ciel et montagnes (photo d'origine fournie 11-11) — bandeau d'accueil
x_=O('x-danse-canape-ciel.jpg')
export(x_.crop((0,150,1024,662)),'danse-canape-ciel-2x1',[768,1024])
export(crop_ratio(x_,4,5,cx=360),'danse-canape-ciel-4x5',[480,614])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
# N2 : Julieta au sol, bras levé, grande étoffe terracotta (fournie 13-11) — nouvelle image d'accueil
manifest=json.load(open(OUT+'manifest.json'))
n2=O('n-hero-julieta-sol-voile.png')
export(n2,'accueil-julieta-sol-voile',[720,1076])
export(n2.crop((40,0,618,722)),'accueil-julieta-sol-voile-4x5',[480,578])
json.dump(manifest,open(OUT+'manifest.json','w'),indent=1)
