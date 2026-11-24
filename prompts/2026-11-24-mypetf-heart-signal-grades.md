# 마이펫프 하트시그널 등급 이미지 3D 매끈 (2026-11-24)

- 날짜: 2026-11-23 ~ 2026-11-24
- 캐릭터: 방실 (강아지 등급) & 몽실 (고양이 등급), 한 프롬프트에 한 캐릭터
- 요청(한국어): 펫프렌즈 앱 개인화 3.0, 마이펫프 회원 등급(평생연분 & 심쿵주의 & 콩닥콩닥 & 두근두근 & 몽글몽글 & 설렘시작)별 프로필 이미지를 3D로. 최종은 120×100 GIF, 고화질로 뽑아 크기만 줄인다. 모션은 지금 2D와 같지 않아도 되고 등급별로 이야기가 이어지면 된다. 재질 매끈, 방실 먼저
- 경로: B (ChatGPT 크롬) & 16:9 & 1장씩
- 미리보기: Figma PDS 파일 `마이펫프 X` 페이지, 실제 노출 슬롯(81×72)에 360×300 크롭을 넣고 밑에 원본을 둠
- 크롭: 피사체 bbox 기준 6:5, `ch = max(gh*1.08, gw*1.06/1.2)`, `cw = 1.2*ch`, 흰 캔버스에 음수 오프셋으로 붙여 넣기(범위 밖 검정 방지) → 360×300

## 등급별 결과 & 상태

| 등급 | 장면 | 방실 | 몽실 |
|---|---|---|---|
| 설렘시작 | 하트 상자 속에서 눈만 빼꼼 | `grade1_seollem_v4` **승인** ("몽실이도 이버전으로 만들어줘") | `grade1_seollem_v1` 미확인 (다음 등급으로 넘어감) |
| 심쿵주의 | 상자 위로 반쯤 올라와 진한 하트를 듦 | `grade2_heartbox_v5` 미확인 | `grade_simkung_v1` **승인** ("저걸로 몽실이도 제작해주고 심쿵주의 시안은 이걸로") |
| 두근두근 | 서서 더 큰 하트를 안음 | `grade_dugeun_v1` **승인** ("응 좋아 몽실이도 만들어줘") | `grade_dugeun_v1` 미확인 (다음 등급으로 넘어감) |
| 콩닥콩닥 | 45도로 돌아 살짝 앉아 하트를 껴안음 & 행복한 표정 | `grade_kongdak_v5` **승인** ("응 몽실이도 이렇게 만들어줘") | `grade_kongdak_v1` → 사용자가 Figma에서 팔 하트 위치를 직접 고친 버전 **승인** ("이걸로 올려줘") |
| 몽글몽글 & 평생연분 | — | 진행 전 | 진행 전 |

- 등급 문구는 사용자가 Figma에서 직접 바꾼 것이 있어 프레임 이름과 다를 수 있다

## 콩닥콩닥 진행 (단계 순서대로)

1. ② 정면 + 소품: 시트 + `3d_smooth/Front.png`, 배경 #E4DFE3, 정면 자세로 진한 핑크 하트 옆에 섬
2. ③ 자세 변경: 뷰를 추천하고 답을 받은 뒤 생성
   - 방실: 시트 + ② 결과 + `Sit` + `Left_3Q` + `Smile` → 마지막에 행복한 표정만 다시 (자세 타겟 + `Smile` + `Left_3Q`)
   - 몽실: 시트 + ② 결과 + `Sit` + `Left_3Q` + `Tongue` (사용자 확인 "응"), 처음부터 흰 배경 & 자연 그림자로 생성
3. 몽실 결과의 팔 하트가 바깥 팔에 찍혀 나와(락 기준은 꼬리 쪽 위팔 안쪽 가장자리) 사용자가 Figma에서 직접 수정

## 최종 프롬프트 — 몽실 콩닥콩닥 ③ (승인)

