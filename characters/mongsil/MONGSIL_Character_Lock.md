# MONGSIL — CHARACTER IDENTITY LOCK

Rewritten 2026-11-09 against the re-rendered 9-view 3D reference sheet (Figma `기타 인쇄물` → `몽실_3D`).
Every proportion stated below was measured on those images, not recalled. Where a number appears, the view it was measured on is named.

**This file covers MONGSIL only.** BANGSIL has its own lock at `characters/bangsil/BANGSIL_Character_Lock.md`. The two characters share a body but contradict each other on face, markings, and point colour. Load **one** lock per prompt. For a two-shot, see section 10.

## 0. Purpose, reference set, and priority

This is the identity lock for every MONGSIL image. It fixes anatomy, markings, and palette. Pose, expression, props, costume, camera, and environment may change only when they do not alter that identity.

The approved reference set is `characters/mongsil/references/3d/`, all 1254 × 1254:

| File | View | Use it for |
|---|---|---|
| `Front.png` | 정면 | default; the measurement baseline for this file |
| `Left_3Q.png` | 45도 | any three-quarter turn |
| `Left_Profile.png` | 측면 | profile and near-profile |
| `Back.png` | 후면 | back and rear three-quarter |
| `Paw_Front.png` | 앞발 | a front palm facing the camera |
| `Paw_Hind.png` | 뒷발 | a hind sole facing the camera |
| `Sit.png` | 앉기 | sitting; also the approved open-mouth smile |
| `Tongue.png` | 메롱 | open-mouth / tongue expression |
| `Run.png` | 달리기 | walking, running, mid-stride, one foot lifted |

`Front.png`, `Left_3Q.png`, `Left_Profile.png`, `Back.png` are one coherent turnaround of the same model at the same camera distance. Rotate that one character between them; never redesign per view.

When sources disagree, apply this order:

1. The approved reference image closest to the requested view
2. This lock file
3. The applicable style guide
4. The scene prompt

Do not replace a visible reference detail with a guessed measurement, a named shape, or an inferred colour. If a requested view exposes something none of the nine images show, keep the visible structure intact and say the detail is unverified rather than inventing it.

## 1. Non-negotiable identity and proportion

- MONGSIL is a compact, soft, upright cat mascot: a dominant head, a short rounded torso, short stubby limbs, and no visible neck.
- **The head is the biggest thing about the character.** Measured on `Front.png`: the head (ears excluded) is about **692 px wide and 570 px tall**, and the whole standing figure from ear tip to sole is about **1065 px**. So the head alone is roughly **half the total height**, and the head is **wider than the torso** (torso ≈ 550 px at its widest).
- The head is **wider than it is tall — about 1.2 : 1**. It is a broad, softly rounded horizontal oval. Not a sphere, not a vertical oval, not a wedge, not a triangle.
- Keep the padded, chubby silhouette in every scene, including under clothing. The body never becomes slim, tall, or long-waisted.
- Arms and legs stay as short and stubby as in the turnaround. A raised, reaching, waving, or hugging arm keeps exactly the same short length. A pose never lengthens a limb.
- When both arms are raised, they open outward in a V **away from the face**, with clear space between each arm and the head. Arms must not press against the sides of the face.

### Reaching a prop without lengthening an arm

MONGSIL's arms are too short to reach many props. When a pose needs more reach, buy it from the **body**, never from the arm:

- Rise onto tiptoe, lean the torso forward, bend at the hip, stretch upward through the shoulders, or move MONGSIL physically closer to the prop.
- Or lower the prop so it falls inside the arm's real reach.
- **Reject and regenerate** any result where a forearm or upper arm is visibly longer or thinner than the turnaround, even if the pose otherwise reads correctly. A stretched arm is an identity failure, not a pose choice.

## 2. Head and face

### All views

- Broad forehead, full cheeks, substantial lower face. The jaw is a wide soft curve.
- Features sit small and low-centred inside that broad head. On `Front.png` the two eyes are about 115 px apart centre to centre inside a 692 px head — that is how small they read.
- Expression may change; head volume, feature scale, and feature spacing may not.

### Profile rotation

Rotate the same broad head volume. Do not compress or carve away the lower face.
**Reject and regenerate** if the jaw or chin tapers to a point, the lower face is crushed inward, or the profile reads triangular. The profile keeps rounded cheek and chin volume.

### Eyes, nose, muzzle

