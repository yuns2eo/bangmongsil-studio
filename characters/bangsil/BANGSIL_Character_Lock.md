# BANGSIL — CHARACTER IDENTITY LOCK

Written 2026-11-21 against the current reference sets (`references/3d/` & `references/3d_smooth/`).
Every proportion stated below was measured on the current images, not recalled. Where a number appears, the view it was measured on is named.

**This file covers BANGSIL only.** MONGSIL has its own lock at `characters/mongsil/MONGSIL_Character_Lock.md`. The two characters share a body but contradict each other on face, markings, and point colour. Load **one** lock per prompt. For a two-shot, see section 10.

## 0. Purpose, reference set, and priority

This is the identity lock for every BANGSIL image. It fixes anatomy, markings, and palette. Pose, expression, props, costume, camera, and environment may change only when they do not alter that identity.

The approved reference sets, all 1254 × 1254:

| File | View | `references/3d/` (펠트) | `references/3d_smooth/` (매끈) | Use it for |
|---|---|---|---|---|
| `Front.png` | 정면 | ● | ● | default; the measurement baseline for this file |
| `Left_3Q.png` | 45도 측면 | ● | ● | any three-quarter turn |
| `Left_Profile.png` | 측면 | ● | ● | profile and near-profile |
| `Back.png` | 후면 | ● | ● | back and rear three-quarter; the clean-back proof |
| `Smile.png` | 정면 웃는얼굴 | ● | ● | open-mouth smile |
| `Sit.png` | 앉은자세 | ● | ● | sitting; the hind-sole pad reference |
| `Run.png` | 측면 뛰는자세 | ● | ● | walking, running, mid-stride |
| `Face.png` | 머리만 | — | ● | head-only close-up. **Shape reference only**: it is rendered glossy, which `styles/3D_Smooth.md` does not allow, so never use it as a material reference |

Felt and smooth sets show the same face; they differ only in material. Rotate one coherent character between views; never redesign per view.

**Higgsfield Elements do not match the current references.** `방실_3D` (`1173218c-…`) and `방실_3D_매끈` (`cdfcf687-…`) were registered from earlier images that carry whisker rods and brown features. Until they are re-registered from the current images, attach the matching current reference as a media input in **every** BANGSIL generation, front view included, and check every result for whiskers (section 9, item 9).

When sources disagree, apply this order:

1. The approved reference image closest to the requested view
2. This lock file
3. `styles/3D_Felt.md` or `styles/3D_Smooth.md`
4. The scene prompt

Do not replace a visible reference detail with a guessed measurement, a named shape, or an inferred colour. If a requested view exposes something none of the images show, keep the visible structure intact and say the detail is unverified rather than inventing it. There is **no front-palm reference**; a visible palm is unverified — follow the hind-sole layout in `Sit.png`. See section 4-1.

## 1. Non-negotiable identity and proportion

- BANGSIL is a compact, soft, upright cat mascot: a dominant head, a short rounded torso, short stubby limbs, and no visible neck.
- **The head is the biggest thing about the character.** Measured on `3d/Front.png`: the standing figure from ear tip to sole is **1136 px**, the chin sits at the **52 % mark** of that height, and the head is about **705 px wide** across the cheeks (the cheek tufts of section 5 excluded; with the upper tufts the silhouette reaches about 752 px). So the head fills the top half of the figure and its width is about **0.62 × the total height**.
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

BANGSIL's ears are **low, broad, soft triangles with rounded tips**, sitting on the upper outer corners of the head dome and leaning slightly outward. They are not tall, not upright, and not pointed. Measured on `3d/Front.png`:

| | Measured |
|---|---|
| Free height standing clear of the head dome | **about 0.12 × HW** (85 px against a 705 px head) |
| Base width : free height | **2.7 – 2.9 : 1** — far wider than tall |
| Width at 20 % down from the tip | **0.42 – 0.49 × the base width** |
| Width at 50 % down from the tip | 0.72 – 0.76 × the base width |
| Inner ear patch centre | ±0.33 HW from the face centre, 0.26 HW above the eye line |

