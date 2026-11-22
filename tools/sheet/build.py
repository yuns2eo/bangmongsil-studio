import json, sys
from PIL import Image
R='/home/claude/bangmongsil-studio/'
def corner(p):
    im=Image.open(R+p).convert('RGB');w,h=im.size
    px=[im.getpixel((5,5)),im.getpixel((w-6,5)),im.getpixel((5,h-6)),im.getpixel((w-6,h-6))]
    c=[sorted(x[i] for x in px)[1] for i in range(3)]
    return '#%02x%02x%02x'%tuple(c)
S={
 'MONGSIL_Sheet_Felt':dict(name='MONGSIL',kr='몽실이',badge='3D FELT',d='characters/mongsil/references/3d/',
   turn=['Front','Left_3Q','Left_Profile','Back'],
   poses=[('Run','RUNNING','달리기'),('Sit','SITTING','앉기')],
   expr=[('Front','SMILE','기본 미소'),('Tongue','HAPPY','입 벌려 웃음')],
   paws=['characters/mongsil/references/3d/Paw_Front.png','characters/mongsil/references/3d/Paw_Hind.png'],
   L=[('EAR','귀 안쪽 #FFCDB4',27,15),('WHISKERS','볼에서 솟은 수염 한쪽 2가닥',32,37),('BLUSH','볼터치 #FFCDB4',37,40),('ARM','짧고 통통, 팔목 없음',27,70)],
   Rt=[('BROWN PATCH','머리 & 귀 물결 무늬 #B79571',62,20),('EYES','검정 #000000, 작은 눈',53,34),('MUZZLE','입주변 흰 돌출 2개',50,41),('ARM HEART','팔 하트 무늬 #B79571',64,63),('BELLY PATCH','배 가운데 원 #FFCDB4',49,70),('TAIL','갈색 초승달 꼬리',77,72)],
   pal=[('#FFCDB4','#FFCDB4','포인트 컬러','귀 & 볼 & 배 & 패드'),('#B79571','#B79571','갈색 무늬','머리 & 팔 하트 & 꼬리'),('#000000','#000000','검정','눈 & 코 & 수염')],note='',
   rules=['수염 한쪽 2가닥 (총 4가닥), 볼에서 솟은 입체','입주변 흰 돌출 2개, 입선 없음','갈색 #B79571은 머리 & 귀 물결, 팔 하트, 꼬리에만','머리는 가로로 넓은 타원, 전신 높이의 약 절반','팔다리는 짧고 통통, 팔목 & 발목 없음','젤리는 모양 그대로, 손바닥 방향을 따라 기운다','팔 안쪽이 보이는 자세는 팔 하트 생략 가능']),
 'MONGSIL_Sheet_Smooth':dict(name='MONGSIL',kr='몽실이',badge='3D SMOOTH',d='characters/mongsil/references/3d_smooth/',
   turn=['Front','Left_3Q','Left_Profile','Back'],
   poses=[('Run','RUNNING','달리기'),('Sit','SITTING','앉기'),('Wave','WAVING','손 흔들기')],
   expr=[('Front','SMILE','기본 미소'),('Tongue','HAPPY','입 벌려 웃음')],
   paws=['assets/props/detail/mongsil_3d_paw_front_smooth_v1.png','assets/props/detail/mongsil_3d_paw_hind_smooth_v1.png'],
   L=[('EAR','귀 안쪽 #FFCDB4',29,20),('WHISKERS','볼에서 솟은 수염 한쪽 2가닥',29,38),('BLUSH','볼터치 #FFCDB4',36,39),('ARM','짧고 통통, 팔목 없음',28,67)],
   Rt=[('BROWN PATCH','머리 & 귀 물결 무늬 #B79571',70,23),('EYES','검정 #000000, 작은 눈',50,35),('MUZZLE','입주변 흰 돌출 2개',46,41),('ARM HEART','팔 하트 무늬 #B79571',61,62),('BELLY PATCH','배 가운데 원 #FFCDB4',46,67),('TAIL','갈색 초승달 꼬리',73,62)],
   pal=[('#FFCDB4','#FFCDB4','포인트 컬러','귀 & 볼 & 배 & 패드'),('#B79571','#B79571','갈색 무늬','머리 & 팔 하트 & 꼬리'),('#000000','#000000','검정','눈 & 코 & 수염')],note='',
   rules=['수염 한쪽 2가닥 (총 4가닥), 볼에서 솟은 입체','입주변 흰 돌출 2개, 입선 없음','갈색 #B79571은 머리 & 귀 물결, 팔 하트, 꼬리에만','머리는 가로로 넓은 타원, 전신 높이의 약 절반','팔다리는 짧고 통통, 팔목 & 발목 없음','젤리는 모양 그대로, 손바닥 방향을 따라 기운다','팔 안쪽이 보이는 자세는 팔 하트 생략 가능']),
 'BANGSIL_Sheet_Felt':dict(name='BANGSIL',kr='방실이',badge='3D FELT',d='characters/bangsil/references/3d/',
   turn=['Front','Left_3Q','Left_Profile','Back'],
   poses=[('Run','RUNNING','달리기'),('Sit','SITTING','앉기')],
   expr=[('Front','SMILE','기본 미소 (W 입선)'),('Smile','HAPPY','입 벌려 웃음')],
   paws=['characters/bangsil/references/3d/Paw_Front.png','characters/bangsil/references/3d/Paw_Hind.png'],
   L=[('EAR','귀 안쪽 #FFCBD1',28,17),('CHEEK TUFTS','볼 털 한쪽 2개 (수염 없음)',19,37),('BLUSH','볼터치 #FFCBD1',35,39),('ARM','짧고 통통, 팔목 없음',27,74)],
   Rt=[('EYES','검정 #000000, 크고 둥근 눈',54,33),('W MOUTH','검정 W 입선, 평평한 얼굴',48,38),('BELLY PATCH','배 가운데 원 #FFCBD1',46,72),('TAIL','몸통색, 하나로 이어진 초승달',79,62),('FEET','짧은 발, 발목 없음',40,95)],
   pal=[('#FFCBD1','#FFCBD1','포인트 컬러','귀 & 볼 & 배 & 패드'),('#FBF8F5','WHITE / CREAM','몸통 색','몸 & 꼬리 같은 색'),('#000000','#000000','검정','눈 & 코 & W 입선')],note='NO BROWN & NO WHISKERS',
   rules=['수염 없음 & 볼 털 뭉치 한쪽 2개','갈색 없음 (눈 & 코 & 입선 모두 검정)','머리는 가로로 넓은 타원, 전신 높이의 약 절반','귀는 낮고 넓은 둥근 삼각형','팔다리는 짧고 통통, 팔목 & 발목 없음','젤리는 모양 그대로, 손바닥 방향을 따라 기운다']),
 'BANGSIL_Sheet_Smooth':dict(name='BANGSIL',kr='방실이',badge='3D SMOOTH',d='characters/bangsil/references/3d_smooth/',
   turn=['Front','Left_3Q','Left_Profile','Back'],
   poses=[('Run','RUNNING','달리기'),('Sit','SITTING','앉기'),('Wave','WAVING','손 흔들기'),('Cheer','CHEERING','신나서 점프')],
   expr=[('Front','SMILE','기본 미소 (W 입선)'),('Smile','HAPPY','입 벌려 웃음')],
   paws=['assets/props/detail/bangsil_3d_paw_front_smooth_v1.png','assets/props/detail/bangsil_3d_paw_hind_smooth_v1.png'],
   L=[('EAR','귀 안쪽 #FFCBD1',31,17),('CHEEK TUFTS','볼 털 한쪽 2개 (수염 없음)',19,37),('BLUSH','볼터치 #FFCBD1',35,38),('ARM','짧고 통통, 팔목 없음',25,72)],
   Rt=[('EYES','검정 #000000, 크고 둥근 눈',52,34),('W MOUTH','검정 W 입선, 평평한 얼굴',46,38),('BELLY PATCH','배 가운데 원 #FFCBD1',46,70),('TAIL','몸통색, 하나로 이어진 초승달',76,68),('FEET','짧은 발, 발목 없음',40,92)],
   pal=[('#FFCBD1','#FFCBD1','포인트 컬러','귀 & 볼 & 배 & 패드'),('#FBF8F5','WHITE / CREAM','몸통 색','몸 & 꼬리 같은 색'),('#000000','#000000','검정','눈 & 코 & W 입선')],note='NO BROWN & NO WHISKERS',
   rules=['수염 없음 & 볼 털 뭉치 한쪽 2개','갈색 없음 (눈 & 코 & 입선 모두 검정)','머리는 가로로 넓은 타원, 전신 높이의 약 절반','귀는 낮고 넓은 둥근 삼각형','팔다리는 짧고 통통, 팔목 & 발목 없음','젤리는 모양 그대로, 손바닥 방향을 따라 기운다']),
}
CSS='''*{box-sizing:border-box;margin:0;padding:0}body{width:1920px;height:1080px;background:#F7F7F8;font-family:"Noto Sans CJK KR","Noto Sans CJK JP",sans-serif;color:#111;position:relative;overflow:hidden;
background-image:linear-gradient(#ececee 1px,transparent 1px),linear-gradient(90deg,#ececee 1px,transparent 1px);background-size:40px 40px}
h1{position:absolute;left:50px;top:34px;font-size:40px;font-weight:900;letter-spacing:-.5px}h1 small{font-size:24px;font-weight:700;margin-left:6px}
.badge{position:absolute;right:50px;top:38px;background:#111;color:#fff;font-size:18px;font-weight:800;padding:7px 14px;border-radius:999px;letter-spacing:.5px}
.sec{position:absolute;font-size:16px;font-weight:800;letter-spacing:1.5px;color:#444}
.card{position:absolute;border-radius:12px;overflow:hidden;background-repeat:no-repeat;background-position:center}
.cap{position:absolute;text-align:center;font-size:15px;font-weight:800;line-height:1.25}.cap span{display:block;font-size:12px;font-weight:500;color:#555}
.lab{position:absolute;font-size:15px;font-weight:800;line-height:1.2}.lab span{display:block;font-size:11px;font-weight:500;color:#444}
.box{position:absolute;left:1020px;top:709px;width:860px;height:280px;background:#fff;border:1px solid #e3e3e6;border-radius:16px}
.sw{position:absolute;width:42px;height:42px;border-radius:9px;border:1px solid #e3e3e6}
.pt{position:absolute;font-size:15px;font-weight:800;line-height:1.2}.pt span{display:block;font-size:11px;font-weight:500;color:#444}
ul{position:absolute;list-style:none}li{font-size:15px;font-weight:700;margin-bottom:9px}li:before{content:"\\2022";margin-right:8px}
'''
def html(k,c):
    d=c['d'];o=[f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>']
    o.append(f'<h1>{c["name"]} CHARACTER SHEET<small>({c["kr"]} 캐릭터 시트)</small></h1><div class="badge">{c["badge"]}</div>')
    X0,W=50,932;g=16
    def card(x,y,w,h,src,lab,sub,zoom=None):
        bg=corner(src);url='file://'+R+src
        if zoom and zoom[0]==100:
            o.append(f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg}"><div style="position:absolute;inset:-20px;background:url({url}) center/100% 100% no-repeat;filter:blur(22px)"></div><div style="position:absolute;inset:0;background:url({url}) center/contain no-repeat"></div></div>')
            o.append(f'<div class="cap" style="left:{x}px;top:{y+h+12}px;width:{w}px">{lab}<span>{sub}</span></div>')
            return
        if zoom: style=f'background-image:url({url});background-size:{'cover' if zoom[0]==100 else str(zoom[0])+'%'};background-position:50% {zoom[1]}%;background-color:{bg}'
        else: style=f'background-image:url({url});background-size:contain;background-color:{bg}'
        o.append(f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{style}"></div>')
        o.append(f'<div class="cap" style="left:{x}px;top:{y+h+12}px;width:{w}px">{lab}<span>{sub}</span></div>')
    o.append('<div class="sec" style="left:50px;top:88px">TURNAROUND</div>')
    names={'Front':('FRONT VIEW','정면'),'Left_3Q':('3/4 VIEW','45도'),'Left_Profile':('SIDE PROFILE','측면'),'Back':('BACK VIEW','후면')}
    cw=(W-3*g)/4
    for i,t in enumerate(c['turn']): card(X0+i*(cw+g),110,cw,220,d+t+'.png',*names[t])
    n=len(c['poses']);px0=X0+(W-(n*cw+(n-1)*g))/2
    o.append(f'<div class="sec" style="left:{px0}px;top:403px">ACTION POSES</div>')
    for i,(f,a,b) in enumerate(c['poses']): card(px0+i*(cw+g),425,cw,cw,d+f+'.png',a,b)
    o.append('<div class="sec" style="left:50px;top:712px">EXPRESSIONS</div><div class="sec" style="left:%dpx;top:712px">PAWS</div>'%(X0+2*(cw+g)))
    for i,(f,a,b) in enumerate(c['expr']): card(X0+i*(cw+g),734,cw,220,d+f+'.png',a,b,zoom=(230,27))
    for i,(p,a,b) in enumerate([(c['paws'][0],'PALM','손바닥: 큰 젤리 1 + 발가락 젤리 3'),(c['paws'][1],'SOLE','발바닥: 큰 젤리 1 + 발가락 젤리 3')]):
        card(X0+(2+i)*(cw+g),734,cw,220,p,a,b,zoom=(178,50))
    # anatomy
    o.append('<div class="sec" style="left:1020px;top:88px">ANATOMY</div>')
    AX,AY,AS=1205,110,500
    card(AX,AY,AS,AS,d+'Front.png','','')
    o.pop()
    svg=[f'<svg style="position:absolute;left:0;top:0" width="1920" height="1080">']
    def ys(nn,top,bot): return [top+(bot-top)*i/(nn-1) for i in range(nn)] if nn>1 else [top]
    for side,items,lx in (('L',c['L'],1180),('R',c['Rt'],1730)):
        Y=ys(len(items),165,560)
        for (t,s,px,py),y in zip(items,Y):
            x=AX+AS*px/100;yy=AY+AS*py/100
            if side=='L':
                o.append(f'<div class="lab" style="left:{lx-330}px;width:330px;top:{y-12}px;text-align:right">{t}<span>{s}</span></div>')
                svg.append(f'<polyline points="{lx+2},{y+8} {lx+16},{y+8} {x:.1f},{yy:.1f}" fill="none" stroke="#111" stroke-width="1.3"/>')
            else:
                o.append(f'<div class="lab" style="left:{lx}px;width:180px;top:{y-12}px">{t}<span>{s}</span></div>')
                svg.append(f'<polyline points="{lx-2},{y+8} {lx-16},{y+8} {x:.1f},{yy:.1f}" fill="none" stroke="#111" stroke-width="1.3"/>')
            svg.append(f'<circle cx="{x:.1f}" cy="{yy:.1f}" r="4.5" fill="#fff" stroke="#111" stroke-width="1.5"/>')
    svg.append('</svg>');o+=svg
    # palette & rules
    o.append('<div class="box"></div><div class="sec" style="left:1045px;top:728px">COLOR PALETTE</div><div class="sec" style="left:1355px;top:728px">KEY RULES</div>')
    for i,(col,t,s1,s2) in enumerate(c['pal']):
        y=766+i*64
        o.append(f'<div class="sw" style="left:1045px;top:{y}px;background:{col}"></div><div class="pt" style="left:1100px;top:{y-2}px">{t}<span>{s1}</span><span>{s2}</span></div>')
    if c['note']: o.append(f'<div style="position:absolute;left:1045px;top:962px;font-size:12px;font-weight:800;color:#D3263A">{c["note"]}</div>')
    o.append('<ul style="left:1355px;top:762px">'+''.join(f'<li>{r}</li>' for r in c['rules'])+'</ul>')
    o.append('</body></html>');return '\n'.join(o)
import os
out=os.path.dirname(os.path.abspath(__file__))
for k,c in S.items():
    open(f'{out}/{k}.html','w').write(html(k,c))
print('ok')
