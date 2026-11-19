# 몽실 매끈 탐정 — STEP 1 의상 & 소품

- 날짜: 2026-11-19
- 캐릭터: 몽실
- 요청(한국어): 몽실 3D, 매끈 재질로. 탐정옷 같은 걸 입히고 손에는 돋보기 (사용자 첨부 이미지: 사람 아이 탐정 일러스트 — 의상 참고용, 생성에는 첨부 안 함)
- 상태: 실패 (사용자 수정 요청 → 다음 차수로 대체)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 3:4 (전신 의상 확인이라 3:4)
- Element: 몽실_3D_매끈 (d76af9ed-b1e7-4ba9-be0e-262a70fbde19)
- 첨부 레퍼런스: 없음 (정면)
- job: 2eb0310e-c00b-497f-bd4e-5e3a4380eef2
- 크레딧: 사용 0.5 (예상치, 표시 1) / 남은 989.5

## 결정 메모

- 사람 아이 탐정 이미지는 첨부하지 않았다. 사람 몸 & 얼굴이 섞일 위험이 있어 의상만 글로 옮겼다.
- 사냥모자는 귀 사이에 얹어 갈색 귀 & 웨이브 마킹을 가리지 않게 했다.
- 코트는 엉덩이까지, 앞을 열어 배 패치를 보이게 했다.
- 돋보기는 눈을 가리지 않게 얼굴 옆 볼 높이로 들게 했다 (눈 측정 & 섞임 판정을 위해).
- 매끈 재질이라 scene-blocks Negative의 재질 줄 `glossy plastic, vinyl shine, clay render`를 `felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look`으로 바꿨다. `styles/3D_Smooth.md` 2번과 충돌하기 때문이다. 매끈 장면이 더 나오면 scene-blocks에 매끈용 재질 줄을 따로 두는 걸 제안할 것.

## 최종 프롬프트

```
<<<d76af9ed-b1e7-4ba9-be0e-262a70fbde19>>> # MONGSIL detective — STEP 1 wardrobe & prop

## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown whenever that inner edge faces the camera in any pose including walking, running, and sitting; omitted only when the edge is turned away or covered.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: curious, confident little detective look, closed mouth.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all markings rotate with the head; markings stay on the character's anatomical left side and never mirror.

## Pose & Paws
MONGSIL stands upright. Its right arm (screen left) is raised only to shoulder height, still short, holding a magnifying glass by its handle so the round lens sits beside the face at cheek level on screen left — the lens does NOT cover the face or either eye. Its left arm (screen right) rests at its side.
The right paw wraps around the handle of the magnifying glass; the paw touches the handle.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette; the outline shows two separate shapes there, not one.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Magnifying glass: a round clear glass lens in a dark brown rim with a short dark brown handle. Lens upright, facing the camera, handle pointing down toward the paw.
Size: the lens is about a third of the width of the character's head.
Nothing is printed on it.

## Wardrobe
A small classic detective outfit, all in smooth matte material like the character:
- A small tan-brown plaid deerstalker cap with front and back peaks and little ear flaps tied up on top, perched on top of the head BETWEEN the ears. Both ears stay fully visible poking out on either side of the cap; the brown ear and the brown wave marking on the upper head stay visible and are not covered.
- A short tan trench coat / cape-collar coat that reaches only to the hips, worn OPEN at the front so the round belly patch stays clearly visible between the coat fronts. Short sleeves end above the paws.
- A small dark brown bow tie at the neck.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby below the coat. The tail stays visible.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet.

## Camera
Front view, eye level, full body from ear tips to feet, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured markings are integrated surface colour with clean edges. Paw pads, nose, the two muzzle bumps, and whisker rods are raised relief.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays a broad oval clearly wider than tall, fills the top half of the figure, and stays wider than the torso.
3. The brown wave marking stays on MONGSIL's own left ear and upper head (screen right in front view), with the whole outer ear brown and the wave contour intact and not mirrored.
4. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
4-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
5. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.22 of the head's maximum width long.
5-1. The eyes stay SMALL and close-set: each about 0.037 of the head's maximum width, centres about 0.157 of that width apart. Large or wide-set eyes are BANGSIL's face.
6. The closed mouth has no drawn mouth line: only the nose and the vertical groove between the two raised muzzle bumps. No tooth or fang appears anywhere.
7. Colours stay literal: brown #B79571, inner ears, blush and belly patch #FFCDB4, features #000000. #FFCBD1 never appears.
8. The body stays chubby and round; arms and legs stay as short as the reference in every pose, and raised arms never press against the face.
9. Brown appears only on the ear and head wave marking, the heart on the inner tail-side upper arm (only when that inner edge is visible), and the tail. No other spots anywhere on the body.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The coat is open at the front and the round belly patch stays visible.
11. The deerstalker cap sits between the ears; both ears and the brown head wave marking stay visible.
12. The magnifying glass lens sits beside the face and does not cover either eye; the paw holds the handle.
13. Smooth matte vinyl surface everywhere, on the character and the clothes — no felt texture.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated MONGSIL, BANGSIL, all-white cat with no brown, realistic cat,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, flat face without muzzle bumps, drawn mouth line, W-shaped mouth,
large eyes, wide-set eyes, oversized eyes,
brown whiskers, warm brown nose, reddish whiskers,
smile curve under the muzzle, teeth, fangs,
mirrored markings, brown marking on the wrong ear, missing ear wave marking, simplified round brown patch,
cloud-shaped arm marking, dot arm marking, arm marking on the outer arm or forearm,
extra brown spots on the body, calico patches,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
#FFCBD1, pink inner ears,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
white tail, squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, hat covering the ear marking, closed coat covering the belly patch, long coat, trousers, shoes,
lens covering the eye, magnifying glass floating, human child, human face
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 세모 옆얼굴 | 해당 없음 (정면) |
| 머리 형태 & 크기 | 통과. 머리폭 약 550px, 몸통보다 넓음, 전신 높이 절반 수준 |
| 귀 & 갈색 웨이브 | 통과. 화면 오른쪽 귀 전체 갈색, 웨이브 유지, 모자가 가리지 않음 |
| 배 패치 (원) | 통과. 열린 코트 사이 가운데 원 |
| 수염 (한쪽 2가닥) | 통과. 돋을 막대 |
| 입 & 이빨 | 통과. 입선 없음, 이빨 없음 |
| 얼굴 실측 | 통과. 눈폭 0.036 HW, 간격 0.157 HW (기준 0.037 & 0.157) |
| HEX & 섞임 | 통과. #FFCBD1 & 큰 눈 없음 |
| 팔 하트 | 통과. 꼬리쪽 팔 안쪽 위 |
| 팔 길이 & 얼굴 틈 | 통과. 든 팔 짧게 유지, 발이 얼굴 아래에서 떨어져 있음. 돋보기 테두리가 볼 가장자리 앞에 겹치는 건 소품이라 허용 |
| 발끝 세 마디 | 통과. 두 뒷발 3마디 & 홈 2개, 내린 앞발도 마디 보임. 돋보기 쥔 앞발은 감싼 형태 |
| 꼬리 | 주의. 하나로 이어진 초승달 & 위 덩이 가장 큼은 통과. 홈 깊이 대략 위 9% & 아래 6%로 기준(5~7% & 1~2%)보다 깊지만 15% 실패선 아래. 꼬리 안쪽 경계가 팔 & 코트에 가려 폭은 추정 |
| 매끈 재질 | 통과. 펠트 결 없음, 무광 비닐 & 클레이 |
| 의상 | 사냥모자 & 짧은 트렌치 & 나비넥타이. 바지 & 신발 없음 |

---

# 2차 — 실제 돋보기 & 셔츠 + 넥타이 + 트렌치 (1차 결과 1회 편집)

- 요청(한국어): 돋보기는 실제 돋보기(은색 테 & 검정 손잡이 사진 첨부), 의상 디테일 더, 코트 안에 셔츠 + 넥타이 + 바바리코트 (사람 아이 탐정 3D 이미지 첨부 — 의상 참고용, 생성에는 첨부 안 함)
- 상태: 실패 (사용자 수정 요청 → 다음 차수로 대체)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 3:4
- Element: 몽실_3D_매끈 (d76af9ed-b1e7-4ba9-be0e-262a70fbde19)
- medias: 1차 job 2eb0310e-c00b-497f-bd4e-5e3a4380eef2 (편집 기준, **1회 편집 사용함**) + 돋보기 사진 media 9f4c0020-deaf-4bef-bcad-6d3953187dad
- job: 9dace2da-e7a7-4d76-8bda-f27a6d799b41
- 크레딧: 사용 0.5 / 남은 989

## 결정 메모

- 셔츠가 배 패치를 덮지 않게 "윗가슴만 덮는 짧은 셔츠 앞판 + 배 패치 위에서 끝나는 넥타이"로 지시했다.
- 이 결과를 다시 고치려면 편집이 아니라 원본 레퍼런스로 새로 생성해야 한다 (`templates/scene.md` 6번, 편집 1회 제한).

## 최종 프롬프트

```
<<<d76af9ed-b1e7-4ba9-be0e-262a70fbde19>>> # MONGSIL detective — STEP 1 rev 2 (edit of the first attached image)

