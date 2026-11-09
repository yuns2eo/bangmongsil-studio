# 템플릿: 캐릭터 장면 (Scene)

몽실이와 방실이 이미지 프롬프트는 둘 다 이 골격으로 만든다. 이 파일에는 **캐릭터와 무관한 골격과 워크플로만** 있다.

캐릭터 정체성 문장(`## Subject`, `## Critical conditions`, `## Negative`)은 캐릭터 폴더에서 가져온다.

| 캐릭터 | 락 | 장면 블록 | 레퍼런스 |
|---|---|---|---|
| 몽실이 | `characters/mongsil/MONGSIL_Character_Lock.md` | `characters/mongsil/scene-blocks.md` | `characters/mongsil/references/3d/` |
| 방실이 | `characters/bangsil/BANGSIL_Character_Lock.md` | `characters/bangsil/scene-blocks.md` | `characters/bangsil/references/3d/` |

**한 프롬프트에는 한 캐릭터의 블록만 넣는다.** 두 캐릭터는 몸은 같고 얼굴과 포인트 컬러가 정반대라, 블록을 같이 넣으면 섞인다. 투샷은 각 락 10번을 따른다.

3D 렌더 규칙은 `styles/3D_Felt.md`에 있다. 이 템플릿은 규칙을 **프롬프트 문장으로 옮기는 방법**만 정한다. 락 & 스타일 내용과 충돌하면 락 & 스타일이 이긴다.

---

## 1. 블록 선택표

장면에 필요한 블록만 넣는다. 필수 블록은 항상 넣는다.

| 블록 | 넣는 경우 | 필수 |
|---|---|---|
| Element 줄 | 항상 | ● |
| `## Subject` | 항상 | ● |
| `## Orientation` | 항상 (정면 기본 자세라도 한 줄은 쓴다) | ● |
| `## Pose & Paws` | 팔이나 다리가 기본 자세와 다를 때, 앞발로 무언가 할 때 | |
| `## Prop` | 소품이 있을 때 | |
| `## Wardrobe` | 모자, 옷, 액세서리가 있을 때 | |
| `## Environment` | 흰 배경이 아닐 때 | |
| `## Camera` | 항상 | ● |
| `## Style` | 항상 (3D는 아래 문장 그대로) | ● |
| `## Critical conditions` | 항상 | ● |
| `## Negative` | 항상 | ● |

빈 블록은 지운다. "없음"이라고 쓰지 않는다.

---

## 2. 프롬프트 골격

```
<<<캐릭터 Element ID>>> <<<소품 Element ID (있을 때만)>>> # {장면 제목}

## Subject
{해당 캐릭터 scene-blocks.md의 Subject 블록을 그대로 붙여넣는다. 바꾸는 것은 {표정}뿐이다.}

## Orientation
- Body faces: {몸 방향, 예: three-quarter toward screen left}
- Head faces: {머리 방향, 예: turned slightly more toward the camera than the body}
- Eyes look at: {시선 대상, 예: the gift box / the camera / off to screen right}
The head turns on the body naturally with no visible neck. The face, ears, and all markings rotate with the head; markings stay on the character's anatomical left side and never mirror.

## Pose & Paws
{자세 1~2문장. 팔 방향은 신체 기준과 화면 기준을 둘 다 쓴다.
예: its left arm (screen right) reaches forward; its right arm (screen left) rests at its side.}
{앞발과 소품의 접촉 방식 — 아래 4번 참고}
{발이 보이면 해당 캐릭터 scene-blocks.md의 `## Paws` 블록을 여기에 그대로 붙인다. 이 문장 근처에 `no fingers` 같은 부정어를 쓰지 않는다.}

