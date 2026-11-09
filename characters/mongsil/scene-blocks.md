# MONGSIL — 장면 프롬프트 블록

`templates/scene.md`의 골격에 끼워 넣는 **몽실이 전용 블록**이다. 골격과 워크플로는 그쪽에, 캐릭터 정체성 문장은 여기에 있다.

방실이 장면에는 이 파일을 쓰지 않는다. 한 프롬프트에 두 캐릭터 블록을 같이 넣는 것이 섞임의 원인이다 (`MONGSIL_Character_Lock.md` 10번).

원문 근거는 `MONGSIL_Character_Lock.md`다. 충돌하면 락이 이긴다.

---

## `## Subject`

```
MONGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that is clearly wider than it is tall and fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two SMALL glossy black vertical-oval eyes, taller than wide, set wide apart but not far apart: each eye is about 0.037 of the head's maximum width, and the gap between their centres is about 0.157 of that width. They are noticeably smaller and closer together than BANGSIL's. No highlight dot, no eyelashes, no eyebrows.
Two raised round white muzzle bumps side by side below the nose, and a small rounded dark triangle nose sitting on top of them with a short vertical groove running down between the bumps. No drawn mouth line of any kind.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Rounded triangular ears. The whole outer surface of MONGSIL's own left ear (screen right in front view) is brown #B79571, and that brown continues into a wave-shaped marking across the right half of the upper head. The other ear is white outside. Inner ears #FFCDB4.
Soft blush #FFCDB4 on both cheeks. A centred circular belly patch #FFCDB4 on the lower torso, about a third of the head's width.
A small brown #B79571 heart on the inner edge of the upper arm on the tail side, high near the shoulder, shown only when that inner edge is visible and the arm hangs free.
A brown #B79571 tail growing from the hip on the same side: ONE continuous padded upright crescent like a fat comma, taller than wide. Its outer edge is a single curve gently scalloped by two SHALLOW dimples, and the swells they separate are unequal — a large rounded dome at the top, then progressively smaller and flatter swells settling back into the curve. Its inner edge is one smooth unbroken curve. The tail is one mass, never a stack of separate balls.
Black features and whiskers #000000. No other brown anywhere on the body.
Expression: {표정}.
```

- `{표정}` 만 바꾼다. 나머지 문장은 줄이지 않는다. 줄이면 몸의 갈색 점과 입선이 돌아온다.
- 입을 벌리는 장면이면 마지막 줄을 `Expression: open-mouth smile with a soft pink tongue, no teeth and no fangs.`로 바꾼다.

## `## Critical conditions`

장면 고유 조건 앞에 항상 이 9개를 그대로 넣는다.

```
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
{10~. 이번 장면 고유 조건}
```

- 발이 보이면 위 `## Paws` 블록을 반드시 함께 넣는다. 손바닥이나 발바닥 안쪽이 보이면 패드 문장까지 더한다.


## `## Paws` — 발이 하나라도 보이면 항상 넣는다

캐릭터가 서 있든 앉아 있든 발끝은 거의 항상 보인다. 이 블록을 빼면 발끝이 매끈한 방망이로 나온다.

```
Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft visible grooves, like a small clover leaf; the middle lobe is the largest and sits slightly forward. The grooves stay clearly visible as shallow creases. The paw tip is never a smooth undivided club.
```

손바닥이나 발바닥 안쪽이 카메라를 향하면 **한 문장 더** 넣는다. 패드와 마디는 별개 사실이라 둘 다 써야 한다.

```
The {palm / sole} facing the viewer shows one large central pad and exactly THREE small round toe pads in an arc above it, and the outer edge of that paw still reads as three rounded lobes.
```

- `## Subject`와 `## Pose & Paws`에 `no fingers`, `fingerless`, `rounded nub`, `mitten` 같은 말을 절대 쓰지 않는다. 발 설명 옆에 붙은 부정어가 마디를 없애는 가장 흔한 원인이다.
- 손가락을 막아야 하면 `separated fingers, knuckles, claws, nails, human hand`를 **Negative 블록에만** 넣는다.

## `## Negative`

```
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
long fur, individual hairs, fabric seams, stitching, glossy plastic, vinyl shine, clay render,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face
```

장면 고유 Negative는 이 뒤에 더한다.
