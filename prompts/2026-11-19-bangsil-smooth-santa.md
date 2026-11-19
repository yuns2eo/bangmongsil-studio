# 방실 매끈 산타 — STEP 1 의상 & 소품

- 날짜: 2026-11-19
- 캐릭터: 방실
- 요청(한국어): 산타 방실이. 바지는 안 입혀도 됨, 손으로 선물보따리를 들고, 산타모자 & 산타의상, 흰 콧수염이 귀엽게 (사람 산타 일러스트 첨부 — 참고용, 생성에는 첨부 안 함). 재질은 매끈 (사용자 선택)
- 상태: 실패 (사용자 수정 요청 — 2차로 대체)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 3:4 (전신 의상 확인)
- Element: 방실_3D_매끈 (cdfcf687-3667-4ee4-b795-33b41009c558)
- 첨부 레퍼런스: 없음 (정면)
- job: 969a6dd5-e71f-4a5c-acd9-dbc714ce75b5
- 크레딧: 사용 0.5 (견적) / 남은 961

## 결정 메모

- 선물보따리는 펫프 선물상자가 아니라 천 자루라 소품 Element 없이 `## Prop` 문장으로 처리. 펫프 아이콘은 호출되지 않음.
- 산타 재킷은 배 패치 위에서 끝나게 짧게 (락 4번). 바지 & 부츠 없음.
- 콧수염은 W 입선을 가리지 않도록 코 바로 아래 작게, 수염(whisker)도 가리지 않게 지시 (락 2번 & 9-3번).
- 매끈 재질이라 Negative 재질 줄을 펠트 방지 표현으로 교체 (몽실 탐정과 같은 처리).

## 최종 프롬프트

