# 방실 매끈 택배 배달부 — 의상 & 소품 + 투명 누끼

> 2026-11-21 정리: 방실 옛 얼굴 기준 수치는 지웠다. 현재 기준은 `characters/bangsil/BANGSIL_Character_Lock.md` 2번 & 5번. 원래 전송본은 git 기록(`c4c288e` 이전)에 있다.

- 날짜: 2026-11-19
- 캐릭터: 방실
- 요청(한국어): 택배 배달부 콘셉트 (참고 이미지: 다른 회사 마스코트가 주황 볼캡 & 택배상자를 든 도시 장면 — 의상 & 소품 참고용, 생성에는 첨부 안 함). 주황 볼캡 + 앞면 흰 택배 아이콘, 두 앞발로 가슴 앞 크라프트 택배상자, 상자 앞면 흰 택배 아이콘 & '바로구매', 모자만 착용, 정면 전신, 매끈 무광 소프트 비닐, 배경 없는 투명 PNG, 바닥 & 그림자 없음, 1:1
- 상태: 미확인
- 모델 & 품질 & 해상도 & 비율: GPT Image 2 & low & 1K & 1:1
- Element: 방실_3D_매끈 (cdfcf687-3667-4ee4-b795-33b41009c558)
- 첨부 레퍼런스: 없음 (정면)
- job: 51a7eb9b-346c-4f1e-b729-031bbc5ac42e (단색 배경) → 누끼 job 74c06bfe-b155-45e7-a556-782f28cf74c5 (`image_background_remover`)
- 크레딧: 생성 0.5 + 누끼 1 (balance 958.5 → 957.5) / 남은 957.5

## 결정 메모

- 모자 아이콘 & 상자 아이콘 & '바로구매' 문구는 생성하지 않고 빈 면으로 만듦 (`templates/scene.md` 7번 "글자 & 로고는 Figma에서"). 사용자 요청서의 텍스트 항목은 Figma 합성 단계로 넘김
- 택배상자는 펫프 아이콘(`택배상자` Parcel_Box)이 있지만 사용자가 펫프 아이콘을 부르지 않아 쓰지 않음 (2026-11-19 규칙)
- 투명 PNG는 단색 #E4DFE3로 생성 후 Higgsfield 배경 제거로 처리. 그림자 & 바닥 없음 지시
- 배 패치는 상자를 가슴 높이로 올려 아래 반원이 보이게 함 (락 4번)

## 최종 프롬프트