## Prop
{소품 이름}: {형태, 색, 재질}. {소품 방향, 예: long side horizontal, the notch facing screen right}.
Size: {캐릭터 머리와 비교한 크기, 예: about half the width of the character's head}.
The prop keeps exactly this shape and orientation{소품 Element가 있으면: as in the prop reference}. Nothing is printed on it unless stated.

## Wardrobe
{의상 & 액세서리}. It sits on top of the character without changing the head shape, ears, or body volume, and does not cover a locked marking unless stated.

## Environment
{배경. 기본: clean light gray to white seamless studio background with a soft contact shadow.}

## Camera
{정면 & 3/4 & 측면 & 후면} view, eye level, {full body / waist up}, centred, nothing cropped.

## Style
Soft flocked felt 3D mascot figure with a very short, dense, even matte pile. Soft even studio lighting, gentle contact shadow. No long fur, no individual hairs, no seams or stitching, no glossy plastic or vinyl.

## Critical conditions (must all hold)
{해당 캐릭터 scene-blocks.md의 Critical conditions 9개를 그대로 붙여넣는다}
{10~. 이번 장면 고유 조건 — 소품 방향, 시선 대상, 앞발 접촉, 앞 물체 깊이 등}

## Negative
{해당 캐릭터 scene-blocks.md의 Negative} + {장면 고유 Negative}
```

---

## 3. 시선 & 몸 방향 쓰는 법

- 몸 방향, 머리 방향, 시선 대상을 **따로 한 줄씩** 쓴다. 한 문장에 섞으면 모델이 전부 정면으로 맞춘다.
- "앞 & 뒤 & 왼쪽 & 오른쪽"은 신체 기준인지 화면 기준인지 항상 밝힌다. 둘 다 쓰는 게 가장 안전하다.
  - 실측: "팔을 앞뒤로" 지시가 2회 연속 반대로 나왔다 (`prompts/2026-10-01-mongsil-3d-walk-paw-pads.md`)
  - 이 기록들은 몽실이로 확인한 것이지만 몸이 같으므로 방실이에도 그대로 적용된다
- 몸이 측면인데 얼굴만 정면으로 고정되는 실패가 있었다 (`prompts/2026-09-30-higgsfield-element-failures.md`). 몸과 머리를 다르게 원하면 각도 차이를 명시하고, 같게 원하면 "head and body face the same direction"을 쓴다.

## 4. 앞발 & 소품 상호작용

| 상호작용 | 문장 예시 |
|---|---|
| 두 손으로 들기 | holds the {prop} in front of its chest with both rounded paws pressed against the left and right sides of the {prop} |
| 한 손으로 들기 | holds the {prop} with its {left/right} paw (screen {right/left}); the paw wraps around the edge |
| 끌어안기 | hugs the {prop} against its belly with both short arms; the paws rest on the front of the {prop} |
| 내밀기 | holds the {prop} out toward the camera at chest height with both paws underneath it |
| 누르기 & 터치 | touches the {prop} with the round tip of its {left/right} paw |

- 소품은 반드시 앞발에 **닿아 있게** 쓴다. 떠 있거나 몸에 붙어 있으면 안 된다.
- 소품이 배 패치를 다 가리면 배 패치 검증을 할 수 없다. 가려도 되는 장면이 아니면 "held low enough that part of the belly patch stays visible"을 넣는다.
- 손바닥이 카메라를 향하는 자세(손 흔들기, 하이파이브, 만세)는 **사용자가 따로 말하지 않아도** 손바닥 패드 문장을 넣는다: `the palm facing the viewer has soft pink paw pads: one large central pad and exactly three small round toe pads above it`. 이 문장을 빼먹어 패드 없이 나온 사례가 있다 (`prompts/2026-10-22-staged-scenes.md`, 택배기사).
- **발가락 패드는 3개다.** 이전 템플릿에 4개로 적혀 있었다 (2026-11-09 레퍼런스 실측으로 정정).
- 몽실이는 손바닥 젤리가 보여야 하면 `mongsil_3d_paw_front_v1`을, 발바닥이면 `mongsil_3d_paw_hind_v1`을 소품 Element로 추가한다. 단, 앞발 젤리 개수는 Element & 숫자 지정 & Negative로도 보장되지 않았다 (실측 3회). 젤리가 중요한 컷이면 생성 전에 이 한계를 사용자에게 알린다.
- 방실이는 앞발 손바닥 레퍼런스도 Element도 없다. 손바닥이 보여야 하면 뒷발 패드 구성을 쓰고 미검증임을 알린다.

## 5. 소품 형태 & 방향 유지

- 소품 Element가 있으면 Element 줄에 넣고, `## Prop`에도 형태를 글로 다시 쓴다 (Element + 글 이중 안전장치).
- 방향은 화면 기준으로 쓴다: 긴 변 가로 & 세로, 홈 & 절취선 위치, 기울기.
- 크기는 캐릭터 머리와 비교해서 쓴다. 숫자 cm 단위는 쓰지 않는다.
- 소품에 글자가 필요하면 `"..." rendered sharp, crisp, and clearly legible`. 필요 없으면 Negative에 `text on prop`.

## 6. 레퍼런스 & Element 조합

- 캐릭터 Element는 **1개만** 쓴다. 같은 캐릭터 Element를 여러 개 넣으면 여러 마리로 나온다.
- 캐릭터 1개 + 소품 Element 추가는 다중 캐릭터 문제를 만들지 않았다 (실측 2회).
- `몽실_3D` & `방실_3D`는 4장(정면 & 45도 & 측면 & 후면)으로 등록돼 있지만 **생성 때 몇 장이 주입되는지는 아직 측정 전이다.** 정면이 아닌 구도는 안전하게 해당 캐릭터 폴더의 `references/3d/`에서 그 각도 이미지를 `medias`로 함께 넣는다.
- 다른 캐릭터의 레퍼런스를 첨부하지 않는다. 몽실 장면에 방실 이미지를 넣는 순간 얼굴이 섞인다.
- 기존 결과를 고칠 때 그 결과를 편집 기준 이미지로 넣는 건 **1회까지만** 한다. 1회 편집은 정체성 & 배경 & 질감이 잘 유지됐다 (실측 4회).
- 같은 결과를 2회 이상 이어서 편집하면 화질이 깨지고 형태가 틀어진다. 두 번째 수정부터는 원본 레퍼런스로 **새로 생성**하고, 작은 경계 & 이음새 정리는 생성하지 말고 Figma에서 처리한다 (`prompts/2026-10-22-staged-scenes.md`, 만세 & 수의사 장면 2건).

### 경로 B 변환 (ChatGPT로 돌릴 때)

`<<<ID>>>`는 힉스필드 전용 문법이라 ChatGPT에서는 아무 의미가 없다. 그 자리를 **실제 첨부 + 문장**으로 바꾼다.

| 힉스필드 | ChatGPT |
|---|---|
| 캐릭터 `<<<ID>>>` | `references/3d/Front.png` 첨부 + `The character is exactly the attached reference: same face, markings, proportions, and colors.` |
| 정면이 아닌 구도 | 그 각도 파일(`Left_3Q.png` 등)을 **추가로** 첨부 |
| 소품 `<<<ID>>>` | `assets/props/`의 같은 이름 PNG 첨부 + `The prop is exactly the attached reference: same shape, silhouette, proportions, parts, and every engraved mark.` |
| 패드 Element | `assets/props/detail/` 해당 PNG 첨부 |

- 첨부 순서는 **캐릭터 먼저, 소품 나중**. 섞이면 소품 색이 캐릭터로 넘어온다
- 첨부가 5장을 넘으면 캐릭터가 흐려진다. 장면을 쪼개서 STEP을 하나 더 만든다
- `## Subject` & `## Critical conditions` & `## Negative`는 그대로 쓴다. 캐릭터 정의는 경로가 달라져도 바뀌지 않는다
- 기존 이미지를 고치는 프롬프트면 바꿀 것만 번호로 나열하고 나머지는 `Keep EVERYTHING identical`로 고정한다
- 소품 PNG 배경이 검정인 것들이 있다. 결과에 검정 테두리나 어두운 반사가 묻어나는지 확인한다 (`assets/props/README.md`)

---

## 7. 단계별 생성 (기본 순서)

한 프롬프트에 의상 & 소품 & 장면 & 행동을 다 넣으면 얼굴과 비율이 쉽게 흐트러진다. 캐릭터 장면은 항상 아래 순서로 만든다.

| 단계 | 하는 일 | 배경 |
|---|---|---|
| 0. 분리 | 고정할 것(몽실 정체성, 레이아웃, 브랜드 컬러)과 바뀌는 것(의상, 소품, 자세, 장소)을 먼저 나눈다 | |
| STEP 1 의상 & 소품 | 의상과 소품만 입힌 캐릭터를 만들어 캐릭터 규칙부터 확인한다 | 단색 `#E4DFE3` |
| STEP 2 장면 & 행동 | STEP 1 결과를 `medias` 참조로 넣고 행동과 앞쪽 물체를 더한다 | 누끼용 단색, 또는 장면 배경 |
| STEP 3 분리 & 합성 | 캐릭터 누끼와 배경을 따로 만들어 Figma에서 규격별로 배치한다 | |
| (선택) 모션 | 확정된 장면 이미지를 시작 프레임으로 짧은 모션을 만든다 | |

- 각 단계 결과를 사용자에게 보여주고 다음 단계로 넘어간다. 단계를 건너뛰지 않는다.
- STEP 1이 실패하면 STEP 2로 넘기지 않고 STEP 1을 새로 생성한다.
- STEP 1 소품이 펫프 아이콘이나 펫용품이면 `CLAUDE.md`의 **펫프 아이콘 에셋** 표에서 Element를 넣는다. 모양 & 형태 & 각인은 에셋 그대로, 재질은 달라도 된다. 겹치는 사물은 어느 쪽을 쓸지 먼저 묻는다.

### 앞에 물체가 있는 장면 (책상, 바구니, 상자)

캐릭터가 물체 뒤에 있어야 하면 아래 문장을 `## Critical conditions`에 넣는다. 넣지 않으면 상반신만 잘려서 물체 위에 올려진 것처럼 나온다 (수의사 장면 실측).

```
DEPTH: the {object} is IN FRONT of {CHARACTER}. {CHARACTER} stands BEHIND it; the {object} hides the lower body.
{CHARACTER} does NOT sit or rest on top of the {object}; no body shadow on its top surface.
```

### 글자 & 로고

- 배너 문구, 브랜드 로고, 상자 인쇄 마크는 생성하지 않는다. 생성하면 글자와 마크 모양이 틀어진다.
- 소품은 로고 없이 생성하고, 문구와 로고는 Figma에서 원본 에셋으로 얹는다.
- 위쪽에 문구가 들어갈 배너면 생성할 때 그 자리를 비워 둔다.

### 팔 자세

- 짧은 팔로 머리 위까지 드는 자세(상자 번쩍 들기 등)는 팔이 길어지거나 얼굴에 붙기 쉽다. 가능하면 가슴 앞에서 끌어안기 & 한 팔에 끼기처럼 짧은 팔에 맞는 자세로 바꾼다.
- **팔을 드는 자세는 "틈"으로 지시한다 (실측 2회).** "clearly out away from the head", "a visible gap between the paw and the face" 정도로는 안 막힌다. 2026-11-09 손 흔들기 컷은 이 문장을 넣고도 발과 얼굴이 **한 실루엣으로 붙어 나왔다** (그 높이의 가로 단면이 x166~734 한 덩어리, 간격 0px). 대신 배경이 보이게 지시한다.

```
There is a clear gap of background visible between the raised paw and the cheek,
at least as wide as the paw itself. The raised arm and the head do not touch and do
not overlap at any point; the silhouette shows two separate shapes there, not one.
```

- Negative 에도 함께 넣는다: `paw touching the face, paw overlapping the head, arm fused to the head, no gap between paw and cheek`
- 근거: `prompts/2026-11-09-validation-run.md` (손 흔들기), `prompts/2026-10-22-staged-scenes.md` (만세 & 택배기사)

### 다른 AI(ChatGPT 등)용 프롬프트만 요청받을 때

생성까지 해 달라는 게 아니라 **프롬프트만** 달라고 했을 때다. 생성까지 맡은 경우는 위 6번 "경로 B 변환"을 따른다.

생성하지 않고 프롬프트만 준다. 이때도 해당 캐릭터 `scene-blocks.md`의 Subject & Critical conditions & Negative를 빠짐없이 넣는다. 기존 이미지를 고치는 프롬프트면 바꿀 것만 번호로 나열하고 나머지는 "Keep EVERYTHING identical"로 고정한다.

---

## Negative

공통 Negative는 캐릭터마다 다르다. 해당 캐릭터 `scene-blocks.md`의 `## Negative` 블록을 그대로 쓰고, 그 뒤에 장면 고유 항목을 더한다.

다른 캐릭터 이름과 포인트 컬러를 Negative에 넣어 두는 것이 섞임을 막는 가장 확실한 장치다. 두 블록에 이미 들어가 있으니 지우지 않는다.

## 장면 고유 Negative 예시

- 소품 방향: `prop rotated, prop upside down, prop shape changed`
- 소품 접촉: `prop floating, prop not touching paws, prop fused into body`
- 시선: `looking at camera` (다른 곳을 봐야 할 때만)
- 의상: `hat covering the ear marking` (마킹이 보여야 할 때)

---

## 학습 루프

이 템플릿에서 고친 규칙은 `prompts/` 기록에서 **2회 이상 확인된 것만** 넣는다. 넣을 때 근거 기록 파일명을 함께 적는다.
캐릭터 하나에서만 확인된 규칙은 그 캐릭터의 `scene-blocks.md`에, 둘 다에 해당하는 규칙은 이 파일에 넣는다.
락 & 스타일 파일 반영이 필요해 보이면 직접 고치지 말고 사용자에게 제안한다.