```
<<<cdfcf687-3667-4ee4-b795-33b41009c558>>> # BANGSIL Santa — STEP 1 wardrobe & prop

## Subject
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.054 of the head's maximum width, and the gap between their centres is about 0.206 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded dark triangle nose sitting directly on the smooth cheek surface, and below it a drawn wide W-shaped smile line in the same dark colour as the whiskers.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, whiskers, nose and mouth line #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail.
Expression: cheerful, warm happy look with the W smile, mouth closed.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all features rotate with the head and never mirror.

## Pose & Paws
BANGSIL stands upright. Its right arm (screen left) is raised only to shoulder height, still short, and its paw holds the gathered, tied neck of a big gift sack slung over that shoulder, so the sack hangs behind the screen-left shoulder. Its left arm (screen right) rests at its side.
The paw grips the sack neck; the sack touches the paw and the shoulder.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette; the outline shows two separate shapes there, not one.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Gift sack: a big soft round red cloth sack, full of presents, its top gathered and tied with a white cord into a short neck. Size: the sack body is about as wide as the character's head. It hangs over the screen-left shoulder and stays on the screen-left side, never covering the face, the belly patch, or the tail. Nothing is printed on it.

## Wardrobe
A cute Santa outfit sized to the chubby mascot body, no trousers:
- Santa hat: red with a soft rounded white trim band and a white pom-pom on its drooping tip, sitting on top of the head BETWEEN the two ears; both low broad ears stay fully visible on either side.
- Santa jacket: a short red jacket with soft white trim along the collar, the front opening, the cuffs and the hem, a black belt with a gold buckle, ending ABOVE the round belly patch so the belly patch stays clearly visible below the jacket hem. Sleeves end above the paws. No trousers, no boots — the short white legs and paws are bare.
- Mustache: a small, cute, fluffy bright-white Santa mustache that curls out to both sides just under the nose. It is small: it stays inside the flat face, does not cover the whiskers, and the black W-shaped smile line stays clearly visible directly below it. No long beard.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby. The tail stays visible.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet. The tail silhouette stays clearly readable against the background.

## Camera
Front view, eye level, full body from ear tips to feet, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured areas are integrated surface colour with clean edges. Paw pads, nose, and whisker rods are raised relief. The white trims and mustache are soft rounded smooth shapes, not shaggy fur.

## Critical conditions (must all hold)
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn.
4. Both ears are low broad triangles with rounded tips, each clearly wider at the base than tall, matching each other, body-coloured outside with #FFCBD1 inside. Neither ear is a tall upright spike and neither tip comes to a point.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.26 of the head's maximum width long.
8-1. The eyes stay LARGE and wide-set: each about 0.054 of the head's maximum width, centres about 0.206 of that width apart. Small, close-set eyes are MONGSIL's face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The Santa hat sits between the ears; both ears stay fully visible.
11. The jacket ends above the belly patch; the round #FFCBD1 belly patch stays clearly visible. No trousers.
12. The white mustache is small and sits under the nose; the W smile line stays visible below it, and the two whiskers per side stay visible on the cheeks. No long beard.
13. The raised paw holds the sack neck at shoulder height with a visible gap from the cheek; the arm stays short.
14. Smooth matte vinyl surface everywhere — no felt texture.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated BANGSIL, MONGSIL, calico cat, brown patched cat, realistic cat,
brown marking, brown ear, brown head patch, brown tail, heart on the arm, any brown on the body,
#FFCDB4, #B79571, peach inner ears,
raised muzzle bumps, puffy white muzzle, missing mouth line, no smile line,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, folded ears, mismatched ears, teeth, fangs,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
small eyes, close-set eyes, tiny eyes,
neutral gray whiskers, gray nose,
squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
fox ears, tall upright ears, pointed ear tips, sharp ear tips, narrow ears, ears taller than their base width,
tail invisible against the background,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, long beard, full beard, beard covering the mouth, mustache covering the mouth line, mustache covering the whiskers, beard covering the belly,
jacket covering the belly patch, trousers, pants, boots, gloves, human hands,
gift box, petf gift box, sack covering the face, sack covering the tail, floating sack, text on the sack, human face, human body
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 갈색 | 통과. 갈색 없음 |
| 납작한 얼굴 & 머즐 | **주의.** 콧수염이 코 아래 흰 볼록 두 덩이로 나와, 전체 크기에서는 몽실이 머즐 볼록처럼 읽힐 수 있음 (섞임 신호 2번과 비슷). 확대하면 끝이 말린 콧수염 모양 |
| W 입선 | 통과. 콧수염 아래로 W 입선이 또렷함 |
| 귀 | 통과. 낮고 넓은 둥근 귀, 모자가 귀 사이에 앉음 |
| 얼굴 실측 | 통과. 눈폭 0.055 HW (기준 0.054), 간격 0.194 HW (기준 0.206) |
| 수염 | 통과. 한쪽 2가닥, 갈색 톤은 락 11-1 기지 사항 |
| 배 패치 | 통과. 재킷 아래로 아래쪽 반원 보임 |
| **든 팔 & 얼굴 틈** | **실패 (락 12-1).** 보따리를 쥔 앞발 윗부분이 아래 볼에 붙어 사이에 배경이 안 보임 (뒤는 보따리) |
| 발끝 세 마디 | 통과. 두 뒷발 3마디, 내린 앞발 3마디 |
| 꼬리 | 통과. 흰 초승달, 배경과 구분됨 |
| 섞임 | #FFCDB4 & 갈색 없음, 눈 크고 넓음 → 섞임 없음 (콧수염 주의만) |
| 매끈 재질 | 통과 |

---

# 2차 — 큰 산타 수염 & 1:1 (1차 결과 1회 편집)

- 요청(한국어): 수염을 완전히 더 크게. 방실이 얼굴이 흰색이라 수염이 잘 안 보임. 사진은 1:1로
- 1차 상태: 실패 (사용자 수정 요청)
- 2차 상태: 실패 (사용자 수정 요청 — 3차로 대체)
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 1:1 (1024×1024)
- Element: 방실_3D_매끈 (cdfcf687-3667-4ee4-b795-33b41009c558)
- medias: 1차 job 969a6dd5-e71f-4a5c-acd9-dbc714ce75b5 (편집 기준, **1회 편집 사용함**)
- job: 58b65c1c-d48e-4ead-9fb2-e9294bcc212b
- 크레딧: 사용 0.5 / 남은 960.5
- 함께 고친 것: 1차 실패(앞발이 볼에 닿음)를 같이 고치도록 "보따리 쥔 앞발을 조금 내려 볼과 틈" 지시 추가
- 수염 대비: 순백 + 회색 음영 + 외곽 그림자로 크림색 얼굴과 구분되게 지시

## 최종 프롬프트

```
<<<cdfcf687-3667-4ee4-b795-33b41009c558>>> # BANGSIL Santa — STEP 1 rev 2 (edit of the attached image), square 1:1

