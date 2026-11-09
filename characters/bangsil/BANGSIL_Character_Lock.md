# BANGSIL — CHARACTER IDENTITY LOCK

Written 2026-11-09 against the 8-view 3D reference sheet (Figma `기타 인쇄물` → `방실_3D`).
Every proportion stated below was measured on those images, not recalled. Where a number appears, the view it was measured on is named.

**This file covers BANGSIL only.** MONGSIL has its own lock at `characters/mongsil/MONGSIL_Character_Lock.md`. The two characters share a body but contradict each other on face, markings, and point colour. Load **one** lock per prompt. For a two-shot, see section 10.

## 0. Purpose, reference set, and priority

This is the identity lock for every BANGSIL image. It fixes anatomy, markings, and palette. Pose, expression, props, costume, camera, and environment may change only when they do not alter that identity.

The approved reference set is `characters/bangsil/references/3d/`:

| File | View | Native | Use it for |
|---|---|---|---|
| `Front.png` | 정면 | 1254 px | default; the measurement baseline for this file |
| `Left_3Q.png` | 45도 측면 | 1254 px | any three-quarter turn |
| `Left_Profile.png` | 측면 | 1254 px | profile and near-profile |
| `Back.png` | 후면 | 1254 px | back and rear three-quarter; the clean-back proof |
| `Smile.png` | 정면 웃는얼굴 | 1254 px | open-mouth smile |
| `Sit.png` | 앉은자세 | 1254 px | sitting; the hind-sole pad reference |
| `Run.png` | 측면 뛰는자세 | 1254 px | walking, running, mid-stride |
| `Wave.png` | 손 흔들기 | 1254 px | a raised arm; **the front-paw palm reference** — the palm faces the camera. Also the reference for how far a raised paw clears the head |

Rotate one coherent character between views; never redesign per view.

Higgsfield Element: `방실_3D` (`1173218c-f55e-4561-92eb-04fda591b0e4`), registered 2026-11-09 from the four turnaround views of the current references. How many of the four are actually injected has not been measured, so attach the matching angle as a media input for anything that is not the front view. The older `방실3D_통합` holds the superseded render and the superseded ear and tail wording — do not use it.

When sources disagree, apply this order:

1. The approved reference image closest to the requested view
2. This lock file
3. `styles/3D_Felt.md`
4. The scene prompt

**이 순서의 예외 — 섹션 6이 "미반영"이라고 적어 둔 항목.** 레퍼런스 렌더가 아직 최신 규칙을 따라가지 못한 항목은 섹션 6의 locked value가 레퍼런스를 이긴다. 현재 해당하는 것은 **수염 & 코 & 입선 색상**뿐이며, `#000000`이 기준이다. 그 외 모든 항목은 위 순서 그대로 레퍼런스가 우선이다.

Do not replace a visible reference detail with a guessed measurement, a named shape, or an inferred colour. If a requested view exposes something none of the eight images show, keep the visible structure intact and say the detail is unverified rather than inventing it. **`Wave.png` is the front-palm reference** — the raised paw shows its palm with pads. See section 4-1.

## 1. Non-negotiable identity and proportion

- BANGSIL is a compact, soft, upright cat mascot: a dominant head, a short rounded torso, short stubby limbs, and no visible neck.
- **The head is the biggest thing about the character.** Measured on `Front.png`: the head is **739 px at its widest**, the whole standing figure from ear tip to sole is **1179 px**, and the chin sits at the **50 % mark** of that height. So the head fills the top half of the figure and its width is about **0.63 × the total height**.
- The head is a broad, softly rounded oval, clearly wider than the lower face is deep. Not a sphere, not a vertical oval, not a wedge, not a triangle.
- Keep the padded, chubby silhouette in every scene, including under clothing. The body never becomes slim, tall, or long-waisted.
- Arms and legs stay as short and stubby as in the references. A raised, reaching, waving, or hugging arm keeps exactly the same short length. A pose never lengthens a limb. BANGSIL's arms hang slightly further out from the torso than MONGSIL's — follow `Front.png`.
- When both arms are raised, they open outward in a V **away from the face**, with clear space between each arm and the head.