- The tip is a **soft round curve, not a point.** One fifth of the way down from the tip the ear is already nearly half as wide as its base.
- The outer surface of **both** ears is the body colour. The inner ear is the point colour (section 6).
- Both ears match each other. Do not fold them and do not colour one differently.

**Failure measured 2026-11-09 — caused by an earlier wording of this section.** It once said "tall, pointed triangular ears standing upright… noticeably taller and sharper than MONGSIL's". Both validation renders came out as a fox: one with a needle tip (width at 20 % down 0.07), one twice too narrow (base : height 1.3 : 1). **Reject** when base : height falls below **2.2 : 1**, or when the width at 20 % down from the tip is under **0.35** of the base width.

**Ear shape is not a usable mixing check.** MONGSIL's ears have the same shape and stand about 0.08 × HW high; BANGSIL's stand a little higher. Use the face (section 10).

### All views

- Broad forehead, full cheeks, substantial lower face. The jaw is a wide soft curve, interrupted on each side only by the cheek tufts (section 5).
- **Expression may change; feature scale, feature spacing and feature colour may not.** The numbers below are the face.

### Face measurements — the numbers that stop the face deforming

Everything is expressed against **HW = the head's width across the cheeks, cheek tufts excluded**, measured in the same frame. Measured 2026-11-21 on `3d/Front.png`, `3d/Smile.png`, `3d/Sit.png`, `3d_smooth/Front.png`, `3d_smooth/Smile.png`, `3d_smooth/Sit.png`.

| | Measured | Accept |
|---|---|---|
| Eye width ÷ HW | **0.057 – 0.062** | 0.050 – 0.068 |
| Eye height ÷ width | 1.44 – 1.55 | taller than wide, 1.35 – 1.65 |
| Gap between eye centres ÷ HW (front view) | **0.212 – 0.224** | 0.19 – 0.24 |
| Nose centre, below the eye centre line | **+0.05 HW** — the top of the nose sits level with the bottom of the eyes | +0.03 – +0.07 HW |
| Nose width ÷ HW | 0.062 | 0.05 – 0.08 |
| W mouth width ÷ HW | **0.26** | 0.22 – 0.30 — the mouth is wide |
| Blush width ÷ HW | **about 0.21** | 0.18 – 0.25 |
| Blush centre, from face centre | ±0.24 – 0.25 HW | ±0.21 – 0.28 HW |
| Blush centre, below the eye centre line | +0.084 HW | +0.06 – +0.11 HW |
| Upper cheek tuft tip, below the eye centre line | +0.09 HW, standing about 0.04 HW clear of the cheek | — |
| Lower cheek tuft tip, below the eye centre line | +0.17 HW, standing about 0.025 HW clear of the cheek | — |

In pixels on `3d/Front.png`: eyes 43 × 63 px, centres 154 px apart, head 705 px.

**BANGSIL's eyes are large.** At about 0.06 HW they are roughly **1.6 × MONGSIL's** (0.036 – 0.039 HW) and sit **noticeably wider apart** (0.21 – 0.22 vs 0.157 HW in front view). Small, close-set eyes on BANGSIL mean MONGSIL's face leaked in.

### Measured feature colours — the current renders

| | Sampled on `3d/Front.png` | Spec |
|---|---|---|
| Eyes | `#090806` (darkest `#040000`) | `#000000` ✓ |
| Nose | `#151514` | `#000000` ✓ |
| W mouth line | `#151313` | `#000000` ✓ |

All three are neutral black. **Brown or reddish-brown eyes, nose or mouth line are an error** — most likely pulled in by the out-of-date Element (section 0).

### Profile rotation

Rotate the same broad head volume. Do not compress or carve away the lower face. In profile and three-quarter views the cheek tufts on the near side break the jaw line as two small soft points — see `Left_Profile.png` and `Left_3Q.png`.
**Reject** — and report it, regenerating only on the user's request — if the jaw or chin tapers to a point or the profile reads triangular.

### Eyes, nose, mouth — the flat face

