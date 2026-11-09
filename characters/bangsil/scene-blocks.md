# BANGSIL — 장면 프롬프트 블록

`templates/scene.md`의 골격에 끼워 넣는 **방실이 전용 블록**이다. 골격과 워크플로는 그쪽에, 캐릭터 정체성 문장은 여기에 있다.

몽실이 장면에는 이 파일을 쓰지 않는다. 한 프롬프트에 두 캐릭터 블록을 같이 넣는 것이 섞임의 원인이다 (`BANGSIL_Character_Lock.md` 10번).

원문 근거는 `BANGSIL_Character_Lock.md`다. 충돌하면 락이 이긴다.

---

## `## Subject`

```
BANGSIL, the exact character in the reference: a compact, soft, upright 3D cat mascot with a dominant broad head that fills the top half of the figure, full cheeks, a soft rounded lower face, a short rounded torso, short stubby limbs, and no visible neck.
Two tall pointed triangular ears standing upright on top of the head. The outer surface of both ears is the body colour; the inner ears are #FFCBD1.
Two small glossy black vertical-oval eyes set wide apart, no highlight dot, no eyelashes, no eyebrows.
A completely flat face with no raised muzzle bumps. A small rounded dark triangle nose sitting directly on the smooth cheek surface, and below it a drawn wide W-shaped smile line in the same dark colour as the whiskers.
Exactly two whiskers per side, four in total: thin softly curved raised 3D rods attached at the cheek just outside the blush, never printed or engraved into the face.
Soft blush #FFCBD1 on both cheeks. A centred circular belly patch #FFCBD1 on the lower torso, about a third of the head's width.
A tail in the body colour growing from the hip on BANGSIL's own left (screen right in front view): one continuous padded upright mass, taller than wide, with a large dome plus exactly two more rounded bumps along its outer edge and one smooth unbroken curve along its inner edge.
Eyes, whiskers, nose and mouth line #000000. The body is one solid white cream colour from head to feet — absolutely no brown anywhere, no head patch, no ear patch, no arm marking, no brown tail.
Expression: {표정}.
```

- `{표정}` 만 바꾼다. 나머지 문장은 줄이지 않는다. 특히 마지막 줄의 갈색 금지 문장을 빼면 몽실이의 갈색이 돌아온다.
- 입을 벌리는 장면이면 마지막 줄을 `Expression: open-mouth smile, the W mouth opening into a rounded smile, no teeth and no fangs.`로 바꾼다.

## `## Critical conditions`

장면 고유 조건 앞에 항상 이 9개를 그대로 넣는다.

```
1. BANGSIL has NO brown anywhere: no head patch, no brown ear, no arm marking, no brown tail. The body is one solid colour broken only by the inner ears, blush, belly patch and paw pads.
2. The face is flat. There are no raised white muzzle bumps under the nose.
3. The W-shaped mouth line under the nose is present and clearly drawn.
4. Both ears are tall pointed triangles standing upright, matching each other, body-coloured outside with #FFCBD1 inside.
5. In any turned or side view, the lower face stays broad and rounded — never a triangle or a pointed chin.
6. The head stays a broad oval and fills the top half of the figure.
7. The belly patch is a centred circle following the body surface — not an elongated oval, not a button.
7-1. Every visible paw tip is divided into three rounded toe lobes by two visible grooves — never a smooth undivided club.
8. Exactly two raised whisker rods per side, growing from the cheeks — not printed, engraved, or pressed into the face.
9. Colours stay literal: inner ears, blush and belly patch #FFCBD1, features #000000. #FFCDB4 and #B79571 never appear.
{10~. 이번 장면 고유 조건}
```

- 발이 보이면 위 `## Paws` 블록을 반드시 함께 넣는다. 발바닥 안쪽이 보이면 패드 문장까지 더한다.
- 방실이는 앞발 손바닥 레퍼런스가 없다. 손바닥이 보여야 하는 장면이면 위 문장을 쓰되, 손바닥은 미검증이라고 사용자에게 알린다 (`BANGSIL_Character_Lock.md` 4-1번).
- 흰 꼬리는 배경에 묻히기 쉽다. 밝은 배경이면 `the tail silhouette stays clearly readable against the background`를 넣는다.


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
extra characters, two cats, duplicated BANGSIL, MONGSIL, calico cat, brown patched cat, realistic cat,
brown marking, brown ear, brown head patch, brown tail, heart on the arm, any brown on the body,
#FFCDB4, #B79571, peach inner ears,
raised muzzle bumps, puffy white muzzle, missing mouth line, no smile line,
human body, long limbs, visible neck, separated fingers, knuckles, claws, nails, human hands,
triangular face, pointed chin, narrow lower face, perfectly spherical head, vertically long head,
small head, short rounded ears, folded ears, mismatched ears, teeth, fangs,
elongated oval belly patch, off-centre belly patch, raised button belly, missing belly patch,
whiskers printed on face, engraved whiskers, thick rigid whiskers, three whiskers per side,
squat tail, bumps on the inner edge of the tail, tail as a row of equal beads, tapered tail,
tail invisible against the background,
long fur, individual hairs, fabric seams, stitching, glossy plastic, vinyl shine, clay render,
text, watermark, logo, cropped character, floating object, slim body, long arms, arms touching the face
```

장면 고유 Negative는 이 뒤에 더한다.