### Reaching a prop without lengthening an arm

BANGSIL's arms are too short to reach many props. When a pose needs more reach, buy it from the **body**, never from the arm:

- Rise onto tiptoe, lean the torso forward, bend at the hip, stretch upward through the shoulders, or move BANGSIL physically closer to the prop.
- Or lower the prop so it falls inside the arm's real reach.
- **Reject** any result where a forearm or upper arm is visibly longer or thinner than the references. Report the failure to the user; regenerate only when they ask.

## 2. Head and face

### Ears — an identity feature

BANGSIL's ears are **low, broad, soft triangles with rounded tips**, sitting on the upper outer corners of the head dome and leaning slightly outward. They are not tall, not upright, and not pointed. Measured 2026-11-09 on `Front.png` and on the approved face reference:

| | Measured |
|---|---|
| Free height standing clear of the head dome | **0.11 – 0.12 × the head's maximum width** |
| Base width : free height | **2.7 – 2.9 : 1** — far wider than tall |
| Width at 20 % down from the tip | **0.42 – 0.49 × the base width** |
| Width at 50 % down from the tip | 0.72 – 0.76 × the base width |
| Tip centre | about 0.65 × the head half-width out from the head centre, leaning outward |

Read the first row again. The part of the ear standing clear of the dome is only about **one eighth of the head's width**. Everything above the eyes is mostly dome, not ear.

- The tip is a **soft round curve, not a point.** One fifth of the way down from the tip the ear is already nearly half as wide as its base.
- The outer surface of **both** ears is the body colour. The inner ear is the point colour (section 6).
- Both ears match each other. Do not fold them and do not colour one differently.

**Failure measured 2026-11-09 — caused by this section's own earlier wording.** This section used to say "tall, pointed triangular ears standing upright… noticeably taller and sharper than MONGSIL's… do not round the ear tips off". Both validation renders came out as a fox, in two different ways:

| | base : height | width at 20 % down |
|---|---|---|
| Reference | 2.7 – 2.9 : 1 | 0.42 – 0.49 |
| `cut1` 방실 앉기 | 2.6 : 1 | **0.07** — a needle point |
| `cut3` 투샷 | **1.3 : 1** — twice too narrow | 0.47 |

**Reject** when base : height falls below **2.2 : 1**, or when the width at 20 % down from the tip is under **0.35** of the base width. Either one reads as a fox.

### How BANGSIL's ears differ from MONGSIL's — smaller than previously written

Measured on both characters' `Front.png` with the same method:

| | Free height ÷ head width | Base : height | Width at 20 % down |
|---|---|---|---|
| BANGSIL | 0.112 | 2.92 : 1 | 0.49 |
| MONGSIL | 0.082 | 2.97 : 1 | 0.45 |

The **shape is the same** on both characters — equally broad, equally round-tipped. BANGSIL's ears simply stand about **1.4 × higher** off the dome. That is the whole difference, and it is a subtle one.

Because of this, **ear shape is not a usable mixing check.** The reliable separators are the muzzle, the mouth line, brown, and the point colour (section 10).

### All views

- Broad forehead, full cheeks, substantial lower face. The jaw is a wide soft curve.
- **Expression may change; feature scale, feature spacing and feature colour may not.** The numbers below are the face. Change them and it stops being BANGSIL even if the colours are right.

### Face measurements — the numbers that stop the face deforming

Everything is expressed against **HW = the head's maximum width in that frame**, so it holds at any crop or canvas size. Measured 2026-11-09 across `Front.png`, `Left_3Q.png`, `Sit.png`, `Run.png`, `Wave.png`.