The attached image is the previous result of this exact BANGSIL in the Santa outfit.
Keep EVERYTHING identical to it — the face, eyes, nose, W smile line, whiskers, ears, belly patch, tail, paws, body proportions, Santa hat, red jacket with white trim and belt, red gift sack, smooth matte material, lighting and background colour — except these changes:
1. Replace the small mustache with a BIG, very visible fluffy Santa beard and mustache: a large curled mustache spreading wide under the nose, and a full rounded beard that frames the lower face from cheek to cheek and hangs down over the upper chest, in bright pure white with soft grey shading in its curls and a soft shadow along its outline so it stands out clearly against BANGSIL's cream-white face. The black W-shaped smile line stays visible in a small gap between the mustache and the beard. The two whiskers per side stay visible, growing from the cheeks over the beard.
2. Lower the raised paw holding the sack neck slightly, so a clear sliver of background shows between the paw and the cheek / beard.
3. Square 1:1 framing: the whole figure, sack and tail centred with even margins, nothing cropped.

## Subject
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.054 of the head's maximum width, and the gap between their centres is about 0.206 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded dark triangle nose sitting directly on the smooth cheek surface, and below it a drawn wide W-shaped smile line in the same dark colour as the whiskers.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, whiskers, nose and mouth line #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail.
Expression: cheerful, warm happy look with the W smile, mouth closed.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all features rotate with the head and never mirror.

## Pose & Paws
BANGSIL stands upright. Its right arm (screen left) is raised only to shoulder height, still short, and its paw holds the gathered, tied neck of a big gift sack slung over that shoulder, so the sack hangs behind the screen-left shoulder. Its left arm (screen right) rests at its side.
The paw grips the sack neck; the sack touches the paw and the shoulder.
A continuous sliver of background stays visible between the raised paw and the cheek all the way down, even where it is narrow. The raised arm and the head never merge into one silhouette; the outline shows two separate shapes there, not one.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Gift sack: a big soft round red cloth sack, full of presents, its top gathered and tied with a white cord into a short neck. Size: the sack body is about as wide as the character's head. It hangs over the screen-left shoulder and stays on the screen-left side, never covering the face, the belly patch, or the tail. Nothing is printed on it.

## Wardrobe
A cute Santa outfit sized to the chubby mascot body, no trousers:
- Santa hat: red with a soft rounded white trim band and a white pom-pom on its drooping tip, sitting on top of the head BETWEEN the two ears; both low broad ears stay fully visible on either side.
- Santa jacket: a short red jacket with soft white trim along the collar, the front opening, the cuffs and the hem, a black belt with a gold buckle, ending ABOVE the round belly patch so the belly patch stays clearly visible below the jacket hem. Sleeves end above the paws. No trousers, no boots — the short white legs and paws are bare.
- Santa beard: a BIG fluffy bright-white Santa mustache and full rounded beard framing the lower face and hanging over the upper chest, with soft grey shading and a soft outline shadow so it reads clearly against the cream face. The black W smile line peeks out between the mustache and the beard; the two whiskers per side stay visible on the cheeks.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby. The tail stays visible.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet. The tail silhouette stays clearly readable against the background.

## Camera
Front view, eye level, square 1:1 frame, full body from hat tip to feet with the sack and tail, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured areas are integrated surface colour with clean edges. Paw pads, nose, and whisker rods are raised relief. The white trims are soft rounded smooth shapes; the beard is soft rounded curls, not shaggy hair strands.

