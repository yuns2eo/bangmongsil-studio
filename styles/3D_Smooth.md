# 3D SMOOTH STYLE — MONGSIL & BANGSIL 공통

Read the character's own lock first — `characters/mongsil/MONGSIL_Character_Lock.md` or `characters/bangsil/BANGSIL_Character_Lock.md`. The lock file and that character's reference images override this guide whenever there is a conflict.

This is the **smooth-material counterpart of `styles/3D_Felt.md`**. Everything in the felt guide still applies except section 2 (material) and the material line of the delivery check. Use this file only when the user asks for the 매끈한 재질 version; the felt version remains the default.

## 1. Reference use

Use that character's own `references/3d_smooth/` folder, not `references/3d/`.

| 폴더 | 몽실 | 방실 |
|---|---|---|
| `references/3d_smooth/` | Front / Left_3Q / Left_Profile / Back / Run / Sit / Tongue / Face | Front / Left_3Q / Left_Profile / Back / Run / Sit / Smile / Face |

`Face.png` is a head-only close-up (added by the user 2026-11-21). Use it for face-detail and head-only shots.

Felt and smooth references must not be mixed in one prompt. If a pose exists only in felt (for example MONGSIL `Paw_Front` & `Paw_Hind`), attach the felt image only as a shape reference and state that the material must stay smooth.

## 2. Material

- Smooth, clean, soft matte vinyl / soft-touch clay surface.
- No felt pile, no embossed grain, no fur, no fuzz, no fibres.
- Very soft satin response to light: broad gentle highlights only. No mirror gloss, no wet look, no glass, no metal.
- Coloured markings and patches are integrated surface colour with clean edges, not stickers.
- Raised relief is the same as in felt: paw pads, nose, MONGSIL's two muzzle bumps, and whiskers as raised rods.
- Paw tips keep the three lobes with two **shallow** grooves. Smooth material makes them easy to lose — the paw must not become a plain club, and the grooves must not be cut deep either. BANGSIL `Sit.png` & `Run.png` in `3d_smooth/` are the depth standard for both characters.

## 3. How the smooth references were made (2026-11-19)

- 정면 & 45도 & 측면 & 후면: Figma 매끈 라인업(몽실 `9550:23212`, 방실 `9550:23222`)을 한 장씩 쪼개 정방형 중앙 배치.
- 포즈(Run & Sit & Tongue & Smile & Wave): 펠트 원본 `references/3d/`를 ChatGPT에 주고 **재질만** 바꿔 달라고 했다. 몽실 Sit는 발 마디 문제로 여러 번 실패했고, 펠트 원본 + 매끈 정면을 같이 주고 재질만 바꾼 버전이 채택됐다. 발을 따로 합성하는 방법은 사용자가 반려했다.

## 4. 3D delivery check (smooth)

`styles/3D_Felt.md` 7번 항목을 그대로 보되 1번만 아래로 바꾼다.

1. The surface reads as smooth soft matte vinyl / clay — no felt grain, no fur, no hard mirror gloss.

추가로:

7. Paw tips still show three lobes with shallow grooves in every visible paw.