| | Measured | Accept |
|---|---|---|
| Eye width ÷ HW | **0.051 – 0.057** | 0.046 – 0.063 |
| Eye height ÷ width | 1.48 – 1.49 | taller than wide, 1.35 – 1.65 |
| Gap between eye centres ÷ HW (front view) | **0.206 – 0.207** | 0.18 – 0.23 |
| Nose centre, below the eye line | +0.076 HW | +0.06 – +0.10 HW |
| Nose + W mouth block, width ÷ HW | **0.251** | 0.21 – 0.29 — the mouth is wide |
| Whisker length ÷ HW | 0.258 – 0.259 | 0.23 – 0.29 |
| Whisker thickness ÷ HW | 0.0115 – 0.0122 | 0.009 – 0.015 |
| Whisker roots, from face centre | ±0.33 HW | ±0.30 – 0.37 HW |
| Whisker rows, below the eye line | +0.023 and +0.087 HW | two rows, the lower about 0.06 HW under the upper |
| Blush width ÷ HW | 0.181 – 0.192 | 0.16 – 0.22 |
| Blush centre, from face centre | ±0.23 HW | ±0.20 – 0.26 HW |
| Blush centre, below the eye line | +0.071 – 0.072 HW | +0.05 – +0.10 HW |
| Inner ear patch, from face centre | ±0.32 HW, 0.27 HW above the eye line | — |

**BANGSIL's eyes are large.** At 0.054 HW they are about **1.5 × MONGSIL's** (0.036 – 0.039 HW) and sit **noticeably wider apart** (0.206 vs 0.157 HW in front view). That difference held in all five views of each character and is the most reliable face separator there is — more reliable than the ears, which the two characters share (section 10). Small, close-set eyes on BANGSIL mean MONGSIL's face leaked in.

### Measured feature colours — renders, not spec

| | Sampled | Spec |
|---|---|---|
| Eyes | `#060502` – `#080604` | `#000000` ✓ matches |
| Whiskers | `#351002` – `#391403`, R−B **+48 to +54** | `#000000` — render is warm brown (section 6 pending item) |
| Nose & mouth line | `#310C01`, R−B +48 | `#000000` — same pending item |

The warm brown is the known mismatch recorded in section 6, not a generation error. What *is* an error is the opposite direction: if BANGSIL's whiskers come out a **neutral dark gray** (R−B under about 25), that is MONGSIL's value leaking in.

### Profile rotation

Rotate the same broad head volume. Do not compress or carve away the lower face.
**Reject** — and report it, regenerating only on the user's request — if the jaw or chin tapers to a point or the profile reads triangular.

### Eyes, nose, mouth — the flat face

- Two glossy black eyes, each a **vertical oval** (taller than wide), set wide apart. No highlight dot, no eyelashes, no eyebrows, no pupils. Size and spacing are fixed by the table above — **0.054 HW wide, 0.206 HW apart.** They are noticeably larger and wider-set than MONGSIL's.
- The nose is a small **rounded triangle**, point down, sitting directly on the face, centred and about 0.08 HW below the eye line.
- **BANGSIL's face is flat.** There are no raised white muzzle bumps under the nose. The nose sits on a smooth cheek surface. *(This is one of the two things that most reliably turns BANGSIL into MONGSIL — see section 10.)*
- Below the nose there is a **drawn mouth line: a wide W-shaped smile**, two soft curves meeting under the nose, in the same dark colour as the whiskers. The mouth line is always present in the default closed expression.
- In profile the same mouth reads as a single hook curving down and back from the nose — see `Left_Profile.png`.
- An open mouth is allowed when the user asks, or when matching `Smile.png`: the W opens into a rounded smile. **No teeth and no fangs, in any view, in any frame.**
- In video, an open or talking mouth is the most reliable way to make teeth appear. Unless the user asked for speech, lock the mouth closed for the whole clip rather than relying on a negative prompt.

## 3. Markings and left/right orientation

All directions use BANGSIL's anatomical left/right. In the front view, BANGSIL's left is the **screen right**.

### BANGSIL HAS NO BROWN. ANYWHERE.

- There is **no brown head patch, no brown ear, no brown arm marking, and no brown tail.** A brown-channel scan of all eight references returns **zero** brown regions, `Back.png` included.
- BANGSIL is one solid body colour from head to feet, broken only by the point-colour elements in section 6.
- `Back.png` is the proof image: a completely clean white back, clean arms, clean legs, clean tail.
- **Any brown on BANGSIL means MONGSIL's lock leaked into the prompt.** Reject it and never retouch it — a mixed result is fixed by generating again from a clean prompt, which the user asks for.

