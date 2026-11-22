# BANGSIL — 장면 프롬프트 블록

`templates/scene.md`의 골격에 끼워 넣는 **방실이 전용 블록**이다. 골격과 워크플로는 그쪽에, 캐릭터 정체성 문장은 여기에 있다.

몽실이 장면에는 이 파일을 쓰지 않는다. 한 프롬프트에 두 캐릭터 블록을 같이 넣는 것이 섞임의 원인이다 (`BANGSIL_Character_Lock.md` 10번).

원문 근거는 `BANGSIL_Character_Lock.md`다. 충돌하면 락이 이긴다.

---

## `## Subject`

```
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two low, broad, soft triangular ears with clearly ROUNDED tips, sitting on the upper outer corners of the head and leaning slightly outward. Each ear is far wider at its base than it is tall — the base is about 2.8 times the height that stands clear of the head, and that free height is only about an eighth of the head's width. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two glossy black vertical-oval eyes, taller than wide, set clearly wide apart: each eye is about 0.06 of the head's width across the cheeks, and the gap between their centres is about 0.22 of that width. They are noticeably larger and wider-set than MONGSIL's. No highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded black triangle nose sitting high, directly on the smooth face, its top level with the bottom of the eyes, and directly below it a drawn wide black W-shaped smile line.
NO whiskers of any kind. Instead, two small soft fur tufts on each side of the face, four in total, growing out of the lower cheek outline below the blush in the body colour: the upper tuft larger, the lower tuft smaller, both soft rounded points sweeping outward and slightly down, part of the head silhouette.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Eyes, nose and mouth line pure black #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail, no brown on the face.
Expression: {표정}.
```

- **방실 Element(`방실_3D` & `방실_3D_매끈`)는 현재 레퍼런스와 다른 이미지(수염 & 갈색 이목구비)로 등록돼 있다.** 재등록 전까지는 정면 컷이라도 해당 재질의 현재 `references/`(정면은 `Front.png`)를 `medias`로 함께 첨부하고, 결과에 수염이 붙었는지 반드시 본다 (`BANGSIL_Character_Lock.md` 0번 & 9-9번).
- `{표정}` 만 바꾼다. 나머지 문장은 줄이지 않는다. 특히 마지막 줄의 갈색 금지 문장을 빼면 몽실이의 갈색이 돌아온다.
- 입을 벌리는 장면이면 마지막 줄을 `Expression: open-mouth smile, the W mouth opening into a rounded smile, no teeth and no fangs.`로 바꾼다.

## `## Critical conditions`

장면 고유 조건 앞에 항상 이 9개를 그대로 넣는다.

```
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
{10~. 이번 장면 고유 조건}
```

- 발이 보이면 위 `## Paws` 블록을 반드시 함께 넣는다. 발바닥 안쪽이 보이면 패드 문장까지 더한다.

- **패드는 손바닥 표면에 붙은 무늬다.** 모양 & 크기 & 배치는 패드 레퍼런스와 똑같이 두고, 방향만 손바닥 & 팔이 기운 각도 그대로 같이 기울고 돌아가고 원근으로 눌린다. 패드 Element(레퍼런스)는 똑바로 선 정면 사진이라 AI가 그 방향을 그대로 붙이기 쉽다. 모양 & 개수 참고용이지 방향 참고용이 아니다 (2026-11-22 사용자 지적: 몽실 만세 컷에서 손은 바깥으로 꺾였는데 패드는 수직으로 선 채 나옴).
- 방실이 손바닥 & 발바닥은 `references/3d/Paw_Front.png` & `Paw_Hind.png`와 패드 Element(`CLAUDE.md` 디테일 표)를 쓴다. 패드는 중앙 큰 패드 1개 + 발가락 패드 3개 구성과 코랄 패드색(`#FCA39C`~`#FCADAC`)을 함께 쓴다 (`BANGSIL_Character_Lock.md` 4-1번).
- 흰 꼬리는 배경에 묻히기 쉽다. 밝은 배경이면 `the tail silhouette stays clearly readable against the background`를 넣는다.


## `## Paws` — 발이 하나라도 보이면 항상 넣는다

캐릭터가 서 있든 앉아 있든 발끝은 거의 항상 보인다. 이 블록을 빼면 발끝이 매끈한 방망이로 나온다.

```
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.
```

손바닥이나 발바닥 안쪽이 카메라를 향하면 **한 문장 더** 넣는다. 패드와 마디는 별개 사실이라 둘 다 써야 한다.

```
The {palm / sole} facing the viewer shows one large central pad and exactly THREE small round toe pads in an arc between the central pad and the paw tip, and the outer edge of that paw still reads as three rounded lobes. The pads are part of the {palm / sole} surface: they keep exactly the same shape, size and layout as the paw pad reference, but they tilt, rotate and foreshorten together with the paw and arm, following the exact angle of the paw — the toe pads always point toward the paw tip, never straight up the screen when the paw is tilted.
```

- `## Subject`와 `## Pose & Paws`에 `no fingers`, `fingerless`, `rounded nub`, `mitten` 같은 말을 절대 쓰지 않는다. 발 설명 옆에 붙은 부정어가 마디를 없애는 가장 흔한 원인이다.
- 손가락을 막아야 하면 `separated fingers, knuckles, claws, nails, human hand`를 **Negative 블록에만** 넣는다.

## `## Negative`

```
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
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face
```

장면 고유 Negative는 이 뒤에 더한다.