The FIRST attached image is the previous result of this exact MONGSIL. The SECOND attached image is the magnifying glass reference.
Keep EVERYTHING identical to the first image — the character, face, eyes, whiskers, ears, brown ear and head wave marking, belly patch, arm heart, tail, paws, body proportions, pose, camera, background colour, lighting, and the smooth matte material — except these changes:
1. Replace the magnifying glass with the real magnifying glass from the second attached image: a polished silver chrome round rim with a clear glass lens, a short silver chrome collar, and a glossy black cylindrical handle. Same shape and proportions as the reference. The right paw (screen left) still holds it by the black handle at the same place, lens beside the face at cheek level, not covering either eye.
2. Change the outfit to a white dress shirt + necktie + trench coat (classic belted trench coat), with more detail (see Wardrobe).
3. Give the deerstalker cap more detail (see Wardrobe).


## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown whenever that inner edge faces the camera in any pose including walking, running, and sitting; omitted only when the edge is turned away or covered.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: curious, confident little detective look, closed mouth.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all markings rotate with the head; markings stay on the character's anatomical left side and never mirror.

## Pose & Paws
MONGSIL stands upright. Its right arm (screen left) is raised only to shoulder height, still short, holding a magnifying glass by its handle so the round lens sits beside the face at cheek level on screen left — the lens does NOT cover the face or either eye. Its left arm (screen right) rests at its side.
The right paw wraps around the handle of the magnifying glass; the paw touches the handle.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette; the outline shows two separate shapes there, not one.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Magnifying glass: exactly the attached magnifying glass reference — polished silver chrome round rim around a clear glass lens, a short silver chrome collar with a small ring, and a glossy black cylindrical handle. Lens upright facing the camera, handle pointing down into the paw.
Size: the lens is about a third of the width of the character's head.
The prop keeps this shape; nothing is printed on it. Only the prop is glossy; the character stays smooth matte.

## Wardrobe
A detailed classic detective outfit, sized to the chubby mascot body:
- Deerstalker cap: fine brown-and-tan houndstooth / small check pattern, front and back peaks, side ear flaps tied up on top with a small brown ribbon bow, a small button on the crown. It sits on top of the head BETWEEN the ears; both ears stay fully visible on either side, and the brown ear and brown wave marking on the upper head stay visible.
- White dress shirt: a crisp white pointed collar visible at the neck, and a short shirt front covering only the upper chest, ending just ABOVE the round belly patch so the belly patch stays clearly visible below it.
- Necktie: a dark navy necktie with a neat knot, its tip ending above the belly patch.
- Trench coat: a camel / tan classic trench coat with wide notched lapels, a storm flap on one shoulder, shoulder epaulettes with buttons, double-breasted dark brown buttons, angled pocket flaps, cuffed sleeves with small cuff straps, and a waist belt with a buckle tied loosely at the back so the front stays OPEN. Coat length reaches only to mid-thigh. Worn open at the front so the shirt, tie, and the round belly patch are visible between the coat fronts. Sleeves end above the paws; the paws stay fully visible.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby below the coat. The tail stays visible beside the coat.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet.