### The only non-body colours on BANGSIL

Inner ears, blush, belly patch, paw pads — all the point colour. Eyes, whiskers, nose, mouth line — dark. Nothing else.

### Body has no markings

Apart from the belly patch, the body has **no markings at all**: no spots on the waist, sides, back, flanks, shoulders, or legs, in any colour. When a prompt uses the short scene format, carry the body-part enumeration verbatim — back, side, flank, shoulder, shoulder blade, rump, hip, waist, chest, belly, thigh, both arms, both forearms, both paws, both legs — and state that BANGSIL is **not** a calico or patched cat.

## 3-1. Tail — shape lock

The tail is the **same sculpt as MONGSIL's, in the body colour instead of brown.** Colour is the only difference; the geometry rules below are identical and are not optional.

### Geometry

- **ONE continuous padded mass** in the body colour, growing from the hip on BANGSIL's anatomical left (screen right in the front view).
- Standing, it rises and curls **outward and upward, away from the body**, and is **taller than it is wide — about 1.3–1.5 : 1.** Never squat, never as wide as tall.
- The whole tail is **ONE padded crescent — a fat comma.** The silhouette is continuous from base to tip and never pinches in to less than about **85 % of the local width** anywhere along it.
- Its **outer edge** (facing away from the body) is that same single curve, **gently scalloped** by **TWO shallow notches of unequal depth**. Measured on `Front.png` against a 144 px tail: the **upper notch 10 px (≈ 7 %)**, the **lower notch 3 px (≈ 2 %)**. Quote them separately — one blanket figure makes the lower notch three times too deep. They are soft dimples in a continuous edge, not divisions.
- The three swells that the notches separate are **not equal and not round.** The top dome is the largest and most rounded; the two below it are progressively **smaller and flatter**, settling back into the curve toward the base.
- Its **inner edge** (facing the body) is **ONE long smooth unbroken curve** with no bumps and no notches. The asymmetry between the two edges is the signature of the shape.
- The **base** is a thick stalk merging smoothly into the hip. The tail never tapers to a point, never narrows to a stem, never detaches.

**Failure measured 2026-11-09.** This section used to say the outer edge "carries exactly THREE rounded forms stacked along it" and that the whole shape "reads like a fat upright clover leaf". Both phrases describe three separate objects, and that is exactly what came out: in `cut1` and `cut3` the tail rendered as **three near-equal spheres stacked like a snowman**, round on both edges, with deep pinches between them. The user's words were "무슨 3개 동그란 알갱이 같은게 붙어있는것처럼 오바스럽게 굴곡이 많아".

**Reject** when the lobes read as separate balls, when any two swells are the same size, when the inner edge grows bumps, or when a notch cuts deeper than about **15 %** of the tail's width.
- In `Back.png` and `Sit.png` the same form swings out sideways. Rotation is allowed; reshaping is not.

### Verifying a white tail

Because the tail is the same colour as the body, it cannot be isolated against a pale background the way MONGSIL's brown tail can. **Check it against `Back.png` and `Sit.png`**, where the tail reads clearly away from the torso, and confirm all five:

1. Height is visibly greater than width (about 1.3–1.5 : 1 standing).
2. The silhouette is **one continuous crescent**. Cover the notches with a thumb and it still reads as a single padded mass.
3. The outer edge swells are **unequal and progressively smaller** going down from the top dome, and the two notches between them are shallow dimples of **unequal depth** — upper about 7 % of the tail's width, lower about 2 %, neither more than 15 %.
4. The inner edge is a single smooth curve with no bumps.
5. The mass joins the hip with a thick base.

On a pale background a white tail also tends to disappear into the body or the backdrop. If the tail silhouette is not legible, that is a failure, not a lighting preference.

### Wordings that have caused failures — do not use

- "short and broad", "as wide as tall", "compact bunched mass" → squat blob
- "a few lobes overlapping side by side" → beads in a row
- "bumps along its free edge" without the height ratio → caterpillar
- "cloud", "fluffy", "puffy" used alone → separated puffs or a smooth paddle
- "three rounded forms stacked along it", "clover leaf" → three equal spheres like a snowman (실측 2026-11-09, `cut1` & `cut3`)

