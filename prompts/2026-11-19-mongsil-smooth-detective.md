# 몽실 매끈 탐정 — STEP 1 의상 & 소품

- 날짜: 2026-11-19
- 캐릭터: 몽실
- 요청(한국어): 몽실 3D, 매끈 재질로. 탐정옷 같은 걸 입히고 손에는 돋보기 (사용자 첨부 이미지: 사람 아이 탐정 일러스트 — 의상 참고용, 생성에는 첨부 안 함)
- 상태: 미확인
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
- 상태: 미확인
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