## Camera
Front view, eye level, full body from ear tips to feet, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured markings are integrated surface colour with clean edges. Paw pads, nose, the two muzzle bumps, and whisker rods are raised relief.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays a broad oval clearly wider than tall, fills the top half of the figure, and stays wider than the torso.
3. The brown wave marking stays on MONGSIL's own left ear and upper head (screen right in front view), with the whole outer ear brown and the wave contour intact and not mirrored.
4. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
4-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
5. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.22 of the head's maximum width long.
5-1. The eyes stay SMALL and close-set: each about 0.037 of the head's maximum width, centres about 0.157 of that width apart. Large or wide-set eyes are BANGSIL's face.
6. The closed mouth has no drawn mouth line: only the nose and the vertical groove between the two raised muzzle bumps. No tooth or fang appears anywhere.
7. Colours stay literal: brown #B79571, inner ears, blush and belly patch #FFCDB4, features #000000. #FFCBD1 never appears.
8. The body stays chubby and round; arms and legs stay as short as the reference in every pose, and raised arms never press against the face.
9. Brown appears only on the ear and head wave marking, the heart on the inner tail-side upper arm (only when that inner edge is visible), and the tail. No other spots anywhere on the body.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The coat is open at the front; the shirt front and tie end above the belly patch, and the round belly patch stays clearly visible.
11. The deerstalker cap sits between the ears; both ears and the brown head wave marking stay visible.
12. The magnifying glass is the silver-rim, black-handle glass from the reference; its lens sits beside the face and does not cover either eye; the paw holds the black handle.
13. Smooth matte vinyl surface everywhere, on the character and the clothes — no felt texture.
14. Everything not listed in the changes stays identical to the first attached image.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated MONGSIL, BANGSIL, all-white cat with no brown, realistic cat,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, flat face without muzzle bumps, drawn mouth line, W-shaped mouth,
large eyes, wide-set eyes, oversized eyes,
brown whiskers, warm brown nose, reddish whiskers,
smile curve under the muzzle, teeth, fangs,
mirrored markings, brown marking on the wrong ear, missing ear wave marking, simplified round brown patch,
cloud-shaped arm marking, dot arm marking, arm marking on the outer arm or forearm,
extra brown spots on the body, calico patches,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
#FFCBD1, pink inner ears,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
white tail, squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, hat covering the ear marking, closed coat covering the belly patch, shirt covering the belly patch, tie covering the belly patch, long coat, trousers, shoes, waistcoat, vest,
lens covering the eye, magnifying glass floating, brown wooden magnifying glass, gold rim, human child, human face, change of character design
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 머리 형태 & 크기 | 통과 |
| 귀 & 갈색 웨이브 | 통과. 모자가 귀 사이, 웨이브 보임 |
| 배 패치 (원) | **주의.** 셔츠 앞판 & 넥타이가 위쪽 절반을 덮어 아래 반원만 보인다. 일부 보임이라 13번 실패는 아님. 원 모양 검증은 불가 |
| 수염 (한쪽 2가닥) | 통과 |
| 입 & 이빨 | 통과 |
| 얼굴 실측 | 통과. 눈폭 약 0.036 HW, 간격 약 0.155 HW |
| HEX & 섞임 | 통과 |
| 팔 하트 | 소매가 위팔을 덮어 안 보임 (가려짐 허용) |
| 팔 길이 & 얼굴 틈 | 통과. 돋보기 테가 볼 가장자리 앞에 겹침(소품) |
| 발끝 세 마디 | 통과. 두 뒷발 3마디 & 홈 2개. 쥔 앞발은 손잡이를 감싼 형태 |
| 꼬리 | 주의. 1차와 같음 — 초승달 & 위 덩이 최대, 홈이 기준보다 조금 깊음(15% 미만) |
| 매끈 재질 | 통과. 코트 소매 & 견장에 박음질 표현이 약간 있음 |
| 돋보기 | 통과. 은색 크롬 테 & 칼라 & 검정 손잡이, 사진과 같은 형태 |
| 의상 | 체크 사냥모자(리본) & 흰 셔츠 칼라 & 남색 넥타이 & 더블 단추 트렌치(라펠 & 견장 & 포켓 플랩 & 소매 스트랩) |

---

# 3차 — 코트 단추 4개 & 셔츠 길게 (원본 레퍼런스로 새로 생성)

- 요청(한국어): 2차 나쁘지 않음. 코트 단추 하나만 없애고(→ 확인 결과 양쪽 맨 아래 줄 제거, 총 4개), 셔츠가 상체를 더 길게 덮게(→ 확인 결과 배 패치 아래 끝만 보이게). 다른 수정 없음
- 사용자 승인: 배 패치는 아래 끝만 보이고 나머지는 셔츠에 가려져도 됨 (락 4번 & 9-13번 예외, 사용자 말로 확인)
- 상태: 승인 (2026-11-19 사용자 "승인, STEP 2로" — 손목 리터치본 기준)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 3:4
- Element: 몽실_3D_매끈 (d76af9ed-b1e7-4ba9-be0e-262a70fbde19)
- medias: 돋보기 사진 media 9f4c0020-deaf-4bef-bcad-6d3953187dad (2차 결과는 편집 1회 제한 때문에 넣지 않음)
- job: 04375046-62b5-4b25-bc59-71420d1527e5
- 크레딧: 사용 0.5 / 남은 988.5

## 최종 프롬프트