```
<<<cdfcf687-3667-4ee4-b795-33b41009c558>>> # BANGSIL delivery courier — STEP 1 wardrobe & prop, square 1:1

## Subject
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.06 of the head's width across the cheeks, and the gap between their centres is about 0.22 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded dark triangle nose sitting directly on the smooth cheek surface, and below it a drawn wide W-shaped smile line in the same dark colour as the whiskers.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, whiskers, nose and mouth line #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail.
Expression: natural, cute, happy smile with the W smile line, mouth closed.

## Orientation
- Body faces: the camera, front view
- Head faces: the camera, the same direction as the body
- Eyes look at: the camera
The head turns on the body naturally with no visible neck. The face, ears, and all features stay in place and never mirror.

## Pose & Paws
BANGSIL stands upright and hugs one parcel box in front of its chest with both short arms: the two paws press against the left and right sides of the box near its lower corners, and the box rests against the upper chest just below the face. The arms stay as short as the reference; the elbows stay at the sides of the body. Both paws stay well below the face. Legs stay short and stubby, standing straight.
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.

## Prop
Parcel box: one real corrugated kraft cardboard shipping box — natural brown kraft paper colour with real corrugated cardboard texture, slightly rounded worn edges, a strip of clear packing tape across the top seam. Size: about 0.6 of the head's width wide and a little less tall. Held at the horizontal centre of the body at chest height, so the lower part of the round belly patch stays visible below the box. The FRONT FACE OF THE BOX IS COMPLETELY PLAIN — no icon, no logo, no letters (they will be added later in design software). It touches both paws and the chest — not floating.

## Wardrobe
Only one item, no clothes:
- Delivery courier baseball cap: a real cotton-twill orange baseball cap with a curved front brim, a small button on top and stitched panels, sitting on top of the head BETWEEN the two ears, brim facing forward; both low broad ears stay fully visible on either side. The FRONT PANEL OF THE CAP IS PLAIN orange — no icon, no logo, no letters (added later in design software).
No shirt, no trousers, no shoes. It sits on top of the character without changing the head shape, ears, or body volume. The tail stays visible.

## Environment
Plain solid flat background colour #E4DFE3, seamless and completely empty, for a clean cutout later. No floor line, no cast shadow, no contact shadow, no props on the ground. The white tail silhouette stays clearly readable against the background.

## Camera
Front view, eye level, square 1:1 frame, full body from cap to feet with the box and the tail, centred, nothing cropped.

## Style
BANGSIL itself is a smooth, clean, soft matte vinyl / soft-touch clay 3D mascot: no felt pile, no fur, no fibres on its body; very soft satin response to light. The cap and box are real-world materials (cotton twill, corrugated kraft cardboard, packing tape) and look clearly different from the smooth vinyl body. Soft even studio lighting. Paw pads, nose, and whisker rods are raised relief.

## Critical conditions (must all hold)
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn.
4. Both ears are low broad triangles with rounded tips, each clearly wider at the base than tall, matching each other, body-coloured outside with #FFCBD1 inside. Neither ear is a tall upright spike and neither tip comes to a point.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face.
8-1. The eyes stay LARGE and wide-set: each about 0.06 of the head's width across the cheeks, centres about 0.22 of that width apart. Small, close-set eyes are MONGSIL's face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
9-1. The tail silhouette is ONE continuous crescent. The notches on its outer edge are shallow dimples and the swells are unequal — never three equal balls stacked like a snowman.
10. The orange cap sits between the ears; both ears stay fully visible. The cap front is plain, with no icon or text.
11. The box is held at chest height at the centre; the lower part of the round belly patch stays visible below it. The box front is plain, with no icon or text.
12. Both paws hold the box well below the face; the arms stay short; legs stay short.
13. No clothes other than the cap. No floor, no shadow, nothing else in the frame.
14. Smooth matte vinyl body; the cap and box are real materials.

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
long fur, individual hairs, seams or stitching on the cat body, felt texture, flocked pile, fuzz, embossed grain, mirror gloss, wet look,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face,
paw touching the face, arm fused to the head,
logo on cap, icon on cap, text on cap, logo on box, icon on box, text on box, letters, Korean text, stickers, shipping label, barcode,
shirt, uniform, vest, trousers, shoes, gloves, backpack,
city background, buildings, road, other characters, extra boxes, stacked boxes,
floor, ground shadow, contact shadow, cast shadow, reflections,
hat covering the ears, cap covering the eyes, backwards cap,
box covering the face, box covering the whole belly, floating box, plastic box, smooth vinyl box,
open mouth, tongue, teeth, exaggerated pose, long arms, long legs
```

## 검증 (락 9번)

| 항목 | 결과 |
|---|---|
| 갈색 & 머즐 | 통과. 갈색 없음, 납작한 얼굴 |
| W 입선 | 통과 |
| 귀 & 모자 | 통과. 볼캡이 귀 사이, 두 귀 모두 보임 |
| 얼굴 실측 | 주의. 눈폭 0.062 HW, 간격 0.237 HW — 방실 방향으로 크고 넓음, 섞임 아님 |
| 수염 | 통과. 한쪽 2가닥 |
| 배 패치 | 통과. 상자 아래로 반원 |
| 앞발 & 뒷발 | 통과. 세 마디 & 홈 보임, 앞발이 얼굴에서 떨어짐 |
| 꼬리 | 통과. 흰 초승달, 누끼에서도 온전 |
| 재질 | 통과. 몸 매끈 비닐, 모자 면 트윌, 상자 골판지 & 테이프 |
| 무지 면 | 통과. 모자 앞면 & 상자 앞면에 글자 & 아이콘 없음 (Figma용) |
| 누끼 | 통과. RGBA, 네 모서리 알파 0, 어두운 배경 합성에서 테두리 깨끗 |