- Two small glossy black eyes, each a **vertical oval** (taller than wide), set wide apart. No highlight dot, no eyelashes, no eyebrows, no pupils.
- The nose is a small **rounded dark triangle**, point down, sitting at the top of the muzzle.
- The muzzle is **two round white puffy bumps side by side** below the nose, raised off the face.
- A short **vertical line runs from the nose down into the groove between the two bumps**. That line is the whole closed mouth.

### Mouth

- **The default closed mouth has no drawn mouth line.** It is the nose plus that vertical groove, nothing more. Do not add a W-mouth, a smile curve, or a cat-mouth line under the muzzle — the references do not have one.
- An open mouth is allowed only when the user asks, or when matching `Sit.png` / `Tongue.png`: a wide rounded opening under the muzzle with a soft pink tongue inside.
- MONGSIL has **no teeth and no fangs, in any view, in any frame.** No tooth, no fang, no tooth row, no white highlight inside the mouth.
- In video, an open or talking mouth is the most reliable way to make teeth appear. Unless the user asked for speech, lock the mouth closed for the whole clip rather than relying on a negative prompt.

## 3. Markings and left/right orientation

All directions use MONGSIL's anatomical left/right. In the front view, MONGSIL's left is the **screen right**. Camera movement never mirrors a marking.

### Brown head / ear marking

- The brown marking sits on MONGSIL's anatomical left head and ear: **screen right in `Front.png`, screen left in `Back.png`.**
- It covers the right half of the top of the head and **the entire outer surface of that ear**. The other ear is white outside. Both ears are peach inside.
- Its lower boundary against the white is a single smooth **wave** — it runs from near the centre of the forehead, dips, then sweeps down and out to the cheek. On `Front.png` the whole patch occupies about 370 × 315 px. Treat the wave contour as an identity feature, not a generic brown blob.
- Do not omit it, flatten it into a circle or block, split it, move it to the other ear, or mirror it.

### Arm marking — a heart

- One small brown **heart** sits on the **upper arm on the tail side** (screen right in the front view, the same side as the ear marking), high up near the shoulder, on the body-facing inner edge.
- It is a real heart: two rounded lobes on top, tapering to a point at the bottom. On `Front.png` it is about **51 × 86 px — clearly taller than wide**. Its left side runs along the arm's inner contour, so part of the left lobe is cut off by the silhouette.
- It is not a cloud, half-cloud, circle, dot, teardrop, stripe, or solid oval. *(Correction: earlier versions of this file described it as a half-cloud and explicitly banned a heart. The references have always shown a heart. The heart is correct.)*
- Show it when that inner arm edge is visible and the arm hangs free. **Omit it entirely** when the arm is raised, crossed, holding a prop, or turned so the edge is hidden. Relocating it to keep it visible is a failure; leaving it out is correct.
- It stays on the upper arm near the shoulder. It never moves to the waist, torso, armpit, forearm, paw, or the other arm.
- If the user drops it for a specific scene or costume, follow that for that scene and note it in the `prompts/` record. It does not change this lock.

### Body has no other markings

- Brown appears in exactly three places: the head-and-ear wave marking, the arm heart, and the tail.
- Apart from the belly patch, the body has **no markings at all**: no brown spots on the waist, sides, back, flanks, or legs. `Back.png` shows a completely clean white back.
- This failure recurs constantly. When a prompt uses the short scene format, carry the full body-part enumeration verbatim — back, side, flank, shoulder, shoulder blade, rump, hip, waist, chest, belly, thigh, both arms, both forearms, both paws, both legs — and state that MONGSIL is **not** a calico cat with scattered patches. Shortening this block brings the stray back patch straight back.

## 3-1. Tail — shape lock

Measured on `Front.png`, `Left_3Q.png`, `Left_Profile.png`, `Back.png`, `Sit.png`. This is the most frequently deformed part of the character. Do not write a tail description from memory; re-read this section and the nearest view every time.

### Geometry