```
<<<d76af9ed-b1e7-4ba9-be0e-262a70fbde19>>> # MONGSIL detective — STEP 1 rev 3

The attached image is the magnifying glass reference only.

## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown whenever that inner edge faces the camera in any pose including walking, running, and sitting; omitted only when the edge is turned away or covered.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: curious, confident little detective look, closed mouth.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all markings rotate with the head; markings stay on the character's anatomical left side and never mirror.

## Pose & Paws
MONGSIL stands upright. Its right arm (screen left) is raised only to shoulder height, still short, holding a magnifying glass by its handle so the round lens sits beside the face at cheek level on screen left — the lens does NOT cover the face or either eye. Its left arm (screen right) rests at its side.
The right paw wraps around the handle of the magnifying glass; the paw touches the handle.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette; the outline shows two separate shapes there, not one.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Magnifying glass: exactly the attached magnifying glass reference — polished silver chrome round rim around a clear glass lens, a short silver chrome collar with a small ring, and a glossy black cylindrical handle. Lens upright facing the camera, handle pointing down into the paw.
Size: the lens is about a third of the width of the character's head.
The prop keeps this shape; nothing is printed on it. Only the prop is glossy; the character stays smooth matte.

## Wardrobe
A detailed classic detective outfit, sized to the chubby mascot body:
- Deerstalker cap: fine brown-and-tan houndstooth / small check pattern, front and back peaks, side ear flaps tied up on top with a small brown ribbon bow, a small button on the crown. It sits on top of the head BETWEEN the ears; both ears stay fully visible on either side, and the brown ear and brown wave marking on the upper head stay visible.
- White dress shirt: a crisp white pointed collar at the neck and a white shirt front that covers most of the torso, from the neck down over the chest and upper belly, ending just above the lower edge of the belly patch so that only the bottom edge of the round #FFCDB4 belly patch peeks out below the shirt hem as a small curved sliver.
- Necktie: a dark navy necktie with a neat knot, hanging straight down the shirt front, its tip ending on the shirt above the shirt hem.
- Trench coat: a camel / tan classic trench coat with wide notched lapels, a storm flap on one shoulder, shoulder epaulettes with buttons, double-breasted dark brown buttons — exactly FOUR buttons in total, two on each side in two rows (no third, lower row of buttons), angled pocket flaps, cuffed sleeves with small cuff straps, and a waist belt with a buckle tied loosely at the back so the front stays OPEN. Coat length reaches only to mid-thigh. Worn open at the front so the shirt, tie, and the bottom edge of the belly patch are visible between the coat fronts. Sleeves end above the paws; the paws stay fully visible.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby below the coat. The tail stays visible beside the coat.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet.

## Camera
Front view, eye level, full body from ear tips to feet, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured markings are integrated surface colour with clean edges. Paw pads, nose, the two muzzle bumps, and whisker rods are raised relief.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays a broad oval clearly wider than tall, fills the top half of the figure, and stays wider than the torso.
3. The brown wave marking stays on MONGSIL's own left ear and upper head (screen right in front view), with the whole outer ear brown and the wave contour intact and not mirrored.
4. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
4-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
5. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.22 of the head's maximum width long.
5-1. The eyes stay SMALL and close-set: each about 0.037 of the head's maximum width, centres about 0.157 of that width apart. Large or wide-set eyes are BANGSIL's face.
6. The closed mouth has no drawn mouth line: only the nose and the vertical groove between the two raised muzzle bumps. No tooth or fang appears anywhere.
7. Colours stay literal: brown #B79571, inner ears, blush and belly patch #FFCDB4, features #000000. #FFCBD1 never appears.
8. The body stays chubby and round; arms and legs stay as short as the reference in every pose, and raised arms never press against the face.
9. Brown appears only on the ear and head wave marking, the heart on the inner tail-side upper arm (only when that inner edge is visible), and the tail. No other spots anywhere on the body.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The coat is open at the front. The shirt covers most of the torso and the belly patch, but the bottom edge of the round belly patch stays visible below the shirt hem. The coat has exactly four buttons, two per side.
11. The deerstalker cap sits between the ears; both ears and the brown head wave marking stay visible.
12. The magnifying glass is the silver-rim, black-handle glass from the reference; its lens sits beside the face and does not cover either eye; the paw holds the black handle.
13. Smooth matte vinyl surface everywhere, on the character and the clothes — no felt texture.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated MONGSIL, BANGSIL, all-white cat with no brown, realistic cat,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, flat face without muzzle bumps, drawn mouth line, W-shaped mouth,
large eyes, wide-set eyes, oversized eyes,
brown whiskers, warm brown nose, reddish whiskers,
smile curve under the muzzle, teeth, fangs,
mirrored markings, brown marking on the wrong ear, missing ear wave marking, simplified round brown patch,
cloud-shaped arm marking, dot arm marking, arm marking on the outer arm or forearm,
extra brown spots on the body, calico patches,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
#FFCBD1, pink inner ears,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
white tail, squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, hat covering the ear marking, closed coat covering the belly patch, short cropped shirt, belly patch fully hidden, six buttons, three buttons per side, long coat, trousers, shoes, waistcoat, vest,
lens covering the eye, magnifying glass floating, brown wooden magnifying glass, gold rim, human child, human face
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 머리 형태 & 크기 | 통과 |
| 귀 & 갈색 웨이브 | 통과 |
| 배 패치 | 통과 (사용자 승인 범위). 셔츠 아래로 반달 모양 아래 끝만 보임 |
| 수염 & 입 & 이빨 | 통과 |
| 얼굴 실측 | 통과. 눈폭 약 0.035 HW, 간격 약 0.153 HW |
| HEX & 섞임 | 통과 |
| **팔 하트** | **실패 (락 9-11).** 소매가 위팔을 덮자 하트가 소매 바로 아래 앞발(손목)로 내려와 반쯤 잘린 갈색 조각으로 나옴. 위치 이동 & 앞팔 배치 둘 다 금지 항목. 수정 방향: Figma에서 갈색 조각을 흰색으로 지우거나, 재생성 시 "the arm heart is hidden under the coat sleeve; the paw below the cuff is plain white with no brown" 추가 |
| 팔 길이 & 얼굴 틈 | 통과 |
| 발끝 세 마디 | 통과. 두 뒷발 3마디 & 홈 2개. 내린 앞발도 3마디 |
| 꼬리 | 주의. 1·2차와 같은 수준 |
| 매끈 재질 | 통과 |
| 의상 | 통과. 코트 단추 4개(양쪽 2개), 셔츠 길게, 넥타이 & 사냥모자 유지. 단추 색이 짙은 갈색보다 검정에 가까움 |
| 돋보기 | 통과 |

## 학습 메모 (1회차, 반영 전)

- 소매가 꼬리쪽 위팔을 덮으면 하트가 노출 부위(손목 & 앞발)로 밀려 내려오는 경향. Subject의 "shown whenever that inner edge faces the camera ... omitted only when the edge is turned away or covered" 문장만으로는 못 막음. 같은 실패가 한 번 더 확인되면 scene-blocks Wardrobe 쪽에 소매 문장을 넣는 걸 제안.

## 3차 후처리 (사용자 선택: 지우기)

- 손목 갈색 조각을 재생성 없이 픽셀 리터치로 지웠다 (Figma 대신 로컬 PIL). 조각 양옆 깨끗한 앞발 열(x 637 & 669)의 소매 그림자 → 흰 앞발 그라데이션을 보간해 덮고 가장자리만 살짝 블러.
- 결과: 소매 아래 앞발 전부 흰색, 앞발 세 마디 그대로. 팔 하트는 소매 속에 가려진 상태로 처리 → 9-11 해소.
- 파일: 로컬 `step1_rev3_fix.png` (스크래치패드, 저장소에는 넣지 않음).

---

# STEP 2 — 고양이 정수기 탐색

- 요청(한국어): 펫프 아이콘 중 고양이 정수기를 불러와서, 탐정 몽실이가 정수기를 훑어보고 탐색하는 모습 (사용자가 펫프 아이콘을 직접 호출)
- 상태: 승인 (2026-11-19 사용자 "승인, 다음 단계로" — 16:9 확장본 기준)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 3:4
- Element: 몽실_3D_매끈 (d76af9ed-b1e7-4ba9-be0e-262a70fbde19), 급수기_고양이 (507822ce-bf38-418a-a87d-ed2b2174035f, petf `Water_Fountain`)
- medias: STEP 1 승인본(손목 리터치) media 23ec1735-4d38-4612-bbae-aae305b28033, `characters/mongsil/references/3d_smooth/Left_3Q.png` media a9baf7ca-820f-4718-bfed-fce5cff4bfb2
- 배경: 누끼용 단색 #E4DFE3 (STEP 3에서 배경 합성 예정)
- job: 306cc784-1f83-4c21-a367-c0f5923963f5
- 크레딧: 사용 0.5 / 남은 988

## 결정 메모

- 45도 레퍼런스(Left_3Q)는 몸이 화면 왼쪽을 향하고 갈색 귀 쪽이 카메라에 가까운 면이다. 그래서 정수기를 화면 왼쪽에 두고, 돋보기 든 오른팔이 정수기 쪽을 향하게 했다.
- 정수기 Element는 정면 1장만 주입되지만 정면에 가까운 각도라 4View는 첨부하지 않았다.
- 소매 아래 하트 이동(STEP 1 3차)을 막으려고 "the arm heart is hidden under the coat sleeve; the paws below the sleeve cuffs are plain white" 문장과 Negative를 넣었다 → 이번엔 재발 없음.

## 최종 프롬프트

```
<<<d76af9ed-b1e7-4ba9-be0e-262a70fbde19>>> <<<507822ce-bf38-418a-a87d-ed2b2174035f>>> # MONGSIL detective inspects the cat water fountain — STEP 2