## 4. Body and belly patch

- Keep the torso short, rounded, and compact beneath any clothing.
- The belly patch is a **circle** in the point colour. Measured: `Front.png` 237 × 245 (w/h 0.97), `Smile.png` 221 × 230 (0.96), `Run.png` 211 × 215 (0.98), `Wave.png` 229 × 226 (1.01), `Sit.png` 209 × 231 (0.90). Render it as a circle, never an elongated oval.
- It is not a button, not a pocket, not a separate raised object. It follows the body surface and deforms only with perspective.
- It is centred on the belly, sits in the lower half of the torso, and its diameter is about **32 % of the head width**.
- When clothing or a prop would cover the belly, keep at least part of the patch visible unless the user accepts it being hidden.

## 4-1. Paws — the three-lobed tip and the pads

This is the single most reliably broken detail. The failure is always the same: the three lobes dissolve and the paw comes out as one smooth club. Treat the lobes as a locked silhouette feature, not a surface detail.

### The three-lobed tip — every paw, every view

- **Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft grooves**, like a small clover leaf. The middle lobe is the largest and sits slightly forward.
- This is true of the front paws and the hind feet, and it is visible from **outside** even when the palm is not facing the camera. `Front.png` and `Wave.png` (standing feet) and `Sit.png` (front paws resting on the belly) all show it.
- The grooves read as shallow creases running a short way back from the free edge. They are never smoothed away.
- **A smooth, undivided, club- or mitten-shaped paw tip is a failure.** Not a stylistic simplification — a failure.

### The pads — only when the inner face shows

- A **hind paw sole facing the viewer** carries one large central pad and **three** round toe pads in an arc above it — `Sit.png`, `Run.png`.
- **Three, not four.**
- Even with the inner face toward the camera, the outer edge of the paw still reads as the three lobes above. Pads and lobes are two separate facts; state both.
- A **front paw palm facing the viewer** carries the same layout — one large central pad with **three** round toe pads in an arc above it. `Wave.png` is the reference for it. *(Correction 2026-11-09: this file previously said `Wave.png` showed the back of the paw and that BANGSIL had no front-palm reference. Both were wrong. The palm faces the camera and the pads are plainly visible.)*
- Measured on `Wave.png`: the central pad is a wide oval about **70 × 38 px** on the 1254 px canvas; the three toe pads sit above it, the middle one largest (about 35 × 30) and the outer two a little smaller (about 34 × 30 and 27 × 23).
- The back of a paw is plain body colour with no pads.
- Pad pink is **the same point colour as the inner ears, blush, and belly patch** — not a separate colour. Sampled on `Wave.png`, every pink area lands in the same coral range under 3D shading (pads `#FCA29B`, inner ears `#ED8A8A` – `#EF9393`, blush `#E18B87` – `#E69D9C`, belly `#F3A5A8`), all more saturated than the flat `#FFCBD1` spec. That gap is the render, not a different swatch. See the open item in section 6 before writing an exact pad HEX into a prompt.

### How to word it so the lobes survive

The lobes are usually destroyed by the prompt, not by the model's inability to draw them. Three rules, in order of importance:

1. **Describe the shape positively, never by negation.** Write `a three-lobed clover-shaped paw tip with two soft grooves`. Do **not** write `rounded nub`, `mitten`, `paddle`, or `simple rounded paw` — each of those is a club in the model's vocabulary.
2. **Keep every digit word out of the Subject and Pose sentences.** `no fingers`, `fingerless`, `without fingers` sitting next to the paw description is the most common cause of the club. If digits must be excluded at all, put `separated fingers, knuckles, claws, nails, human hand` in the **Negative block only**, far from the paw sentence.
3. **Name the grooves, not just the lobes.** The grooves are what the model drops first. `divided by two visible grooves` does more work than `three toe lobes`.

Add these to the Negative whenever a paw is visible:

```
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads
```

### Verification

Crop each visible paw, enlarge it, and confirm two things separately: the outer edge shows three lobes with two grooves, and — if the sole shows — one large pad plus exactly three toe pads. Check at magnification every time, and tell the user when a video cannot be frame-checked.