- The tail is **ONE continuous padded mass** in brown, growing from the hip on MONGSIL's anatomical left (screen right in the front view), the same side as the ear marking.
- Standing, it rises and curls **outward and upward, away from the body**, and is **taller than it is wide**. Measured bounding boxes: `Front.png` 253 × 364 (**1.44 : 1**), `Left_3Q.png` 256 × 353 (1.38 : 1), `Left_Profile.png` 272 × 353 (1.30 : 1). Sitting, `Sit.png` reads 199 × 325 (1.63 : 1). Treat **about 1.3–1.5 : 1 standing** as the target. Never squat, never as wide as tall, never wider than tall.
- Its **outer edge** (facing away from the body) carries exactly **THREE rounded forms stacked along it**: a large rounded dome at the top, then **TWO more rounded bumps** below it, each separated by a soft shallow notch.
- Its **inner edge** (facing the body) is **ONE long smooth unbroken curve** with **no bumps and no notches at all**. The asymmetry between the two edges is the signature of the shape.
- The **base** is a thick stalk merging smoothly into the hip. The tail never tapers to a point, never narrows to a stem, never detaches.
- The whole form reads like a **fat upright clover leaf**, or a mitten with two thumbs down one side.
- In `Back.png` the same form simply swings out sideways — 326 × 364, nearly as wide as tall — with the three rounded forms along its upper-outer edge and the smooth edge sweeping down to the hip. When MONGSIL sits, it rotates the same way. **Rotation is allowed; reshaping is not.**

### Wordings that have caused failures — do not use

- "short and broad", "as wide as tall", "compact bunched mass" → squat blob
- "a few lobes overlapping side by side" → beads in a row
- "bumps along its free edge" without the height ratio → caterpillar
- "cloud", "fluffy", "puffy" used alone → separated puffs or a smooth paddle
- any wording that does not state **upright, taller than wide, three forms on the outer edge only, smooth inner edge**

### Mandatory verification before delivery

Crop the tail out of the result, enlarge it, and set it beside the same region of the nearest approved view. Confirm all four:

1. Height is visibly greater than width (about 1.3–1.5 : 1 standing).
2. The outer edge has a top dome plus exactly two more bumps — not one, not three, not a row of equal beads.
3. The inner edge is a single smooth curve with no bumps.
4. The mass is continuous and joins the hip with a thick base.

Any failure means regenerate. Do not deliver a tail that was not compared at magnification.

## 4. Body and belly patch

- Keep the torso short, rounded, and compact beneath any clothing.
- The belly patch is a soft salmon-pink **circle**. Measured on `Front.png` it is 209 × 221 px, on `Tongue.png` 210 × 209, on `Sit.png` 208 × 201 — **within a few percent of 1 : 1 in every frontal view.** Render it as a circle. *(Correction: earlier versions of this file called it a slight vertical oval. The references do not support that; it is a circle.)*
- It is not an elongated oval in either direction, not a button, not a pocket, not a separate raised object. It follows the body surface and deforms only with perspective.
- It is centred on the belly and sits in the lower half of the torso. Its diameter is roughly **38 % of the torso width**. Do not move it off-centre to compensate for a turned body.
- When clothing or a prop would cover the belly, keep at least part of the patch visible (an open vest, a short top, a prop held low) unless the user accepts it being hidden. A result where the belly patch silently disappears is a failure.

## 4-1. Paws — the three-lobed tip and the pads

This is the single most reliably broken detail. The failure is always the same: the three lobes dissolve and the paw comes out as one smooth club. Treat the lobes as a locked silhouette feature, not a surface detail.

### The three-lobed tip — every paw, every view

- **Every paw tip is scalloped into THREE rounded toe lobes divided by TWO soft grooves**, like a small clover leaf. The middle lobe is the largest and sits slightly forward.
- This is true of the front paws and the hind feet, and it is visible from **outside** even when the palm is not facing the camera. `Front.png` (standing feet), `Sit.png` (front paws resting on the belly) and `Left_Profile.png` all show it.
- The grooves read as shallow creases running a short way back from the free edge. They are never smoothed away.
- **A smooth, undivided, club- or mitten-shaped paw tip is a failure.** Not a stylistic simplification — a failure.

### The pads — only when the inner face shows

- A **front paw palm facing the viewer** carries one large **bean-shaped** central pad and **three** round toe pads in an arc above it — `Paw_Front.png`.
- A **hind paw sole facing the viewer** carries one large **oval** central pad and **three** toe pads — `Paw_Hind.png`, `Sit.png`, `Run.png`.
- **Three, not four.** All of those references show three.
- Even with the inner face toward the camera, the outer edge of the paw still reads as the three lobes above. Pads and lobes are two separate facts; state both.
- The back of a paw is plain white with no pads.
- Pad pink follows the reference. See the open item in section 6 before writing an exact pad HEX into a prompt.

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

Crop each visible paw, enlarge it, and confirm two things separately: the outer edge shows three lobes with two grooves, and — if the inner face shows — one large pad plus exactly three toe pads. The pad count has failed in generation even with the Element, an explicit number and a negative (measured three times), and the lobes fail more often still. Check at magnification every time, and tell the user when a video cannot be frame-checked.

## 5. Whiskers