Attachments, in order: (1) the approved STEP 1 image of this exact MONGSIL in the detective outfit — the costume, magnifying glass, face and body must match it; (2) MONGSIL's three-quarter reference, for how the head, face, markings and body look when turned.
The water fountain is exactly <<<507822ce-bf38-418a-a87d-ed2b2174035f>>>.

## Subject
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown whenever that inner edge faces the camera in any pose including walking, running, and sitting; omitted only when the edge is turned away or covered.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: focused, curious investigating look, closed mouth.

## Orientation
- Body faces: three-quarter toward screen left, toward the water fountain
- Head faces: the same direction as the body, tilted slightly down toward the fountain
- Eyes look at: the top of the water fountain
The head turns on the body naturally with no visible neck. The face, ears, and all markings rotate with the head exactly as in the three-quarter reference; the brown ear and brown head wave stay on MONGSIL's own left side (the side nearer the camera, toward screen right), exactly as in the three-quarter reference and never mirror.

## Pose & Paws
MONGSIL stands on the floor next to the fountain and leans its whole torso forward from the hip toward the fountain, closely investigating it like a detective. Its right paw (screen left, the arm on the fountain side) holds the magnifying glass by its black handle and points the lens toward the fountain's clear dome, held out in front of the body at the height of the fountain top, a little ahead of the face — the lens is between MONGSIL and the fountain and does NOT cover either eye. The arm stays as short as the reference; the reach comes from leaning the body forward and standing close, not from a longer arm. Its left paw (screen right, nearer the camera) is lifted slightly and rests against its own chest/belly, curious. Both feet stay on the floor. The brown tail stays visible at screen right behind the hip.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Water fountain: the prop is exactly <<<507822ce-bf38-418a-a87d-ed2b2174035f>>>: same shape, silhouette, proportions, parts, and every engraved / embossed mark, motif, and symbol — a round two-tier pet water fountain with a hot-pink lower base, a translucent pale-pink upper ring holding clear blue water, a pink centre column under a clear transparent dome spout with thin streams of water falling into the bowl, and one embossed paw-print emblem on the front of the pink base. Keep its colours and glossy plastic / clear acrylic material as in the reference.
It stands on the floor at screen left, its paw emblem facing the camera. Size: the fountain is about as tall as MONGSIL's torso and about as wide as MONGSIL's head.
Magnifying glass: the same one as in the STEP 1 image — polished silver chrome round rim, clear glass lens, silver collar, glossy black handle.

## Wardrobe
Exactly the outfit in the STEP 1 image: houndstooth deerstalker cap with a brown ribbon bow sitting between the ears (both ears and the brown head wave visible), white shirt with pointed collar covering most of the torso, navy necktie, camel trench coat worn open with notched lapels, epaulettes, pocket flaps, cuff straps and exactly four dark buttons (two per side). Only the bottom edge of the round belly patch peeks out below the shirt hem.
The arm heart is hidden under the coat sleeve; the paws below the sleeve cuffs are plain white with no brown on them.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with soft contact shadows under MONGSIL's feet and under the fountain on the same floor. Nothing else in the scene.

## Camera
Slightly elevated eye-level three-quarter view, full body of MONGSIL and the whole fountain in frame, MONGSIL at screen right and the fountain at screen left, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look on the character. Soft even studio lighting, gentle contact shadow. Coloured markings are integrated surface colour with clean edges. Paw pads, nose, the two muzzle bumps, and whisker rods are raised relief. Only the fountain and the magnifying glass are glossy.