- Two glossy black eyes, each a **vertical oval** (taller than wide), set wide apart. No highlight dot, no eyelashes, no eyebrows, no pupils. Size and spacing follow the table above.
- The nose is a small **rounded triangle**, point down, black, sitting directly on the face, centred, high — its top level with the bottom of the eyes.
- **BANGSIL's face is flat.** There are no raised white muzzle bumps under the nose. The nose sits on a smooth cheek surface.
- Directly below the nose there is a **drawn black mouth line: a wide W-shaped smile**, two soft curves meeting at the nose. The mouth line is always present in the default closed expression.
- In profile the same mouth reads as a single hook curving down and back from the nose — see `Left_Profile.png`.
- An open mouth is allowed when the user asks, or when matching `Smile.png` or `Run.png`: the W opens into a rounded smile with a pink tongue. **No teeth and no fangs, in any view, in any frame.**
- In video, an open or talking mouth is the most reliable way to make teeth appear. Unless the user asked for speech, lock the mouth closed for the whole clip rather than relying on a negative prompt.

## 3. Markings and left/right orientation

All directions use BANGSIL's anatomical left/right. In the front view, BANGSIL's left is the **screen right**.

### BANGSIL HAS NO BROWN. ANYWHERE.

- There is **no brown head patch, no brown ear, no brown arm marking, no brown tail, and no brown on the face.** Eyes, nose and mouth are black.
- BANGSIL is one solid body colour from head to feet, broken only by the point-colour elements in section 6 and the black facial features.
- `Back.png` is the proof image: a completely clean white back, clean arms, clean legs, clean tail.
- **Any brown on BANGSIL means MONGSIL's lock or the out-of-date Element leaked into the prompt.** Reject it and never retouch it — a mixed result is fixed by generating again from a clean prompt, which the user asks for.

### The only non-body colours on BANGSIL

Inner ears, blush, belly patch, paw pads — all the point colour. Eyes, nose, mouth line — black. Nothing else. There are no whiskers.

### Body has no markings

Apart from the belly patch, the body has **no markings at all**: no spots on the waist, sides, back, flanks, shoulders, or legs, in any colour. When a prompt uses the short scene format, carry the body-part enumeration verbatim — back, side, flank, shoulder, shoulder blade, rump, hip, waist, chest, belly, thigh, both arms, both forearms, both paws, both legs — and state that BANGSIL is **not** a calico or patched cat.

## 3-1. Tail — shape lock

The tail is the **same sculpt as MONGSIL's, in the body colour instead of brown.** Colour is the only difference; the geometry rules below are identical and are not optional.

### Geometry

- **ONE continuous padded mass** in the body colour, growing from the hip on BANGSIL's anatomical left (screen right in the front view).
- Standing, it rises and curls **outward and upward, away from the body**, and is **taller than it is wide — about 1.3–1.5 : 1.** Never squat, never as wide as tall.
- The whole tail is **ONE padded crescent — a fat comma.** The silhouette is continuous from base to tip and never pinches in to less than about **85 % of the local width** anywhere along it.
- Its **outer edge** (facing away from the body) is that same single curve, **gently scalloped** by **TWO shallow notches of unequal depth**. Measured against a 144 px tail: the **upper notch 10 px (≈ 7 %)**, the **lower notch 3 px (≈ 2 %)**. Quote them separately — one blanket figure makes the lower notch three times too deep. They are soft dimples in a continuous edge, not divisions.
- The three swells that the notches separate are **not equal and not round.** The top dome is the largest and most rounded; the two below it are progressively **smaller and flatter**, settling back into the curve toward the base.
- Its **inner edge** (facing the body) is **ONE long smooth unbroken curve** with no bumps and no notches. The asymmetry between the two edges is the signature of the shape.
- The **base** is a thick stalk merging smoothly into the hip. The tail never tapers to a point, never narrows to a stem, never detaches.