```
Create one new image. Aspect ratio 16:9 landscape.

Attached images, in order:
1. Character sheet — identity reference only.
2. STEP 1 image — the SAME MONGSIL and the SAME heart. Keep the face, eyes, markings, colours, whiskers, the heart's colour, shape and size, and their size ratio exactly. Only the pose and expression change.
3. MONGSIL smooth sitting pose — how the legs, body and tail look when sitting.
4. MONGSIL smooth three-quarter view — the body and head angle turned toward screen left, and where the brown markings sit at that angle.
5. MONGSIL smooth tongue expression — the happy open-mouth expression to use.

The attached character sheet is an identity reference only: match the character's shape, proportions, face, markings and colours exactly, but do not reproduce the sheet layout, grid background, labels, text, leader lines or multiple views.

# MONGSIL hugging the heart with a genuinely happy smile

## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown whenever that inner edge faces the camera in any pose including walking, running, and sitting; omitted when the edge is turned away or covered. When that arm is raised or opened so its inner palm side faces the camera (raised arms, waving, arms spread), the heart may be left out; never move it elsewhere.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: genuinely happy and delighted, exactly like the tongue reference: small eyes OPEN, the mouth opened below the raised muzzle bumps into a happy smile with a small soft pink tongue, no teeth and no fangs, no drawn mouth line, rosy blush.

## Orientation
- Body faces: a clear 45-degree three-quarter turn toward screen left, toward the heart, like reference 4
- Head faces: three-quarter toward screen left, leaning into the heart, both eyes visible
- Eyes: open, looking softly toward the camera
The head turns on the body naturally with no visible neck. The brown ear and head wave marking, the arm heart and the brown tail stay on MONGSIL's own left side (screen right at this angle) and never mirror.

## Pose & Paws
The heart stands upright on the floor on screen left, the same heart as in STEP 1. MONGSIL sits low on the floor right next to it, body turned 45 degrees toward the heart, chest pressed against the heart's right side, head leaning into the heart with one cheek resting against its upper right lobe.
MONGSIL fully embraces the heart: the near arm (closest to the camera) wraps across the front of the heart with its paw resting on the heart's front surface; the far arm goes around the back of the heart and is completely hidden. Only ONE front paw is visible — no second paw anywhere, no paw stacked under another paw.
The hind feet sit on the floor in front, like the sitting reference.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Heart: exactly the heart from STEP 1 — deep vivid pink #FF3D7F, smooth soft matte, very round top lobes with a deep top cleft, soft rounded point. Same size relative to MONGSIL as in STEP 1.

## Environment
Pure white #FFFFFF seamless studio background everywhere, including the floor, with a soft, natural contact shadow directly under the heart and MONGSIL where they touch the floor — soft and diffused, fading out naturally, no hard edges, no flat oval disc. No other objects.

## Camera
Front view of the scene, eye level, everything fully in frame, nothing cropped. The heart + character group is compact and centred.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure and prop. Very soft satin response to light with broad gentle highlights only. No felt pile, no fur, no mirror gloss, no outlines.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays a broad oval clearly wider than tall, fills the top half of the figure, and stays wider than the torso.
3. The brown wave marking stays on MONGSIL's own left ear and upper head (screen right in front view), with the whole outer ear brown and the wave contour intact and not mirrored.
4. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
4-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
5. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.22 of the head's maximum width long.
5-1. The eyes stay SMALL and close-set: each about 0.037 of the head's maximum width, centres about 0.157 of that width apart. Large or wide-set eyes are BANGSIL's face.
6. The mouth opens below the raised muzzle bumps exactly like the tongue reference, with a small pink tongue; no drawn W line. No tooth or fang appears anywhere.
7. Colours stay literal: brown #B79571, inner ears, blush and belly patch #FFCDB4, features #000000. #FFCBD1 never appears.
8. The body stays chubby and round; arms and legs stay as short as the reference in every pose, and raised arms never press against the face.
9. Brown appears only on the ear and head wave marking, the heart on the inner tail-side upper arm (only when that inner edge is visible; it may be left out when the arm is raised or opened with its palm side to the camera), and the tail. No other spots anywhere on the body.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The face is MONGSIL's: small close-set OPEN eyes, raised muzzle bumps with the nose on top, two raised whiskers per side, happy open mouth with a small pink tongue as in the tongue reference. Never closed or curved eyes.
11. Exactly ONE front paw is visible, on the heart. The far paw is hidden behind the heart.
12. The heart is the same as STEP 1.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
pads pasted upright like a flat sticker, pad pattern not following the paw angle, toe pads pointing straight up on a tilted paw, distorted pad shapes,
extra characters, two cats, duplicated MONGSIL, BANGSIL, all-white cat with no brown, realistic cat,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, flat face without muzzle bumps, drawn mouth line, W-shaped mouth,
large eyes, wide-set eyes, oversized eyes,
brown whiskers, warm brown nose, reddish whiskers, missing whiskers, cheek fur tufts instead of whiskers,
teeth, fangs,
mirrored markings, brown marking on the wrong ear, missing ear wave marking, simplified round brown patch,
cloud-shaped arm marking, dot arm marking, arm marking on the outer arm or forearm,
extra brown spots on the body, calico patches,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
#FFCBD1, pink inner ears,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
white tail, squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
long fur, individual hairs, fabric seams, stitching, glossy plastic, vinyl shine, clay render,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
closed eyes, curved happy eyes, ^ ^ eyes, squinting, W-shaped mouth line, second front paw, two paws stacked, extra arm, extra paw, far paw visible, standing pose, side profile face, pale heart, flat heart, shallow heart cleft, heart with face, text on heart, multiple hearts, floating heart, grey background, grey floor, flat oval shadow, hard shadow edge, character sheet layout, multiple views, labels
```