## Critical conditions (must all hold)
1. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
2. The head stays a broad oval clearly wider than tall, fills the top half of the figure, and stays wider than the torso.
3. The brown wave marking stays on MONGSIL's own left ear and upper head (screen right in front view), with the whole outer ear brown and the wave contour intact and not mirrored.
4. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
4-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
5. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.22 of the head's maximum width long.
5-1. The eyes stay SMALL and close-set: each about 0.037 of the head's maximum width, centres about 0.157 of that width apart. Large or wide-set eyes are BANGSIL's face.
6. The closed mouth has no drawn mouth line: only the nose and the vertical groove between the two raised muzzle bumps. No tooth or fang appears anywhere.
7. Colours stay literal: brown #B79571, inner ears, blush and belly patch #FFCDB4, features #000000. #FFCBD1 never appears.
8. The body stays chubby and round; arms and legs stay as short as the reference in every pose, and raised arms never press against the face.
9. Brown appears only on the ear and head wave marking, the heart on the inner tail-side upper arm (only when that inner edge is visible), and the tail. No other spots anywhere on the body.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The outfit matches the STEP 1 image exactly: four coat buttons, long white shirt, navy tie, deerstalker between the ears; only the bottom edge of the belly patch shows.
11. The arm heart is hidden under the sleeve; no brown appears on any paw.
12. The magnifying glass is held by the black handle and points at the fountain; the lens does not cover either eye.
13. DEPTH: the fountain stands on the floor beside MONGSIL at screen left, slightly in front of it; MONGSIL does not stand on, sit on, or touch the water. Both share one floor and one light.
14. The fountain keeps exactly the reference's shape, colours, parts and embossed paw emblem.
15. Smooth matte vinyl surface on the character and clothes — no felt texture.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated MONGSIL, BANGSIL, all-white cat with no brown, realistic cat,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, flat face without muzzle bumps, drawn mouth line, W-shaped mouth,
large eyes, wide-set eyes, oversized eyes,
brown whiskers, warm brown nose, reddish whiskers,
smile curve under the muzzle, teeth, fangs,
mirrored markings, brown marking on the wrong ear, missing ear wave marking, simplified round brown patch,
cloud-shaped arm marking, dot arm marking, arm marking on the outer arm or forearm,
extra brown spots on the body, calico patches,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
#FFCBD1, pink inner ears,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
white tail, squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, hat covering the ear marking, closed coat covering the belly patch, short cropped shirt, belly patch fully hidden, six buttons, three buttons per side, long coat, trousers, shoes, waistcoat, vest,
lens covering the eye, magnifying glass floating, brown wooden magnifying glass, gold rim, human child, human face,
brown patch on the paw, brown mark below the sleeve cuff, MONGSIL standing on the fountain, MONGSIL inside the fountain, paw dipped in the water, fountain recoloured, fountain shape changed, missing paw emboss on the fountain, extra fountains, text on the fountain, black background
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 세모 옆얼굴 | 통과. 3/4에서 아래 얼굴 넓고 둥글다 |
| 머리 형태 & 크기 | 통과 |
| 귀 & 갈색 웨이브 | 통과. 화면 오른쪽 귀 갈색, 웨이브가 모자 아래로 이어짐, 미러 없음 |
| 배 패치 | 통과 (STEP 1에서 사용자 승인한 범위). 셔츠 아래로 아래 끝만 보임 |
| 수염 & 입 & 이빨 | 통과 |
| 눈 | 통과. 작고 가까움 (3/4라 수치 실측은 생략) |
| HEX & 섞임 | 통과 |
| 팔 하트 | 통과. 소매 속에 가려짐, 앞발에 갈색 없음 |
| 팔 길이 & 얼굴 틈 | 통과. 돋보기 든 팔과 얼굴 사이 배경 보임 |
| 발끝 세 마디 | 통과. 두 뒷발 3마디 & 홈 2개, 가슴 앞 앞발도 마디 보임 |
| 꼬리 | 주의. 하나의 초승달 & 위 덩이 최대 & 덩이 크기 다름. 홈 깊이 대략 위 13% & 아래 9%로 기준보다 깊지만 15% 미만 |
| 정수기 | 통과. 핫핑크 하단 & 반투명 상단 링 & 물 & 투명 돔 & 핑크 기둥 & 앞면 발바닥 엠보 모두 에셋과 일치 |
| 의상 | 통과. 단추 4개, 긴 셔츠, 넥타이, 사냥모자 귀 사이 |
| 연출 | 주의. 상체 기울기가 약하고 시선이 정수기보다 카메라 쪽에 가깝게 읽힘 |

## STEP 2 후처리 — 영상용 16:9 (재생성 없음)

- 요청: 영상용 16:9, 몽실이+정수기 묶음 기준 좌우 여백 동일 (사용자 선택: 묶음 가운데, 재생성 X)
- 방법: 원본(880×1168) 양옆으로 캔버스를 넓혀 2076×1168을 만들고, 1920×1080으로 축소. 확장 영역은 행마다 원본 가장자리 색에서 깨끗한 배경색으로 80px에 걸쳐 섞어 채움 (왼쪽 가장자리의 정수기 그림자 이음새 방지)
- 결과: 1920×1080, 묶음 좌우 여백 각 572px (2076 단계 618px & 618px). 위 여백 약 197px, 아래 약 128px
- 몽실이 단독 중심은 화면 중앙보다 오른쪽 (사용자 확인 후 진행)
- 파일: 로컬 `step2_16x9.png` (스크래치패드, 저장소에는 넣지 않음)

---

# 모션 — 정수기 살펴보기 영상

- 요청(한국어): STEP 2 16:9 이미지로 영상 생성. 720p, 클링, 표정 변화 자연스럽게, 정수기를 살펴보는 영상 (배경색은 그대로 — 사용자 선택)
- 상태: 실패 (눈썹 — 사용자 재생성 요청)
- 모델: Kling 3.0 Turbo (`kling3_0_turbo`) & 720p & 5초 & 16:9 — 클링 중 720p 지원 모델 견적(3.0 Turbo 7.5 / 4.0 11.25 / 4.0 Flash 15) 중 최저가
- 시작 프레임: STEP 2 16:9 확장본 media 1d2e9cdf-e291-41ba-b161-84e73b64bbf9
- job: 05b3a30d-6b85-45af-abfc-e48c86b3a86f
- 크레딧: 사용 7.5 / 남은 980.5
- 결과: 1280×720, 24fps, 5.04초

## 프롬프트

```
Animate this exact image. A soft smooth matte vinyl 3D cat mascot (MONGSIL) in a detective outfit curiously inspects the pink pet water fountain beside it.

Action (5 seconds, gentle and cute): MONGSIL leans a little closer to the fountain and slowly moves the silver magnifying glass across the clear dome, as if scanning for clues. It tilts its big head slightly from side to side while looking through the lens at the fountain, then gives a small satisfied nod. Its natural facial expression changes softly: a focused look, a slow blink, the eyes narrowing a little in concentration, then brightening with a pleased, curious look. The ears twitch once. The brown tail sways gently. The free paw stays near its chest. Thin streams of water keep flowing from the clear dome into the bowl and the water surface ripples softly.

Keep identical for the whole clip: the character design, the broad round head, small black oval eyes, raised muzzle bumps, two whiskers per side, brown ear and brown head wave on the same side, houndstooth deerstalker cap between the ears, white shirt, navy tie, camel trench coat with four buttons, the silver black-handled magnifying glass, the fountain's shape, colours and paw emblem, and the plain light grey background. The mouth stays CLOSED the entire clip: no open mouth, no talking, no teeth. Paws keep their three rounded toe lobes. Smooth matte material, no fur.

Camera: completely static locked-off camera, no zoom, no pan; the framing stays exactly as in the image.

Avoid: open mouth, teeth, fangs, talking, eyes growing larger, character redesign, extra characters, extra objects, text, background change, camera movement, flicker, morphing, long arms, fur.
```

