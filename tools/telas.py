"""Fonds « voile à contre-jour » dessinés par calcul (aucune IA générative).
Plis de tissu = somme d'ondes déformées ; contre-jour = halo lumineux qui traverse le voile.
Couleurs = celles du voile de Julieta (photo de la page d'accueil) : terracotta, olive, sable."""
import numpy as np
from PIL import Image, ImageFilter
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / 'assets' / 'images' / 'textures'
OUT.mkdir(parents=True, exist_ok=True)
rng = np.random.default_rng(7)

def hexrgb(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)],float)/255

def ramp(t, stops):
    t=np.clip(t,0,1); pos=np.linspace(0,1,len(stops)); cols=np.array([hexrgb(s) for s in stops])
    out=np.zeros(t.shape+(3,))
    for c in range(3): out[...,c]=np.interp(t,pos,cols[:,c])
    return out

def smooth_noise(w,h,scale,seed):
    r=np.random.default_rng(seed); g=r.random((max(2,h//scale),max(2,w//scale)))
    im=Image.fromarray((g*255).astype('uint8')).resize((w,h),Image.BICUBIC).filter(ImageFilter.GaussianBlur(scale/3))
    return np.asarray(im,float)/255

def plis(w,h,seed,angle=0.25,n=5):
    """Plis longs et presque parallèles, qui se resserrent en haut comme un voile tenu."""
    y,x=np.mgrid[0:h,0:w].astype(float); x/=w; y/=h
    warp=smooth_noise(w,h,420,seed)
    r=np.random.default_rng(seed)
    f=np.zeros_like(x)
    for k in range(n):
        g=0.55+0.45*y                         # éventail : plis serrés en haut, ouverts en bas
        u=(x-0.5)/g+angle*y+0.05*np.sin(y*2.2+k)+0.04*warp
        f+=r.uniform(.5,1)/(k+1)**0.6*np.sin(u*r.uniform(3,11)*np.pi+r.uniform(0,6.3))
    f=(f-f.min())/(f.max()-f.min())
    return f, x, y

def couches(x,y,f,seed,stops,angle=0.35):
    """Voiles superposés en bandes obliques : transitions douces et ondulées,
    avec une ourlet légèrement plus dense là où deux voiles se chevauchent.
    Renvoie (couleur, ourlet)."""
    r=np.random.default_rng(seed); v=y-angle*(x-0.5)
    bords=np.sort(r.uniform(0.0,1.0,len(stops)-1))
    out=np.zeros(x.shape+(3,))+hexrgb(stops[0]); ourlet=np.zeros_like(x)
    for i,b in enumerate(bords):
        bb=b+0.035*np.sin(x*6.5+i*2.1)+0.015*np.sin(x*17+i)
        s_=1/(1+np.exp(-(v-bb)/0.018))
        out+=s_[...,None]*(hexrgb(stops[i+1])-hexrgb(stops[i]))
        ourlet+=np.exp(-((v-bb-0.02)/0.035)**2)
    return out, ourlet

def plis_fins(w,h,seed,angle=0.25):
    """Fronces fines de la mousseline : crêtes nettes, légèrement ondulées."""
    y,x=np.mgrid[0:h,0:w].astype(float); x/=w; y/=h
    r=np.random.default_rng(seed+50); warp=smooth_noise(w,h,240,seed+9)
    c=np.zeros_like(x)
    for k in range(3):
        g=0.5+0.5*y
        u=(x-0.5)/g+angle*y+0.12*warp+0.03*np.sin(y*5+k)
        c+=r.uniform(.5,1)*(1-np.abs(np.sin(u*r.uniform(4,10)*np.pi+r.uniform(0,6))))**2.5
    return c/c.max()

def froisse(w,h,seed):
    r=np.random.default_rng(seed); n=r.normal(0,1,(h//3,w//3))
    im=Image.fromarray(((n-n.min())/(n.max()-n.min())*255).astype('uint8')).resize((w,h),Image.BICUBIC)
    im=im.filter(ImageFilter.GaussianBlur(2.5)).rotate(0)
    a=np.asarray(im,float)/255; a=np.asarray(Image.fromarray((a*255).astype('uint8')).resize((w//6,h)).resize((w,h),Image.BICUBIC),float)/255
    return a-0.5

def grain(w,h,seed,amp):
    r=np.random.default_rng(seed); n=r.normal(0,1,(h,w))
    # trame légère du tissu : fils horizontaux/verticaux
    yy,xx=np.mgrid[0:h,0:w]; t=0.5*np.sin(xx*1.9)+0.5*np.sin(yy*2.3)
    return (n*0.6+t*0.4)*amp

def save(arr,name,q=70):
    im=Image.fromarray((np.clip(arr,0,1)*255).astype('uint8'))
    for wd in (1920,1200,720):
        r=im.resize((wd,round(im.height*wd/im.width)),Image.LANCZOS)
        r.save(OUT/f'{name}-{wd}.webp',quality=q,method=6)
        r.save(OUT/f'{name}-{wd}.avif',quality=q-22) if hasattr(Image,'AVIF') or True else None
        r.save(OUT/f'{name}-{wd}.jpg',quality=q+8,optimize=True,progressive=True)

def nuit(name,w=1920,h=1200,seed=3,lx=.72,ly=.35):
    f,x,y=plis(w,h,seed)
    cc,ourlet=couches(x,y,f,seed,['#C2694A','#A35B3D','#8A7148','#B59266','#D9BD94'])
    couleur=0.7*cc+0.3*ramp(x, ['#BA7757','#9C7A4E','#D4B890'])
    d=np.sqrt(((x-lx)*1.3)**2+(y-ly)**2)
    halo=np.exp(-(d/0.55)**2)                  # la lumière derrière le voile
    epais=0.35+0.65*f**1.6                     # creux de pli = tissu plus fin = plus lumineux
    lum=halo*(0.25+0.95*(1-epais))*(1-0.16*ourlet)+0.05*f
    voile=couleur*lum[...,None]*1.25
    # reflets de crête (fils éclairés)
    crete=np.clip((f-0.86)/0.14,0,1)**2*halo
    voile+=crete[...,None]*hexrgb('#FFE6C8')*0.35
    # bord turquoise discret, comme l'ornement
    
    noir=hexrgb('#0C0907')
    pf=plis_fins(w,h,seed)
    voile*=(1+0.5*froisse(w,h,seed+5)+0.45*pf-0.12)[...,None]
    voile+=(pf**3*halo*0.10)[...,None]*hexrgb('#FFE6C8')
    arr=noir+voile
    arr+=grain(w,h,seed,0.012)[...,None]
    save(Image.fromarray((np.clip(arr,0,1)*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2)) and arr, name)

def jour(name,w=1920,h=1200,seed=11):
    f,x,y=plis(w,h,seed,angle=-0.2,n=6)
    couleur,ourlet=couches(x,y,f,seed,['#E9B49A','#D8C2A0','#C9C09A','#EAD3B4'],angle=-0.3)
    lumiere=np.exp(-(((x-.3)*1.2)**2+((y-.2))**2)/0.35)
    base=hexrgb('#FFFBF6')
    # voile clair : on mélange la couleur selon l'épaisseur, très doux
    k=(0.16+0.42*f**1.3+0.08*ourlet)*(1-0.45*lumiere)
    arr=base*(1-k[...,None])+couleur*k[...,None]
    arr+=(lumiere*0.04)[...,None]
    pf=plis_fins(w,h,seed,angle=-0.2)
    arr-=(0.035*froisse(w,h,seed+5)*k*3)[...,None]
    arr-=(0.07*pf*k*2.2)[...,None]*(1-hexrgb('#A35B3D'))
    arr+=grain(w,h,seed,0.008)[...,None]
    save(arr,name,q=72)

if __name__=='__main__':
    nuit('voile-nuit')
    nuit('voile-nuit-2',seed=21,lx=.25,ly=.55)
    jour('voile-jour')
    print(sorted(p.name for p in OUT.iterdir()))