**Failure measured 2026-11-09.** An earlier wording said the outer edge "carries exactly THREE rounded forms stacked along it" and that the shape "reads like a fat upright clover leaf". The tail then rendered as **three near-equal spheres stacked like a snowman**. **Reject** when the lobes read as separate balls, when any two swells are the same size, when the inner edge grows bumps, or when a notch cuts deeper than about **15 %** of the tail's width.
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
- The belly patch is a **circle** in the point colour. Measured 2026-11-21 on `3d/Front.png`: 228 × 235 px (w/h 0.97). Render it as a circle, never an elongated oval.
- It is not a button, not a pocket, not a separate raised object. It follows the body surface and deforms only with perspective.
- It is centred on the belly, sits in the lower half of the torso, and its diameter is about **32 % of HW**.
- When clothing or a prop would cover the belly, keep at least part of the patch visible unless the user accepts it being hidden.

## 4-1. Paws — the three-lobed tip and the pads

This is the single most reliably broken detail. The failure is always the same: the three lobes dissolve and the paw comes out as one smooth club. Treat the lobes as a locked silhouette feature, not a surface detail.

### The three-lobed tip — every paw, every view

- **Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft grooves**, like a small clover leaf. The middle lobe is the largest and sits slightly forward.
- This is true of the front paws and the hind feet, and it is visible from **outside** even when the palm is not facing the camera. `Front.png` (front paws and standing feet) and `Sit.png` (front paws resting on the belly) show it.
- The grooves read as shallow creases running a short way back from the free edge. They are never smoothed away.
- **A smooth, undivided, club- or mitten-shaped paw tip is a failure.** Not a stylistic simplification — a failure.
- **A single digit pointing out from the paw is also a failure.** When BANGSIL points at something, the whole rounded paw tip touches or faces it; no finger extends (실측 2026-11-19, `prompts/2026-11-19-bangsil-felt-vet.md`).

### The pads — only when the inner face shows

- A **hind paw sole facing the viewer** carries one large central pad and **three** round toe pads in an arc above it — `Sit.png`, `Run.png`.
- **Three, not four.**
- Even with the inner face toward the camera, the outer edge of the paw still reads as the three lobes above. Pads and lobes are two separate facts; state both.
- A **front paw palm facing the viewer** carries the same layout. No current image shows it — follow the hind-sole layout in `Sit.png` and call it unverified.
- The back of a paw is plain body colour with no pads.
- Pad pink is **the same point colour as the inner ears, blush, and belly patch** — not a separate colour. Under 3D shading every pink area renders more saturated than the flat `#FFCBD1` spec (sampled 2026-11-21 on `3d/Front.png` & `3d/Sit.png`: blush `#FA9EA7`, inner ear `#EE7272`, belly `#F68A90`, hind pads `#FBADB0`). That gap is the render, not a different swatch. See the open item in section 6 before writing an exact pad HEX into a prompt.

### How to word it so the lobes survive

The lobes are usually destroyed by the prompt, not by the model's inability to draw them. Three rules, in order of importance:

1. **Describe the shape positively, never by negation.** Write `a three-lobed clover-shaped paw tip with two soft grooves`. Do **not** write `rounded nub`, `mitten`, `paddle`, or `simple rounded paw` — each of those is a club in the model's vocabulary.
2. **Keep every digit word out of the Subject and Pose sentences.** `no fingers`, `fingerless`, `without fingers` sitting next to the paw description is the most common cause of the club. If digits must be excluded at all, put `separated fingers, pointing finger, knuckles, claws, nails, human hand` in the **Negative block only**, far from the paw sentence.
3. **Name the grooves, not just the lobes.** The grooves are what the model drops first. `divided by two visible grooves` does more work than `three toe lobes`.

Add these to the Negative whenever a paw is visible:

```
smooth club paw, blank mitten paw, undivided paw tip, missing toe grooves,
fused toes, two toe lobes, four toe lobes, four toe pads
```

### Verification

Crop each visible paw, enlarge it, and confirm two things separately: the outer edge shows three lobes with two grooves, and — if the sole shows — one large pad plus exactly three toe pads. Check at magnification every time, and tell the user when a video cannot be frame-checked.

## 5. Cheek tufts — BANGSIL has no whiskers