## 검증 (ffmpeg로 0.25초 간격 20프레임 확인)

| 항목 | 결과 |
|---|---|
| 프레이밍 | 통과. 카메라 고정, 묶음 좌우 여백 382~384px & 379~391px (꼬리 흔들림만큼 변동) |
| 입 & 이빨 | 통과. 전 프레임 입 닫힘, 이빨 없음 |
| 머리 & 갈색 웨이브 | 통과. 화면 오른쪽 유지, 미러 없음 |
| 표정 | 집중 → 찡그림 → 깜빡임 → 마지막 눈웃음(^^)으로 변화 |
| **눈썹** | **실패 (스타일 3번 "no eyebrows").** 찡그리는 구간(약 0.5초, 3.0초, 4.0~4.5초)에 눈 위 짧은 눈썹 선이 생김 |
| 수염 & 눈 크기 | 통과 |
| 의상 & 돋보기 & 정수기 | 통과. 일부 프레임에서 사냥모자 챙 모양이 살짝 변함 |
| 시선 | 주의. 정수기보다 카메라 쪽을 보는 프레임이 많음 |
| 발 & 꼬리 | 통과 수준. 꼬리 하나의 덩어리 유지 |

## 학습 메모 (1회차)

- 영상에서 "eyes narrowing in concentration"을 지시하면 눈썹 선이 생긴다. 다음엔 표정을 눈 깜빡임 & 고개 기울기 & 눈웃음으로만 지시하고 Avoid에 `eyebrows, brow lines, frowning` 추가.

## 모션 2차 — 눈썹 막고 재생성

- 요청(한국어): 눈썹 막고 재생성
- 1차 상태: 실패 (눈썹, 사용자 재생성 요청)
- 2차 상태: 실패 (입 열림 — 사용자가 새 프롬프트로 재생성 요청)
- 모델: Kling 3.0 Turbo & 720p & 5초 & 16:9, 시작 프레임 동일
- job: 5f8a7a12-48f7-4e4d-95df-be79cefa0b92
- 크레딧: 사용 7.5 / 남은 973
- 프롬프트 변경: 표정을 "깜빡임 & 고개 기울기 & 마지막 눈웃음"으로만 지시, "NO eyebrows ... area above the eyes stays smooth plain white" 문단 추가, 시선을 정수기에 고정, Avoid에 `eyebrows, brow lines, lines above the eyes, frowning, furrowed brow, angry face, squinting, looking at the camera, cap changing shape` 추가

## 모션 2차 검증 (24fps 전 프레임 중 0.25초 간격 20장 + 입 확대 6장)

| 항목 | 결과 |
|---|---|
| 눈썹 | 통과. 찡그린 눈썹 선 사라짐. 눈 감는 프레임의 곡선은 눈 자체 |
| 프레이밍 | 통과. 좌 382~384px, 우 369~395px (꼬리 흔들림만큼) |
| **입** | **주의.** 약 0.6~3.8초 구간에 머즐 아래로 입이 살짝 열리고 분홍 혀가 보임. 이빨 & 송곳니는 없음. 프롬프트의 "mouth CLOSED"를 어김 |
| 표정 | 깜빡임 → 마지막 눈웃음(^^) |
| 시선 | 주의. 여전히 카메라 쪽을 보는 프레임이 많음 |
| 의상 & 정수기 & 갈색 웨이브 | 통과 |

## 학습 메모

- 1차: "eyes narrowing in concentration" → 눈썹 생성. 2차: 눈썹 막자 입이 열림. Kling 3.0 Turbo는 표정 변화를 요청하면 눈썹 또는 입으로 표현하려는 경향. 같은 현상이 다시 나오면 영상 프롬프트 규칙으로 정리 제안.

## 모션 3차 — 사용자 프롬프트 + 소리 끄기

- 요청(한국어): 소리는 꺼줘, 프롬프트는 사용자가 준 "MONGSIL — Curious Water Fountain Inspection" 문서로
- 2차 상태: 실패 (입 열림 — 사용자가 새 프롬프트로 재생성 요청)
- 3차 상태: 실패 (눈썹 + 입 — 사용자가 모델 교체)
- 모델: Kling 3.0 Turbo & 720p & 5초 & 16:9, 시작 프레임 동일
- job: f0d54775-0482-4152-8e2b-3358b3be2c40
- 크레딧: 사용 7.5 / 남은 965.5
- 소리: Kling 3.0 Turbo에는 소리 끄기 옵션이 없음. 결과에 aac 오디오 트랙이 있어 ffmpeg로 오디오만 제거(`-c:v copy -an`, 영상 재인코딩 없음) → `motion3_mute.mp4`
- 프롬프트 변경: 사용자 원문이 이미지→영상 제한 2500자를 넘어 422 거절됨. 내용은 그대로 두고 제목·줄바꿈만 압축(2356자). Avoid에 락 규칙인 `eyebrows, brow lines`만 추가

## 3차 프롬프트 (전송본)