- **Two whiskers per side, four in total.** Verified on `Front.png`, `Left_3Q.png`, `Left_Profile.png`, `Tongue.png`, `Sit.png`. Not three, not six. *(Earlier versions of this file refused to state a count because it was unverified. It is now verified: two.)*
- They are **thin, softly curved, raised 3D rods** — dark, rounded in section, with a clear shadow under them. They are not printed lines, grooves, or flat black marks.
- Each pair attaches at the cheek **just outside the blush**, and sweeps outward and slightly upward. The upper whisker is longer and flatter; the lower one angles down a little more.
- **In the straight front view the whiskers stay inside the head silhouette**, lying across the cheek — on `Front.png` they span roughly x 310–480 and x 735–915 inside a head that runs x 263–955. At turned angles such as `Left_3Q.png` the near-side pair crosses the silhouette and reads free-standing in space. Both are correct; follow the view.
- Do not make them thick, rigid, perfectly straight, embedded flush in the face, or detached from the cheek.

## 6. Palette lock and colour-data handling

Keep approved HEX values as literal data. Do not replace codes with colour names, delete them during revisions, or invent missing codes from a rendered screenshot.

### Locked base values

| Element | Locked value | Source |
|---|---|---|
| Brown — head & ear wave, arm heart, tail | `#B79571` | Figma variable `몽_pattern_brown` (그래픽소스) |
| Inner ear | `#FFCDB4` | Figma variable `몽_ear_inner` (그래픽소스) |
| Blush | `#FFCDB4` | same point colour |
| Belly patch | `#FFCDB4` | same point colour |
| Eyes, whiskers, nose | `#000000` | black family |
| Body | white / warm cream, as in the references | |

**`#FFCDB4` is MONGSIL's point colour and nothing else carries it.** BANGSIL's point colour is `#FFCBD1` and must never appear on MONGSIL. The two differ by only a few digits and look similar in a swatch — copy them, never retype from memory.

### Measured from the 2026-11-09 renders — reference only, not base values

These are **lit pixel samples**, useful for matching a render or picking a colour in a design tool. They are not substitutes for the locked values above and must not be written into a prompt as base colours.

| Element | Sampled | Where |
|---|---|---|
| Brown, lit top surface | `#CA9E7E` | head patch, `Front.png` |
| Brown, shadowed side | `#B78866` | tail, `Front.png` |
| Body white | `#E9DDDC` | torso, `Front.png` |
| Inner ear | `#FCC5B1` | `Front.png` |
| Belly patch | `#FDBFB8` | `Front.png` |
| Paw pads | `#F8B1A4` | `Paw_Front.png` |
| Blush | `#FBBCBE` | `Front.png` |
| Eye | `#282726` | `Front.png` |
| Tongue | `#D56E7D` | `Tongue.png` |

One open item, carried honestly rather than guessed: **paw pads.** The references render them in the point-colour family but no variable has been confirmed, and the lit sample sits further from the inner-ear value than the belly patch does. Follow the reference colour and flag it as unverified if a scene depends on an exact pad value.

Lighting may create material shading, but it must not redefine the base palette.

## 7. Style separation

- This document defines identity, not rendering technique.
- Read `styles/3D_Felt.md` for 3D material, lighting, and rendering constraints.
- 2D and 3D may differ in rendering treatment, but may not alter the locked silhouette, marking anatomy, orientation, palette data, belly-patch shape, or whisker count and attachment.
- BANGSIL's lock never applies here. A sentence about a flat face, a W mouth line, pointed ears, or `#FFCBD1` does not belong in a MONGSIL prompt.

## 8. Allowed scene changes

Pose, expression, action, costume, prop, background, crop, camera, lighting, and atmosphere may change. If clothing or a prop hides a locked marking, do not move the marking to make it visible.

## 9. Common generation failures — mandatory validation

Before delivery, compare against the closest reference view and reject/regenerate a result with any of the following:

1. **Triangular profile:** lower face crushed, narrowed, or pointed when rotated.
2. **Wrong head silhouette:** a sphere, a vertical oval, or a narrow face instead of a broad oval about 1.2 : 1 wide.
3. **Wrong head size:** the head is no longer about half the total height, or is narrower than the torso.
4. **Lost ear marking:** the front-view screen-right brown wave is absent, simplified into a block, disconnected, distorted, or mirrored; or the brown ear is not fully brown on its outer surface.
5. **Wrong belly patch:** an elongated oval in either direction, an off-centre patch, a button, or a patch that does not follow the body surface, instead of a centred circle.
6. **Embedded whiskers, or the wrong count:** whiskers painted flat into the face, or any number other than two per side.
7. **Wrong mouth:** a drawn mouth line, smile curve, or W-mouth added to the default closed mouth; or any tooth or fang, in a still or in any video frame.
8. **Palette drift / data loss:** a locked HEX removed, renamed without the code, or changed. In particular, BANGSIL's `#FFCBD1` used on the ears, blush, or belly instead of `#FFCDB4`.
9. **Unverified specificity:** a count, ratio, contour, colour, or anatomical detail stated or generated as certain despite not being visible in the relevant reference.
10. **Wrong body or limbs:** slim body, long waist, or arms and legs longer than the turnaround; raised arms pressed against the face; an arm stretched to reach a prop instead of the body leaning or rising on tiptoe.
11. **Wrong markings:** the arm mark rendered as a cloud, dot, or solid oval instead of a heart; placed on the outer arm, forearm, armpit, or wrong arm; relocated to keep it visible; or any extra brown spot on the body.
12. **Club paw:** any visible paw tip has lost its three rounded lobes and two grooves and reads as one smooth undivided club or mitten. This is the most frequent failure — check every paw in every frame.
12-1. **Missing or miscounted pads:** a palm or sole faces the viewer without its pink pads, or shows four toe pads instead of three.
13. **Hidden belly patch:** clothing or a prop covers the whole belly patch without the user accepting it.
14. **Deformed tail:** fails any of the four checks in section 3-1 — squat instead of upright, bumps on the inner edge, a row of equal beads, a smooth paddle, a tapered or detached tail. Verify at magnification; this one is not reliably caught at full-frame size.

## 10. MONGSIL and BANGSIL together

The two characters share a body and contradict each other on the face. Loading both locks into one prompt is how they get mixed.

**One lock per prompt.** For a solo MONGSIL scene, this file is the only character lock in the prompt. Never carry a sentence from BANGSIL's lock into a MONGSIL prompt, and never use a BANGSIL reference as a MONGSIL attachment.

### Where they differ

| | MONGSIL | BANGSIL |
|---|---|---|
| Point colour | `#FFCDB4` | `#FFCBD1` |
| Brown `#B79571` | head & ear wave, arm heart, tail | none |
| Ears | shorter rounded triangles | tall pointed triangles |
| Muzzle | two raised white bumps | flat face |
| Closed mouth | no mouth line at all | W-shaped mouth line |
| Tail | brown | body colour |
| Whiskers | 2 per side | 2 per side |
| Belly patch | circle, point colour | circle, point colour |

### Two-shot scenes

When both appear in one image, load both locks and state the separation explicitly — which character is on which side, and that each keeps its own face and colours. Then add the size rule:

> **MONGSIL's total height is 0.9 × BANGSIL's.** BANGSIL's ear tips sit clearly higher than MONGSIL's. Both stand on the same ground line.

Measured on the 2026-11-09 두 캐릭터 비교 render: BANGSIL 1166 px tall, MONGSIL 1021 px, head widths 724 px and 652 px — a consistent 10 % difference, with BANGSIL's taller ears adding the rest. In solo frames each character fills its own canvas, so size only carries meaning when they share a frame.

## 11. Generation workflow

0. Read `prompts/` first. The approved compact prompt format and the record of what has already failed live there, not in this file.
1. Identify the requested style and camera angle.
2. Open this lock, the relevant style guide, and the nearest reference view from the table in section 0.
3. Separate fixed identity from requested scene changes.
4. Generate without mirroring or redesigning locked features.
5. Run the section 9 checklist, paying special attention to profile shape, the screen-right ear wave in front view, the belly circle, the whisker count, literal HEX preservation, and the section 3-1 tail comparison at magnification.
6. If a required detail is unverified, defer to the reference or flag it; do not fill the gap with a guess.
7. Build a scene in stages instead of one prompt: costume & prop first on a plain background, then scene & action, then cutout & layout. See `templates/mongsil-scene.md` section 7.
8. Do not keep re-editing the same generated image. Each extra edit degrades quality and drifts the shape. Allow at most one edit of a result; after that, generate fresh from the references. Fix small edges and seams in the design tool instead of regenerating.
9. A petf prop needs its Element **and** its reference sheet attached as a media input. The Element alone gets reinterpreted into a generic object.
10. State plainly when a result could not be verified — in particular, video frames cannot be checked without `ffmpeg`, so the gait, pads, teeth, and tail in a clip stay unverified until the user looks at them.