## 5. Whiskers

- **Two whiskers per side, four in total.** Verified on `Front.png`, `Left_Profile.png`, `Smile.png`, `Sit.png`, `Wave.png`. Not three, not six.
- They are **thin, softly curved, raised 3D rods** with a visible highlight along the top and a soft shadow under them. They are not printed lines, grooves, or flat marks.
- Each pair attaches at the cheek **just outside the blush** and sweeps outward and slightly upward. The upper whisker is longer and flatter; the lower one angles down a little more.
- In the straight front view they lie across the cheek inside the head silhouette. At turned angles the near-side pair crosses the silhouette and reads free-standing in space. Both are correct; follow the view.
- Whisker colour follows section 6.

## 6. Palette lock

Keep these values as literal data. Do not replace codes with colour names, delete them during revisions, or invent missing codes from a rendered screenshot.

| Element | Locked value | Source |
|---|---|---|
| Inner ear | `#FFCBD1` | Figma variable `방_ear_inner` (그래픽소스) |
| Blush | `#FFCBD1` | same point colour |
| Belly patch | `#FFCBD1` | same point colour |
| Eyes, whiskers, nose, mouth line | `#000000` | black family |
| Tail | body colour — identical to the torso | |
| Body | white / warm cream, as in the references | |

**`#FFCBD1` is BANGSIL's point colour and nothing else carries it.** MONGSIL's point colour is `#FFCDB4` and must never appear on BANGSIL. The two differ by only a few digits and look similar in a swatch — copy them, never retype from memory.

Two open items, carried honestly rather than guessed:

- **Paw pads.** The references render them in the point-colour family, but no variable has been confirmed. Follow the reference colour and flag it as unverified if a scene depends on an exact pad value.
- **Whiskers and nose in the current renders.** The 3D renders show BANGSIL's whiskers and nose as dark **brown** (sampled `#2D1003` and `#3F1501`), not black. The decision on 2026-11-09 was to unify both characters on the black family, so `#000000` above is the spec and the renders are the older state. Expect a small mismatch until the renders are redone.

Lighting may create material shading, but it must not redefine the base palette.

## 7. Style separation

- This document defines identity, not rendering technique. Read `styles/3D_Felt.md` for 3D material, lighting, and rendering constraints.
- A different rendering treatment may not alter the locked silhouette, the absence of brown, the point colour, the belly-patch shape, the mouth line, or the whisker count.

## 8. Allowed scene changes

Pose, expression, action, costume, prop, background, crop, camera, lighting, and atmosphere may change. If clothing or a prop hides a locked feature, do not move the feature to make it visible.

## 9. Common generation failures — mandatory validation

Before delivery, compare against the closest reference view and reject a result with any of the following. **Report which item failed and what would fix it — do not regenerate on your own; the user asks for that** (CLAUDE.md 기본 이미지 생성 설정 4번):