```
MONGSIL — Curious Water Fountain Inspection. Animate this exact image for 5 seconds.
A soft smooth matte vinyl 3D cat mascot (MONGSIL) in a detective outfit curiously explores the pink pet water fountain.

ACTION: MONGSIL behaves like a genuinely curious little detective discovering an unfamiliar object. It leans slightly closer and carefully examines the fountain through its silver magnifying glass; its gaze naturally follows the water flowing inside the clear dome. Suddenly something catches its attention: it pauses briefly, tilts its big head with a cute, puzzled "Huh? What's this?" expression, and looks more closely through the magnifying glass. It gently shifts the magnifying glass to inspect another part of the fountain, showing renewed curiosity. Movements are spontaneous and slightly irregular, with natural pauses between observations — curious and thoughtful, not a rehearsed animation.

EYES & EXPRESSION (very important): keep the original small black oval eyes. Express curiosity mainly through gaze direction, head tilts and brief pauses. Eyes stay naturally open most of the clip; at most ONE subtle spontaneous blink in 5 seconds; no rhythmic or repeated blinking; no exaggerated eye narrowing or enlargement. The mouth stays CLOSED throughout; no talking, teeth or exaggerated expressions.

SECONDARY MOTION: one subtle ear twitch; brown tail sways gently; free paw stays near the chest; small natural body adjustments; thin streams of water flow continuously into the bowl with soft natural ripples.

CHARACTER LOCK — preserve exactly: broad round head and body proportions; small black oval eyes; raised muzzle bumps; two whiskers per side; brown ear and brown head wave on the original side; houndstooth deerstalker cap between the ears; white shirt and navy tie; camel trench coat with four buttons; silver magnifying glass with black handle; original pink fountain shape, colours and paw emblem; three rounded toe lobes on each paw; smooth matte vinyl, no fur; plain light grey background.

CAMERA: completely static locked-off camera; no zoom, pan, tilt or framing change.

AVOID: repetitive blinking, mechanical scanning, robotic timing, exaggerated reactions, open mouth, talking, teeth, eye enlargement, eyebrows, brow lines, character redesign, extra objects, long arms, fur, flicker, morphing, camera movement.
```

## 3차 검증 (0.25초 간격 20프레임)

| 항목 | 결과 |
|---|---|
| 소리 | 통과. 오디오 트랙 제거 확인 (video 스트림만 남음) |
| 프레이밍 | 통과. 좌 382~384px, 우 365~393px (꼬리 흔들림) |
| 시선 | 개선. 후반에 고개를 정수기 쪽으로 숙이고 돋보기를 따라봄 |
| **눈썹** | **실패.** 약 2.0초부터 끝까지 "Huh?" 갸웃 표정에서 눈썹 선이 뚜렷하게 생김 |
| **입** | **실패(지시 위반).** 약 0.5초부터 입이 벌어져 혀가 보임. 이빨은 없음 |
| 눈 | 한쪽 눈 찡그림(윙크) 프레임 있음 |
| 의상 & 정수기 & 갈색 웨이브 | 통과 |

## 학습 메모 (3회 누적)

- Kling 3.0 Turbo에서 표정 연기("concentration", "puzzled Huh?")를 요구하면 눈썹 & 벌린 입으로 표현한다. 3회 연속 확인 (1차 눈썹, 2차 입, 3차 눈썹+입). 표정 단어를 빼고 고개·시선·돋보기 동작만 지시하는 쪽으로 규칙화 후보 → templates/scene.md 모션 항목 반영 제안 대상.

## 모션 4차 — Seedance 2.0 Mini + 사용자 기존 성공 프롬프트

- 요청(한국어): 씨댄스 2.0 미니로, 예전에 잘 나왔던 프롬프트("The still image comes to life ... over four seconds") 사용, 소리 끄기
- 3차 상태: 실패 (눈썹 + 입 — 사용자가 모델 교체)
- 4차 상태: 미확인
- 모델: Seedance 2.0 Mini (`seedance_2_0_mini`) & 720p & 4초 & 16:9 & `generate_audio: false`
- 시작 프레임: STEP 2 16:9 확장본 media 1d2e9cdf-e291-41ba-b161-84e73b64bbf9
- job: 80af03df-bccc-4212-93aa-47252fa18585
- 크레딧: 견적 4 / 남은 965.5 → 961.5
- 결과: 1280×720, 24fps, 4.04초, 오디오 스트림 없음

## 4차 프롬프트 조정 (원문은 다른 장면 기준이라 지금 이미지와 다른 곳만 바꿈)

| 원문 | 바꾼 것 | 이유 |
|---|---|---|
| white flocked-felt cat mascot in round glasses | white smooth matte vinyl cat mascot in a detective outfit (cap & shirt & tie & trench) | 지금 이미지는 매끈 재질 & 안경 없음 |
| 안경을 앞발로 올리는 동작 & glasses stay clear | 자유로운 앞발로 가슴을 한 번 토닥 | 안경이 없음. 짧은 팔로 모자까지 닿게 하면 팔이 늘어날 위험 (락 1번) |
| its eyes opening wider | 삭제 (impressed, delighted look만 유지) | 눈 크기 고정 (락 2번 얼굴 실측) |
| small satisfied smile | small satisfied look, mouth staying closed | 기본 입은 닫힘 (락 2번 Mouth) |
| soft matte felt texture | smooth soft matte vinyl surface | 매끈 재질 |
| almost-round head slightly wider than tall | broad round head clearly wider than tall | 락 1번 1.2 : 1 |
| peach belly patch | 삭제 | 셔츠에 가려 아래 끝만 보임 |
| small brown half-cloud marking on the outer edge of the upper arm | arm markings hidden under the sleeves, no brown on the paws | 옛 규칙(2026-11-09 폐기). 지금은 위팔 안쪽 하트이고 소매에 가려짐 |
| cloud-shaped brown tail | one continuous brown crescent tail | 락 3-1번 |
| pale warm-white background | pale light grey | 지금 배경색 |
| (없음) | no eyebrows, mouth closed, no teeth, four coat buttons | 1~3차 실패 항목 |

## 4차 검증 (0.25초 간격 16프레임 + 입 확대)

| 항목 | 결과 |
|---|---|
| 소리 | 통과. 오디오 스트림 없음 |
| 동작 | 통과. 몸을 숙여 돋보기를 정수기 쪽으로 대고 살핌 → 바로 서서 끄덕 → 눈웃음. 지금까지 중 "살펴보는" 연출이 가장 좋음 |
| 눈썹 | 통과. 눈썹 선 없음 |
| 입 | 주의. 약 3.4초 눈웃음 순간 몇 프레임 입이 벌어지고 분홍 혀가 보임. 이빨 없음. 나머지는 닫힘 |
| 눈 | 통과. 돋보기를 눈앞에 대는 구간은 렌즈 너머로 보임 |
| 프레이밍 | 주의. 좌 378~382px로 고정, 우 345~389px. 끝부분 몸을 세우며 오른쪽 여백이 약 27px 좁아짐 |
| 의상 & 정수기 & 갈색 웨이브 & 꼬리 | 통과 |