BANGSIL has **no whiskers at all.** Instead:

- **Two soft fur tufts on each side of the face**, four in total, growing out of the lower cheek outline. They are part of the head silhouette, in the body colour and the body material — not separate objects, not lines, not rods.
- Each tuft is a small soft point sweeping outward and slightly down. The **upper tuft is the larger** (tip about 0.09 HW below the eye centre line, standing about 0.04 HW clear of the cheek); the **lower tuft is smaller** (tip about 0.17 HW below the eye line, about 0.025 HW clear).
- In the straight front view both pairs sit on the left and right outline of the head, below the blush, and widen the silhouette there (head 705 px across the cheeks, about 752 px across the upper tufts on `3d/Front.png`).
- In three-quarter and profile views the near-side pair breaks the jaw line as two small points (`Left_3Q.png`, `Left_Profile.png`); in `Back.png` they still show at the head's outline.
- They are soft and rounded at the tips, never spiky, never long hair strands, never a mane.

**Any whisker on BANGSIL — a rod, a drawn line, a printed or engraved stroke — is a failure.** Whisker rods belong to MONGSIL.

## 6. Palette lock

Keep these values as literal data. Do not replace codes with colour names, delete them during revisions, or invent missing codes from a rendered screenshot.

| Element | Locked value | Source |
|---|---|---|
| Inner ear | `#FFCBD1` | Figma variable `방_ear_inner` (그래픽소스) |
| Blush | `#FFCBD1` | same point colour |
| Belly patch | `#FFCBD1` | same point colour |
| Eyes, nose, mouth line | `#000000` | black family — the current renders match (section 2) |
| Cheek tufts | body colour | part of the head |
| Tail | body colour — identical to the torso | |
| Body | white / warm cream, as in the references | |

**`#FFCBD1` is BANGSIL's point colour and nothing else carries it.** MONGSIL's point colour is `#FFCDB4` and must never appear on BANGSIL. The two differ by only a few digits and look similar in a swatch — copy them, never retype from memory.

One open item, carried honestly rather than guessed:

- **Paw pads.** The references render them in the point-colour family, but no variable has been confirmed. Follow the reference colour and flag it as unverified if a scene depends on an exact pad value.

Lighting may create material shading, but it must not redefine the base palette.

## 7. Style separation

- This document defines identity, not rendering technique. Read `styles/3D_Felt.md` (default) or `styles/3D_Smooth.md` (매끈) for material, lighting, and rendering constraints.
- A different rendering treatment may not alter the locked silhouette, the absence of brown, the point colour, the belly-patch shape, the mouth line, or the cheek tufts — and may not add whiskers.

## 8. Allowed scene changes

Pose, expression, action, costume, prop, background, crop, camera, lighting, and atmosphere may change. If clothing or a prop hides a locked feature, do not move the feature to make it visible. A costume beard or mustache may hide the mouth line only when the user accepts it (승인 사례 `prompts/2026-11-19-bangsil-smooth-santa.md`, 4차).

## 9. Common generation failures — mandatory validation

Before delivery, compare against the closest reference view and reject a result with any of the following. **Report which item failed and what would fix it — do not regenerate on your own; the user asks for that** (CLAUDE.md 기본 이미지 생성 설정 4번):