## 최종 프롬프트 — 방실 콩닥콩닥 ③ 표정 (승인)

```
Create one new image. Aspect ratio 16:9 landscape.

Attached images, in order:
1. Character sheet — identity reference only.
2. POSE TARGET — the same BANGSIL hugging the same heart. Keep EXACTLY this pose, body angle, arm placement (only one front paw visible, the far arm hidden behind the heart), the heart, the sizes, the framing and the background.
3. BANGSIL smooth smile reference — the EXPRESSION to use: eyes open, large and wide-set, the W mouth opened into a happy rounded smile with a small pink tongue, no teeth.
4. BANGSIL smooth three-quarter view — the head shape at this angle.

The attached character sheet is an identity reference only: match the character's shape, proportions, face, markings and colours exactly, but do not reproduce the sheet layout, grid background, labels, text, leader lines or multiple views.

# STEP 2 — BANGSIL hugging the heart with a genuinely happy smile

## Subject
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.06 of the head's width across the cheeks, and the gap between their centres is about 0.22 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded black triangle nose sitting high, directly on the smooth face, its top level with the bottom of the eyes, and directly below it a drawn wide black W-shaped smile line.
NO whiskers of any kind. Instead, two small soft fur tufts on each side of the face, four in total, growing out of the lower cheek outline below the blush in the body colour: the upper tuft larger, the lower tuft smaller, both soft rounded points sweeping outward and slightly down, part of the head silhouette.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, nose and mouth line pure black #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail, no brown on the face.
Expression: genuinely happy and delighted, exactly like the smile reference: eyes OPEN, large and wide-set, the W mouth opened into a rounded happy smile with a small pink tongue, no teeth and no fangs, rosy blush.

## Orientation
- Body faces: three-quarter toward screen left, toward the heart, like reference 4
- Head faces: three-quarter toward screen left, tilted a little toward the heart, like reference 4
- Eyes: open, looking softly toward the camera
The head turns on the body naturally with no visible neck. The tail stays on BANGSIL's own left (screen right, behind) and never mirrors.

## Pose & Paws
Exactly the pose of the POSE TARGET: BANGSIL sits low next to the heart, body turned 45 degrees toward it, chest pressed against the heart's right side, head leaning into the heart. The near arm wraps across the front of the heart with one paw resting on it; the far arm goes around the back of the heart and is hidden. Only ONE front paw is visible. Hind feet on the floor.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Heart: exactly the heart from the POSE TARGET — deep vivid pink #FF3D7F, smooth soft matte, very round top lobes with a deep top cleft, soft rounded point. Same size relative to BANGSIL as in the POSE TARGET.

## Environment
Plain solid background #E4DFE3 with a soft contact shadow. No other objects.

## Camera
Front view of the scene, eye level, everything fully in frame, nothing cropped. The heart + character group is compact and centred.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure and prop. Very soft satin response to light with broad gentle highlights only. No felt pile, no fur, no mirror gloss, no outlines.

## Critical conditions (must all hold)
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn.
4. Both ears are low broad triangles with rounded tips, each clearly wider at the base than tall, matching each other, body-coloured outside with #FFCBD1 inside. Neither ear is a tall upright spike and neither tip comes to a point.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. There are NO whiskers anywhere on the face. Exactly two soft fur tufts per side grow out of the lower cheek outline, the upper one larger.
8-1. The eyes stay LARGE and wide-set: each about 0.06 of the head's width across the cheeks, centres about 0.22 of that width apart. Small, close-set eyes are MONGSIL's face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The face is the smile-reference face: eyes OPEN, large and wide-set, open W smile with a small pink tongue. Never closed or curved eyes, no teeth.
11. Exactly ONE front paw is visible, on the heart. The far paw is hidden.
12. Pose, heart, framing and background are the same as the POSE TARGET.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
pads pasted upright like a flat sticker, pad pattern not following the paw angle, toe pads pointing straight up on a tilted paw, distorted pad shapes,
extra characters, two cats, duplicated BANGSIL, MONGSIL, calico cat, brown patched cat, realistic cat,
brown marking, brown ear, brown head patch, brown tail, heart on the arm, any brown on the body,
#FFCDB4, #B79571, peach inner ears,
raised muzzle bumps, puffy white muzzle, missing mouth line, no smile line,
human body, long limbs, visible neck, separated fingers, pointing finger, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, folded ears, mismatched ears, teeth, fangs,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
whiskers, whisker rods, whisker lines, cat whiskers, printed whiskers, missing cheek tufts, long cheek hair, mane, spiky cheek fur,
small eyes, close-set eyes, tiny eyes,
brown eyes, brown nose, brown mouth line,
squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
fox ears, tall upright ears, pointed ear tips, sharp ear tips, narrow ears, ears taller than their base width,
tail invisible against the background,
long fur, individual hairs, fabric seams, stitching, glossy plastic, vinyl shine, clay render,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
closed eyes, curved happy eyes, ^ ^ eyes, squinting, sleeping face, second front paw, two paws stacked, extra arm, extra paw, far paw visible, standing pose, side profile face, one-eyed profile, pale heart, flat heart, shallow heart cleft, heart with face, text on heart, multiple hearts, floating heart, character sheet layout, multiple views, labels
```