## Critical conditions (must all hold)
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn.
4. Both ears are low broad triangles with rounded tips, each clearly wider at the base than tall, matching each other, body-coloured outside with #FFCBD1 inside. Neither ear is a tall upright spike and neither tip comes to a point.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.26 of the head's maximum width long.
8-1. The eyes stay LARGE and wide-set: each about 0.054 of the head's maximum width, centres about 0.206 of that width apart. Small, close-set eyes are MONGSIL's face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The Santa hat sits between the ears; both ears stay fully visible.
11. The jacket ends above the belly patch; the round #FFCBD1 belly patch stays clearly visible. No trousers.
12. The big white Santa beard and mustache are clearly visible against the face; the W smile line shows between them; two whiskers per side stay visible; the eyes, nose and ears are not covered; the beard does not cover the belly patch.
13. The raised paw holds the sack neck at shoulder height with a visible gap from the cheek; the arm stays short.
14. Smooth matte vinyl surface everywhere — no felt texture.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated BANGSIL, MONGSIL, calico cat, brown patched cat, realistic cat,
brown marking, brown ear, brown head patch, brown tail, heart on the arm, any brown on the body,
#FFCDB4, #B79571, peach inner ears,
raised muzzle bumps, puffy white muzzle, missing mouth line, no smile line,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, folded ears, mismatched ears, teeth, fangs,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
small eyes, close-set eyes, tiny eyes,
neutral gray whiskers, gray nose,
squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
fox ears, tall upright ears, pointed ear tips, sharp ear tips, narrow ears, ears taller than their base width,
tail invisible against the background,
long fur, individual hairs, fabric seams, stitching, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, tiny mustache, beard blending into the face, beard covering the eyes, beard covering the belly patch, mustache hiding the W smile line, beard hiding the whiskers, grey beard,
jacket covering the belly patch, trousers, pants, boots, gloves, human hands,
gift box, petf gift box, sack covering the face, sack covering the tail, floating sack, text on the sack, human face, human body
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 산타 수염 | 통과. 크게 말린 콧수염 + 둥근 턱수염, 회색 음영으로 얼굴과 구분됨 |
| 갈색 & 섞임 | 통과. 갈색 없음, 머즐 볼록 없음 (콧수염이 그 자리) |
| **입** | **실패 의심 (락 9-3 & 9-10).** W 입선 대신 콧수염과 턱수염 사이로 벌어진 어두운 입이 보이고, 입 안에 작은 흰 삼각형이 있어 이빨처럼 보임 |
| 얼굴 실측 | 통과. 눈폭 0.057 HW, 간격 0.192 HW (기준 0.054 & 0.206) |
| 수염(whisker) | 통과. 한쪽 2가닥, 볼에서 수염 위로 |
| 귀 & 모자 | 통과 |
| 배 패치 | 통과. 재킷 아래 반원 |
| **든 팔 & 얼굴 틈** | **실패 (락 12-1).** 앞발이 여전히 턱수염 & 아래 볼에 붙어 배경이 안 보임 |
| 발끝 & 꼬리 | 통과 |
| 매끈 재질 | 통과 |

## 다음 수정 시 주의

- 편집 1회를 썼으므로 다음은 원본 Element로 새로 생성 (`templates/scene.md` 6번)
- 앞발 문제는 "어깨 위로 멘 보따리"를 유지하는 한 반복됨 (1차·2차 2회). 가슴 높이에서 보따리 목을 쥐고 보따리를 옆에 늘어뜨리는 자세로 바꾸는 게 확실
- 큰 턱수염이 입 영역을 덮으면 모델이 입을 벌림. "W smile line, mouth closed, no opening between mustache and beard" 같이 닫힌 입을 더 강하게 지시

---

# 3차 — 트리 안기 & 진짜 같은 수염 (원본 Element로 새로 생성)