1. **Any brown on the body or face** — head patch, ear, arm marking, tail, or brown eyes / nose / mouth line. BANGSIL has none.
2. **Raised muzzle bumps** under the nose. BANGSIL's face is flat.
3. **Missing mouth line** — the W smile under the nose is gone (unless a costume beard accepted by the user hides it).
4. **Fox ears:** an ear whose base is under 2.2 × its free height, or whose width 20 % down from the tip is under 0.35 of its base — a tall, narrow, or pointed ear. Also mismatched ears.
5. **Wrong point colour** — `#FFCDB4` (MONGSIL's) used on the ears, blush, belly, or pads instead of `#FFCBD1`.
6. **Triangular profile:** lower face crushed, narrowed, or pointed when rotated.
7. **Wrong head silhouette or size:** a sphere, a vertical oval, a narrow face, or a head that no longer fills the top half of the figure.
8. **Wrong belly patch:** an elongated oval, off-centre, a button, or not following the body surface, instead of a centred circle.
9. **Whiskers present, or cheek tufts wrong:** any whisker rod or line on the face — MONGSIL or the out-of-date Element leaking in; or the cheek tufts missing, more or fewer than two per side, or turned into long hair. Check this on **every** result until the Elements are re-registered.
10. **Teeth:** any tooth, fang, or tooth row, in a still or in any video frame.
11. **Palette drift / data loss:** a locked HEX removed, renamed without the code, or changed.
12. **Wrong body or limbs:** slim body, long waist, or arms and legs longer than the references; an arm stretched to reach a prop.
12-1. **Raised arm fused to the head:** a raised paw touching or overlapping the face so the silhouette reads as one shape there. Background must stay visible between the paw and the cheek at every height — but it can be a **thin sliver**, about 7 % of the paw's width. The failure is 0 px — one fused shape.
13. **Club paw:** any visible paw tip has lost its three rounded lobes and two grooves and reads as one smooth undivided club or mitten. This is the most frequent failure — check every paw in every frame.
13-1. **Missing or miscounted pads:** a sole **or a palm** faces the viewer without its pads, or shows four toe pads instead of three.
13-2. **Pointing finger:** a single digit extends from a paw (section 4-1).
14. **Hidden belly patch:** clothing or a prop covers the whole belly patch without the user accepting it.
15. **Deformed or invisible tail:** fails any of the five checks in section 3-1, or the white tail is not legible against the background. Watch for the **snowman tail** — three near-equal spheres stacked with deep pinches, instead of one continuous crescent with shallow unequal scallops.
16. **Unverified specificity:** a count, ratio, contour, or colour stated or generated as certain despite not being visible in the relevant reference.

## 10. BANGSIL and MONGSIL together

The two characters share a body and contradict each other on the face. Loading both locks into one prompt is how they get mixed.

**One lock per prompt.** For a solo BANGSIL scene, this file is the only character lock in the prompt. Never carry a sentence from MONGSIL's lock into a BANGSIL prompt, and never use any MONGSIL reference as a BANGSIL attachment.

### Where they differ

| | BANGSIL | MONGSIL |
|---|---|---|
| Point colour | `#FFCBD1` | `#FFCDB4` |
| Brown `#B79571` | none | head & ear wave, arm heart, tail |
| Eyes | **about 0.06 HW wide, 0.21 – 0.22 HW apart** | **0.037 HW wide, 0.157 HW apart** — about 1.6 × smaller |
| Whiskers | **none** — two soft cheek tufts per side instead | two raised rods per side |
| Muzzle | flat face | two raised white bumps |
| Closed mouth | black W-shaped mouth line | no mouth line at all |
| Ears | low broad rounded triangles, free height about 0.12 × HW | same shape, free height about 0.08 × HW |
| Tail | body colour | brown |
| Belly patch | circle, point colour | circle, point colour |

> **Eyes and whiskers are the strongest separators.** Eye size and spacing differ by about 1.6 × and 1.4 ×. Whisker rods on BANGSIL, or cheek tufts on MONGSIL, mean the faces mixed.
>
> **Ears are a weak separator.** Both characters have the same low broad round-tipped ear shape. Use the eyes, whiskers, muzzle, mouth line, brown, and point colour instead.

### Two-shot scenes

When both appear in one image, load both locks and state the separation explicitly — which character is on which side, and that each keeps its own face and colours. Then add the size rule:

> **MONGSIL's total height is 0.88 – 0.90 × BANGSIL's.** BANGSIL's ear tips sit clearly higher than MONGSIL's. Both stand on the same ground line.

Height ratio measured on a 두 캐릭터 비교 render **that is not stored in this repository**: BANGSIL 1166 px tall, MONGSIL 1021 px (**0.876**). The head-width ratio has not been measured against the current BANGSIL head. In solo frames each character fills its own canvas, so size only carries meaning when they share a frame.