## 검증 (각 락 9번)

| 항목 | 방실 콩닥콩닥 | 몽실 콩닥콩닥 |
|---|---|---|
| 세모 옆얼굴 | 통과 (45도에서도 아래 얼굴 둥긂) | 통과 |
| 머리 형태 & 크기 | 통과 | 통과 |
| 배 패치 (원) | 통과 | 통과 |
| 수염 / 볼 털 | 수염 없음 & 볼 털 2개씩 | 한쪽 2가닥 |
| 이빨 | 없음 (혀만) | 없음 (혀만) |
| HEX | #FFCBD1 | #FFCDB4 & 갈색 #B79571 |
| 발가락 패드 3개 | 보이는 발 통과 | 보이는 발 통과 |
| 꼬리 | 초승달 하나 | 갈색 초승달 하나 |
| 팔 하트 | 해당 없음 | 처음 결과는 바깥 팔 → 사용자 수정 |
| **섞임** | 없음 | 없음 |

## 실패 & 수정

- 단계를 건너뛰고(② 정면 + 소품 없이, ③ 뷰 추천 없이) 바로 자세를 만듦 → 얼굴이 틀어지고 표정이 지어낸 모양으로 나옴 (확인) → `CLAUDE.md` 작업 순서 ①②③을 그대로 따름 → 해결
- 방실 웃는 얼굴을 눈 감은 ^^ 모양으로 만듦 → 레퍼런스에 없는 표정 (확인, 사용자 "저런 표정은 없어") → `3d_smooth/Smile.png`(몽실은 `Tongue.png`)를 첨부하고 "eyes OPEN" & Negative `closed eyes, curved happy eyes, ^ ^ eyes` → 해결
- 측면(Profile) 뷰를 넣어 얼굴이 변형됨 (확인) → 45도 자세는 `Left_3Q`만 넣음 → 해결
- 하트를 껴안는 자세에서 먼 쪽 앞발이 가까운 발 밑에 하나 더 붙어 나옴 (확인) → 몸을 하트 쪽으로 45도 돌리고 "먼 팔은 하트 뒤로 돌아가 완전히 가려짐, 보이는 앞발은 하나" & Negative `second front paw, two paws stacked, far paw visible` → 방실 & 몽실 모두 해결
- 몽실 심쿵주의 & 방실 콩닥콩닥에서 결과를 이어서 고칠수록 얼굴이 틀어짐 (확인 2회) → 직전 결과는 **구도 타겟으로만** 넣고 얼굴은 정면 & 표정 레퍼런스에서 가져오게 새로 생성 → 해결
- 회색 배경을 픽셀로 흰색으로 바꿨더니 인위적인 타원 그림자가 남고, 픽셀로 더 고칠수록 이상해짐 (확인, 사용자 "아니 더이상한데") → ChatGPT 편집 1회로 흰 배경 & 자연 그림자로 바꿈. 이후 흰 배경이 최종인 컷은 처음부터 `Pure white #FFFFFF ... soft, natural contact shadow ... no flat oval disc`로 생성 → 몽실 콩닥콩닥에서 한 번에 통과
- 81×72 슬롯에서 연한 분홍 하트가 안 보임 (확인) → 진한 비비드 핑크 #FF3D7F & 윗부분 골을 깊게 & 둥근 위쪽 혹 → 심쿵주의 이후 모든 등급에서 잘 보임
- 하트 채도를 픽셀로 올렸더니 배 패치까지 같이 진해짐 (확인) → 색 보정은 픽셀로 하지 않고 생성 단계에서 정함

## 재사용 규칙

- 끌어안는 자세에서 앞발 하나만 보이게 하려면 몸을 소품 쪽으로 45도 돌리고 먼 팔을 소품 뒤로 숨긴다 (2회: 방실 & 몽실 콩닥콩닥)
- 두 번 이상 고쳐야 하면 직전 결과는 구도 타겟으로만 쓰고 얼굴은 레퍼런스에서 새로 가져온다 (2회: 몽실 심쿵주의 & 방실 콩닥콩닥)
- 작게 노출되는 하트는 #FF3D7F 비비드 핑크 & 깊은 골 (6컷 이상)
- 흰 배경이 최종이면 처음부터 흰 배경 & 자연 그림자로 생성 (실패 1 & 성공 1, 1회 더 확인 필요)
- [x] 템플릿 반영 (`templates/scene.md` 4번 & 6번)
- [ ] 락 & 스타일 반영 제안 (없음)