- 요청(한국어): 트리를 가슴 안에 안고 있는 자세로 (산타 일러스트 첨부 — 참고용, 생성에는 첨부 안 함), 수염은 실제 수염 같아야 함. 지금은 너무 딱딱한 재질
- 2차 상태: 실패 (사용자 수정 요청)
- 3차 상태: 미확인
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 1:1
- Element: 방실_3D_매끈 (cdfcf687-3667-4ee4-b795-33b41009c558), medias 없음 (2차에서 편집 1회 사용 → 새로 생성)
- job: 5190069c-4cc7-40a3-898a-98c75d314024
- 크레딧: 사용 0.5 / 남은 960
- 변경: 선물보따리 → 화분 트리를 두 앞발로 가슴 높이에서 안기 (앞발 볼 닿음 2회 반복 해소용). 수염만 매끈 재질 예외로 "부드러운 실제 털 수염" 지시. 입은 W 입선 & 닫힘 강하게 지시

## 최종 프롬프트

```
<<<cdfcf687-3667-4ee4-b795-33b41009c558>>> # BANGSIL Santa hugging a small Christmas tree — STEP 1 rev 3, square 1:1

## Subject
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.054 of the head's maximum width, and the gap between their centres is about 0.206 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded dark triangle nose sitting directly on the smooth cheek surface, and below it a drawn wide W-shaped smile line in the same dark colour as the whiskers.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, whiskers, nose and mouth line #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail.
Expression: cheerful, warm happy look with the W smile, mouth closed.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all features rotate with the head and never mirror.

## Pose & Paws
BANGSIL stands upright and hugs a small potted Christmas tree in front of its chest with both short arms: both paws wrap around the small brown pot from the left and right sides, held at chest height, close to the body. The arms stay as short as the reference; the elbows stay at the sides of the body. Both paws stay well below the face and below the beard, never touching the head.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Small Christmas tree: a cute, rounded, tiered green pine tree in a small brown pot, decorated with small red and white round ornaments and a small gold star on top. Size: the tree with its pot is about as tall as the character's torso. It is held slightly toward screen left in front of the chest so the whole face stays visible: the star tip stays below the eyes, beside the beard, never covering the eyes, nose, mouth or beard centre. The pot sits on the paws at chest height, so the round belly patch below the jacket hem stays visible. Nothing is printed on it.

## Wardrobe
A cute Santa outfit sized to the chubby mascot body, no trousers:
- Santa hat: red with a soft rounded white trim band and a white pom-pom on its drooping tip, sitting on top of the head BETWEEN the two ears; both low broad ears stay fully visible on either side.
- Santa jacket: a short red jacket with soft white trim along the collar, the front opening, the cuffs and the hem, a black belt with a gold buckle, ending ABOVE the round belly patch so the belly patch stays clearly visible below the jacket hem. Sleeves end above the paws. No trousers, no boots — the short white legs and paws are bare.
- Santa beard: a BIG, REALISTIC, soft and fluffy white Santa beard and mustache made of real-looking soft hair — fine wavy strands gathered into airy curly locks, light and fluffy, with natural soft grey shadows between the locks and a wispy, slightly irregular outline, like a real plush Santa beard, NOT a hard sculpted or plastic shape. A large curled mustache spreads wide under the nose, and the full rounded beard frames the lower face from cheek to cheek and falls over the upper chest. It reads clearly against BANGSIL's cream face. Between the mustache and the beard, the black W-shaped smile line is visible and the mouth is CLOSED — no opening, no teeth. The two whiskers per side stay visible on the cheeks above the beard.
It sits on top of the character without changing the head shape, ears, or body volume. The legs stay short and stubby. The tail stays visible.

## Environment
Plain solid flat background colour #E4DFE3, seamless, with a soft contact shadow under the feet. The tail silhouette stays clearly readable against the background.

## Camera
Front view, eye level, square 1:1 frame, full body from hat tip to feet with the tree and tail, centred, nothing cropped.

## Style
Smooth, clean, soft matte vinyl / soft-touch clay 3D mascot figure. No felt pile, no embossed grain, no fur, no fuzz, no fibres on the body and clothes. Very soft satin response to light with broad gentle highlights only; no mirror gloss, no wet look. Soft even studio lighting, gentle contact shadow. Coloured areas are integrated surface colour with clean edges. Paw pads, nose, and whisker rods are raised relief. The white trims are soft rounded smooth shapes. Exception: the Santa beard and mustache alone are soft realistic fluffy hair, not smooth vinyl.

## Critical conditions (must all hold)
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn; the mouth is closed with no opening and no teeth.
4. Both ears are low broad triangles with rounded tips, each clearly wider at the base than tall, matching each other, body-coloured outside with #FFCBD1 inside. Neither ear is a tall upright spike and neither tip comes to a point.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face. Each whisker is about 0.26 of the head's maximum width long.
8-1. The eyes stay LARGE and wide-set: each about 0.054 of the head's maximum width, centres about 0.206 of that width apart. Small, close-set eyes are MONGSIL's face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The Santa hat sits between the ears; both ears stay fully visible.
11. The jacket ends above the belly patch; the round #FFCBD1 belly patch stays clearly visible. No trousers.
12. The big white Santa beard and mustache look like real soft fluffy hair, clearly visible against the face; the closed W smile line shows between them; two whiskers per side stay visible; the eyes, nose and ears are not covered.
13. Both paws hold the tree pot at chest height, well below the face and beard; the arms stay short.
15. The tree never covers the eyes, nose or mouth; the belly patch below the jacket stays visible.
14. Smooth matte vinyl surface on the body and clothes — no felt texture; only the beard is fluffy hair.

## Negative
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads,
extra characters, two cats, duplicated BANGSIL, MONGSIL, calico cat, brown patched cat, realistic cat,
brown marking, brown ear, brown head patch, brown tail, heart on the arm, any brown on the body,
#FFCDB4, #B79571, peach inner ears,
raised muzzle bumps, puffy white muzzle, missing mouth line, no smile line,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, folded ears, mismatched ears, teeth, fangs,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
small eyes, close-set eyes, tiny eyes,
neutral gray whiskers, gray nose,
squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
snowman tail, tail as stacked spheres, three separate balls, deep notches in the tail, equal tail lobes,
fox ears, tall upright ears, pointed ear tips, sharp ear tips, narrow ears, ears taller than their base width,
tail invisible against the background,
long fur on the body, hair on the body, fabric seams, stitching, felt texture, flocked pile, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek,
hat covering the ears, tiny mustache, hard plastic beard, sculpted rigid beard, clay beard, smooth vinyl beard, beard blending into the face, beard covering the eyes, mustache hiding the W smile line, open mouth between mustache and beard, beard hiding the whiskers, grey beard,
jacket covering the belly patch, trousers, pants, boots, gloves, human hands,
gift sack, gift box, petf gift box, tree covering the face, tree covering the belly patch, floating tree, tall tree, real pine needles poking the face, text, human face, human body
```
(전송본은 조건 14 & 15 순서만 바로잡음)

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 수염 | 통과. 부드러운 털 질감의 큰 콧수염 & 턱수염 |
| W 입선 & 입 | 통과. 코 아래 W 입선 또렷, 입 닫힘, 이빨 없음 |
| 앞발 | 통과. 두 앞발이 가슴 높이에서 화분을 감쌈, 얼굴과 떨어짐, 세 마디 보임 |
| 트리 | 통과. 얼굴 안 가림, 별이 수염 옆 |
| 갈색 & 섞임 | 통과. 갈색 없음, 머즐 볼록 없음 |
| 얼굴 실측 | 주의. 눈폭 약 0.061 HW, 간격 약 0.217 HW (기준 0.054 & 0.206) — 조금 크고 넓지만 방실 방향이라 섞임 아님 |
| 귀 & 모자 | 통과. 모자가 귀 사이, 귀 모양은 매끈 레퍼런스와 비슷 |
| 배 패치 | 통과. 재킷 아래 반원 |
| 매끈 재질 | 주의. 몸은 매끈 유지, 모자 & 재킷 테두리는 털 질감으로 바뀜 (수염 털 지시가 의상 테두리로 번짐) |
| 꼬리 & 발끝 | 통과 |