1. **Any brown on the body** — head patch, ear, arm marking, or tail. BANGSIL has none.
2. **Raised muzzle bumps** under the nose. BANGSIL's face is flat.
3. **Missing mouth line** — the W smile under the nose is gone.
4. **Fox ears:** an ear whose base is under 2.2 × its free height, or whose width 20 % down from the tip is under 0.35 of its base — a tall, narrow, or pointed ear. Also mismatched ears. (Rounded tips and a low broad shape are correct — see section 2.)
5. **Wrong point colour** — `#FFCDB4` (MONGSIL's) used on the ears, blush, belly, or pads instead of `#FFCBD1`.
6. **Triangular profile:** lower face crushed, narrowed, or pointed when rotated.
7. **Wrong head silhouette or size:** a sphere, a vertical oval, a narrow face, or a head that no longer fills the top half of the figure.
8. **Wrong belly patch:** an elongated oval, off-centre, a button, or not following the body surface, instead of a centred circle.
9. **Embedded whiskers, or the wrong count:** whiskers painted flat into the face, or any number other than two per side.
10. **Teeth:** any tooth, fang, or tooth row, in a still or in any video frame.
11. **Palette drift / data loss:** a locked HEX removed, renamed without the code, or changed.
11-1. **Not a failure:** brown whiskers or a brown nose matching the current renders. That is the known pending mismatch in section 6, not a generation error — note it and move on.
12. **Wrong body or limbs:** slim body, long waist, or arms and legs longer than the references; an arm stretched to reach a prop.
12-1. **Raised arm fused to the head:** a raised paw touching or overlapping the face so the silhouette reads as one shape there. Background must stay visible between the paw and the cheek at every height — but it can be a **thin sliver**. Measured on `Wave.png`: the gap narrows to about **10–14 px against a 145 px paw (≈ 7 % of the paw's width)** and never closes. The failure is 0 px — one fused shape. *(Correction 2026-11-09: this line previously demanded a gap as wide as the paw, which rejects `Wave.png` itself.)*
13. **Club paw:** any visible paw tip has lost its three rounded lobes and two grooves and reads as one smooth undivided club or mitten. This is the most frequent failure — check every paw in every frame.
13-1. **Missing or miscounted pads:** a sole **or a palm** faces the viewer without its pads, or shows four toe pads instead of three.
14. **Hidden belly patch:** clothing or a prop covers the whole belly patch without the user accepting it.
15. **Deformed or invisible tail:** fails any of the five checks in section 3-1, or the white tail is not legible against the background. The specific failure to watch for is the **snowman tail** — three near-equal spheres stacked with deep pinches, instead of one continuous crescent with shallow unequal scallops.
16. **Unverified specificity:** a count, ratio, contour, or colour stated or generated as certain despite not being visible in the relevant reference.

## 10. BANGSIL and MONGSIL together

The two characters share a body and contradict each other on the face. Loading both locks into one prompt is how they get mixed.

**One lock per prompt.** For a solo BANGSIL scene, this file is the only character lock in the prompt. Never carry a sentence from MONGSIL's lock into a BANGSIL prompt, and never use MONGSIL's `Paw_Front.png` or any MONGSIL reference as a BANGSIL attachment.

### Where they differ

| | BANGSIL | MONGSIL |
|---|---|---|
| Point colour | `#FFCBD1` | `#FFCDB4` |
| Brown `#B79571` | none | head & ear wave, arm heart, tail |
| Eyes | **0.054 HW wide, 0.206 HW apart** | **0.037 HW wide, 0.157 HW apart** — about 1.5 × smaller |
| Whiskers in the renders | warm brown, R−B +48 to +54 | neutral dark gray, R−B +8 to +19 |
| Ears | low broad rounded triangles, free height 0.11 × head width | same shape, free height 0.08 × head width |
| Muzzle | flat face | two raised white bumps |
| Closed mouth | W-shaped mouth line | no mouth line at all |
| Tail | body colour | brown |
| Whiskers | 2 per side | 2 per side |
| Belly patch | circle, point colour | circle, point colour |

> **Eyes are the strongest separator.** Eye width and spacing differ by about 1.5 × and held across all five views of each character (section 2). Check the eyes first.
>
> **Ears are a weak separator.** Both characters have the same low broad round-tipped ear shape; BANGSIL's simply stand about 1.4 × higher. Do not rely on ear shape to tell a mixed render apart — use the muzzle, the mouth line, brown, and the point colour (실측 2026-11-09, 섹션 2).

### Two-shot scenes

When both appear in one image, load both locks and state the separation explicitly — which character is on which side, and that each keeps its own face and colours. Then add the size rule:

> **MONGSIL's total height is 0.88 – 0.90 × BANGSIL's.** BANGSIL's ear tips sit clearly higher than MONGSIL's. Both stand on the same ground line.

Measured on a 2026-11-09 두 캐릭터 비교 render **that is not stored in this repository** — the numbers stand, the image cannot be re-checked here: BANGSIL 1166 px tall, MONGSIL 1021 px (**0.876**); head widths 724 px and 652 px (**0.901**). The two ratios are not the same, so write **0.88 – 0.90**, not "a consistent 10 %". BANGSIL's taller ears account for most of the difference between them. In solo frames each character fills its own canvas, so size only carries meaning when they share a frame.
