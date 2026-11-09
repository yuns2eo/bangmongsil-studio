# 3D FELT STYLE — MONGSIL & BANGSIL 공통

Read the character's own lock first — `characters/mongsil/MONGSIL_Character_Lock.md` or `characters/bangsil/BANGSIL_Character_Lock.md`. The lock file and that character's reference images override this guide whenever there is a conflict.

This file controls **only 3D rendering**: material, lighting, and how forms are built. It is shared by both characters and must not define anatomy, markings, left/right orientation, or palette — those live in each character's lock, and the two characters disagree on them.

## 1. Reference use

Use the nearest reference view for the requested angle from **that character's own** reference folder. Never attach one character's reference to the other's prompt. Rotate one coherent 3D character between views; do not use the text below to override a visible contour, colour, or detail in a reference.

## 2. Material

- Soft flocked felt / velvety plush surface.
- Very short, dense, even matte pile. A fine embossed squiggle-and-loop grain is visible across the whole surface at close range; it is a texture in the material, never a printed pattern.
- Soft padded forms with clean, controlled marking boundaries.
- No long fur, individual hairs, yarn, fabric seams, stitching, hard plastic, glossy vinyl, clay sheen, glass, or metal surface.
- Coloured markings and patches are integrated surface colour, not stickers, pockets, or raised buttons.
- The only parts that read as raised relief are the paw pads, the nose, and — on MONGSIL only — the two muzzle bumps. Everything else is flush with the surface.
- Whiskers are the exception: thin raised 3D rods with a soft shadow under them, never engraved or printed flat.

## 3. Form

- Preserve the broad head and its full cheek and lower-face volume in every view. Both characters carry the head at roughly half the total figure height.
- In profile, the head stays rounded and substantial. Never pinch, flatten, or taper the lower face into a triangle.
- Facial features stay small and reference-consistent. No anime eyes, eyelashes, eyebrows, teeth, or human-like face.
- Eyes are glossy black vertical ovals with no highlight dot, on both characters.
- Keep the padded, chubby silhouette and the short stubby limbs under any clothing.

Anything more specific than this — ear shape, muzzle, mouth line, markings, tail colour, point colour — is character identity. Take it from the lock, not from here.

## 4. Lighting and background

- Soft, even studio lighting with a gentle contact shadow on a pale warm floor, and restrained depth of field when appropriate.
- Scene lighting may create mild natural shading, but the body must still read as its approved base colour and every locked marking as its locked value. Do not recolour a character for atmosphere.
- A white or cream character on a pale background loses its silhouette easily. Keep enough separation that the body outline and the tail stay readable — this matters most for BANGSIL, whose tail is body-coloured.

## 5. Colour handling

- Preserve the literal locked colour data from the character's own lock. Never carry a HEX from one character into the other's prompt: MONGSIL's point colour is `#FFCDB4`, BANGSIL's is `#FFCBD1`, and only MONGSIL has brown `#B79571`.
- Do not invent a HEX from a rendered screenshot. Each lock's section 6 lists measured render samples separately from the base values, and names the values that are still unverified.

## 6. Rendering exclusions

Do not use this style for a flat 2D illustration, sticker, line drawing, colouring page, or an unapproved materially different character treatment. Use the relevant 2D guide when available — there isn't one yet, so ask the user first.

## 7. 3D delivery check

Confirm before delivery, in addition to the character's own section 9 checklist:

1. The surface reads as short dense matte felt with the fine embossed grain — no long fur, no plastic or vinyl sheen, no visible seams or stitching.
2. The profile has a broad, rounded lower face — not a triangle.
3. The head fills roughly the top half of the figure.
4. Whiskers are raised rods with a shadow, not engraved lines.
5. The silhouette, including the tail, is readable against the background.
6. Known HEX codes remain literal, and no colour from the other character appears anywhere.
