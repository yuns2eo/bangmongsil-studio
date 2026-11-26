# 승인 컷 모음

사용자가 "좋다 & 이걸로 가자"고 승인한 결과 이미지 & 영상만 모은다. 기준 자료(`characters/*/references/`)와 달리 **실제로 쓰인 장면 결과물**이다.

## 언제 쓰나

- 자세 & 발 & 손 & 표정이 틀렸을 때, 같은 동작의 승인 컷을 **POSE TARGET**으로 첨부해 고친다 (예: 달리기 뒷발이 어색함 → 택배 몽실 달리기 컷의 뒷발)
- 같은 의상 & 소품 & 장면을 이어서 만들 때 타겟으로 첨부한다
- 영상은 `_frame.png`(대표 프레임)를 이미지 레퍼런스로 쓰고, 영상 자체는 모션 참고용으로 본다
- 승인 컷은 레퍼런스이지 정답 시트가 아니다. 캐릭터 규칙(락 파일 & 시트)과 다르면 규칙이 우선이다

## 올리는 규칙

- 사용자가 승인한 최종 컷만 올린다. 중간 버전 & 탈락 컷은 올리지 않는다
- 폴더: 캐릭터별 `approved/mongsil/` & `approved/bangsil/`. 둘 다 나오면 주인공 캐릭터 폴더에 넣는다
- 파일 이름: `{캐릭터}_{재질}_{장면}-{각도}_v{번호}.png`, 영상은 `{캐릭터}_{재질}_{장면}_video_{길이}.mp4` + 대표 프레임 `_frame.png`
  - 재질: `smooth` 또는 `felt`. 각도는 필요할 때만 (`45` & `front` & `side` & `back`)
  - 이미지는 16:9 정중앙 보정본(`_centered`)을 올린다
- 올릴 때 아래 표에 한 줄 추가한다. "참고하기 좋은 경우"에는 이 컷에서 잘 나온 부분을 구체적으로 적는다
- 기록 파일(`prompts/`)이 있으면 같이 적는다

## 목록

### 몽실

| 파일 | 장면 | 참고하기 좋은 경우 | 날짜 | 기록 |
|---|---|---|---|---|
| `mongsil/mongsil_smooth_courier_front_v2.png` | 택배기사 정면, 핑크 캡(뒤로) & 하늘색 폴로 & 크로스백, 펫프 택배상자 1개 | 택배기사 의상 & 펫프 택배상자 디자인 타겟, 정면 기본 표정 | 2026-11-25 | `prompts/2026-11-25-mongsil-smooth-courier-parcels.md` |
| `mongsil/mongsil_smooth_courier_run-45_v3.png` | 택배 3개를 안고 화면 왼쪽으로 달림, 45도, 당황 표정 & 땀방울 | **달리기 뒷발**: 다리가 뒤로 차올라가고 발바닥이 카메라 쪽으로 기울어 큰 패드 1개 + 발가락 패드 3개가 발끝 방향으로 보임. 짐을 안고 뒤로 젖힌 자세, 동그란 눈 + 작은 o 입 당황 표정 | 2026-11-26 | 같은 파일 |
| `mongsil/mongsil_smooth_courier_parcel-wobble_video_5s.mp4` (+ `_frame.png`) | 위 달리기 컷으로 만든 휘청 & 와리가리 루프 (Seedance 2.0 fast → 1080p) | 제자리 달리기 루프, 소품이 흔들려도 개수 유지, 땀방울. 입이 크게 벌어지는 구간 있음 | 2026-11-26 | 같은 파일 |
| `mongsil/mongsil_smooth_heart-cushion-jump_video_3s.mp4` (+ `_frame.png`) | 큰 하트 쿠션을 안고 폴짝 | 하트 소품 안기 & 점프 모션, 눈웃음 표정 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heart-cushion-jump_video_3s_pink.mp4` (+ `_frame.png`) | 위 영상의 배경만 연분홍 #FDEEF1 | 같은 장면을 연분홍 배경으로 쓸 때 | 2026-11-25 | 같은 파일 |
| `mongsil/mongsil_smooth_heartsignal-seollem_v1.png` | 하트시그널 설렘시작: 펫프 하트 상자 속에서 눈 & 귀만 빼꼼 | 상자 안에 숨은 구도, 상자 테두리에 걸친 앞발, 상자 리본 & 하트 로고 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heartsignal-monggeul_v1.png` | 하트시그널 몽글몽글: 상자 위로 올라와 작은 하트를 듦 | 상자에서 상반신이 나온 구도, 양손으로 하트를 가슴 앞에 든 자세, 혀 살짝 보이는 웃음 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heartsignal-dugeun_v1.png` | 하트시그널 두근두근: 서서 연분홍 하트를 안음, 정면 | 정면 서기 + 하트 안기 기본 자세, 몽실 정면 비율(머리 & 몸), 작은 웃음 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heartsignal-simkung-45_v2.png` | 하트시그널 심쿵주의: 45도로 앉아 진한 하트를 껴안음 | **팔 하트 무늬**: 팔을 앞으로 감쌀 때 윗가장자리에 옆으로 누운 하트(윤서가 직접 고친 위치). 앉은 자세 발바닥 패드, 혀 보이는 웃음 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heartsignal-cheonsaeng-wink_v2.png` | 하트시그널 천생연분: 아주 큰 진한 하트에 기대 윙크 + 입 크게 웃음, 45도 | 윙크 + 큰 웃음 표정(윙크 눈 간격은 `templates/scene.md` 8-1), 한 발 든 들뜬 자세, 하트에 몸을 기댄 구도. 하트를 줄이고 덜 들뜨게 다시 만드는 중이라 대체될 수 있음 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heart-lean-wink-45_v2.png` | 큰 진한 하트에 기대 윙크, 45도 (천생연분 타겟으로 쓴 원본) | 하트에 파묻히듯 기댄 자세, 얼굴이 정면에 가깝게 보이는 45도, 윙크 표정, 팔 하트 이식본 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_heartsignal-kongdak-front_v1.png` | 콩닥콩닥 ② 정면컷: 정면으로 서서 하트 옆에 섬 | 정면컷 단계 비율 기준(머리 0.71), ③ 자세 변경 전 타겟 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `mongsil/mongsil_smooth_sporty-hoodie-front_v1.png` | 운동복 집업 & 헤어밴드 & 땀방울 2개, 정면 | 운동복 의상 타겟. 집업 아래로 배 패치 아래 가장자리만 걸쳐 보이는 처리, 땀방울 크기 & 위치, 무늬 & 귀 정상 | 2026-11-22 | `prompts/2026-11-22-mongsil-sporty-hoodie.md` |
| `mongsil/mongsil_smooth_treadmill-45_v1.png` | 러닝머신 위 달리기, 45도, 힘든 표정 | **45도 달리기 자세**: 러닝머신 위에서 팔다리 교차, 운동복 & 헤어밴드 유지, 소품(러닝머신)과 캐릭터 크기 비율 | 2026-11-22 | 같은 파일 |
| `mongsil/mongsil_smooth_treadmill_video_3s.mp4` (+ `_frame.png`) | 위 컷으로 만든 러닝머신 달리기 루프 (Seedance 2.0 fast → 1080p) | 제자리 달리기 반복 모션, 카메라 고정, 의상 흔들림 | 2026-11-22 | 같은 파일 |
| `mongsil/mongsil_smooth_kimjang-vest-front_v1.png` | 빨강 꽃무늬 누빔 김장조끼, 정면 | 패턴 의상 디테일(다이아 누빔 & 로프 테두리 & 주머니 2개 & 은색 단추). 위 두 단추만 채워 배 패치 아래쪽이 보이게 한 처리. 펠트 → 매끈 재질만 바꾸는 편집 1회로 나온 컷 | 2026-11-22 | `prompts/2026-11-22-mongsil-smooth-kimjang-vest-gyul.md` |
| `mongsil/mongsil_smooth_kimjang-gyul-bowl-front_v1.png` | 김장조끼 입고 귤 4개 담긴 나무 그릇을 두 팔로 안음, 정면 | 그릇을 엉덩이 높이에서 두 팔로 감싸는 소품 들기 자세, 그릇 크기(머리폭 약 0.6) | 2026-11-22 | 같은 파일 |
| `mongsil/mongsil_smooth_kimjang-gyul-sit_v1.png` | 앉아서 귤 까먹기, 귤 조각을 입 앞에 듦 | **앉은 자세 발바닥**: 정면을 향한 뒷발바닥 큰 패드 1 + 발가락 패드 3 정확. 먹는 동작 손 위치(조각 든 손이 얼굴 아래에 살짝 닿는 점은 주의) | 2026-11-22 | 같은 파일 |
| `mongsil/mongsil_smooth_gyul-eating_video_4s.mp4` (+ `_frame.png`) | 귤 조각 쏙 → 오물오물(볼 볼록) → 으음~ 눈 지그시 (Seedance 2.0 fast → 1080p, 4.33초 트림) | 먹는 모션 & 볼 볼록 씹기 표현, 흐름형 프롬프트(#Feel & #Story) 결과. 끝 프레임이 시작 컷으로 돌아오지 않아 루프는 안 됨 | 2026-11-22 | 같은 파일 |
| `mongsil/mongsil_smooth_giftbox-pop_v1.png` | 열린 펫프 선물상자 안에서 고개 내민 몽실 & 하트 말풍선, 뚜껑은 옆에 | 상자 안에 들어간 구도, 앞발을 상자 테두리에 걸친 처리, 펫프 선물상자(박스안 & 뚜껑) 에셋 그대로 | 2026-11-23 | `prompts/2026-11-23-mongsil-smooth-giftbox-pop.md` |
| `mongsil/mongsil_smooth_giftbox-pop_video_5s.mp4` (+ `_frame.png`) | 빈 상자에서 몽실이 뿅 튀어나옴 (시작 = 빈 상자, 끝 = 위 컷) | 시작 & 끝 프레임으로 등장 모션 만들기, 상자 위치 고정 | 2026-11-23 | 같은 파일 |

### 방실

| 파일 | 장면 | 참고하기 좋은 경우 | 날짜 | 기록 |
|---|---|---|---|---|
| `bangsil/bangsil_felt_vet-exam-table-puppy-45_v8.png` | 수의사 방실(안경 & 가운 & 청진기)이 진료대 위 아픈 아기 강아지를 살핌, 45도 | 진지하고 걱정하는 표정 + 입 다문 물결 입, 진료대 & 강아지 소품, 수의사 의상 | 2026-11-25 | `prompts/2026-11-19-bangsil-felt-vet.md` |
| `bangsil/bangsil_felt_vet-puppy-cuddle_video_3s.mp4` (+ `_frame.png`) | 수의사 방실이 강아지를 안고 볼 비비기 (Seedance 2.0 fast → 1080p, 2초~끝 트림) | 두 캐릭터 볼 맞대기 교감, 화면 확대 없이 큰 동작 내기, 배너용 작은 크기에서도 보이는 모션 | 2026-11-26 | `prompts/2026-11-26-bangsil-felt-vet-puppy-cuddle-video.md` |
| `bangsil/bangsil_smooth_heartsignal-seollem_v4.png` | 하트시그널 설렘시작: 펫프 하트 상자 속에서 눈 & 귀만 빼꼼 | 상자 안에 숨은 구도, 상자 테두리에 걸친 앞발, 눈만 보이는 높이 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-monggeul_v5.png` | 하트시그널 몽글몽글: 상자 위로 올라와 작은 하트를 듦 | 상자에서 상반신이 나온 구도, 양손으로 하트를 든 자세, 방실 W 입 웃음 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-dugeun_v1.png` | 하트시그널 두근두근: 서서 연분홍 하트를 안음, 정면 | 정면 서기 + 하트 안기 기본 자세, 볼 털 뭉치 & 수염 없는 얼굴 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-kongdak-45_v5.png` | 하트시그널 콩닥콩닥: 45도로 서서 큰 하트를 품에 안음 | **큰 하트 품에 안기**: 하트가 눌리지 않고 품에 안긴 자세, 하트 크기 기준(몸 대비 약 0.53, 색 #F791A6 근처), 시선 정면 + 혀 보이는 웃음 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-simkung-45_v5.png` | 하트시그널 심쿵주의: 45도로 앉아 진한 하트를 껴안음 | 앉은 자세 발바닥 패드(큰 패드 + 발가락 3개), 하트를 옆에서 껴안은 팔, 눈 뜬 행복한 웃음 | 2026-11-24 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-cheonsaeng-wink_v2.png` | 하트시그널 천생연분: 아주 큰 진한 하트에 기대 윙크 + 입 크게 웃음, 45도 | 윙크 + 큰 웃음 표정(방실 윙크 눈 간격 기준), 한 발 든 들뜬 자세. 하트를 줄이고 덜 들뜨게 다시 만드는 중이라 대체될 수 있음 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_heartsignal-kongdak-front_v1.png` | 콩닥콩닥 ② 정면컷: 정면으로 서서 진한 하트 옆에 섬 | 정면컷 단계 타겟, 살짝 웃는 표정, 하트 크기 중간 | 2026-11-25 | `prompts/2026-11-24-mypetf-heart-signal-grades.md` |
| `bangsil/bangsil_smooth_magnifier-front_v1.png` | 큰 알 돋보기를 든 정면 | 돋보기 소품 크기 & 쥐는 손, 정면 기본 표정 + 안경 | 2026-11-23 | `prompts/2026-11-23-bangsil-smooth-magnifier-treatball.md` |
| `bangsil/bangsil_smooth_magnifier-treatball-45_v1.png` | 45도로 돌아 살짝 숙이고 돋보기로 간식볼을 살핌, 다른 손은 허리 | 45도 숙인 자세 & 허리 손, 간식볼 에셋(링 4개 & 뼈 각인 & 사료) 그대로. 시선이 공 대신 카메라를 보는 점은 주의 | 2026-11-23 | 같은 파일 |
| `bangsil/bangsil_smooth_magnifier-treatball_video_5s.mp4` (+ `_frame.png`) | 간식볼 살피기 → 공이 굴러감 → 정면 쪽으로 돌며 놀람 (Seedance 2.0 fast → 1080p) | 소품이 굴러가는 모션, 확대 없음. 가는 눈 구간 & 'o' 입 구간 있음 | 2026-11-23 | 같은 파일 |
| `bangsil/bangsil_smooth_uniform-openbook-45_v1.png` | 교복 & 투명 핑크 뿔테 & 베이지 백팩, 펼친 책을 든 45도 | 교복 & 안경 & 백팩 의상 타겟, 45도에서 펼친 책 한 권 드는 손 | 2026-11-22 | `prompts/2026-11-22-bangsil-smooth-glasses-push-video.md` |
| `bangsil/bangsil_smooth_uniform-pageturn_video_6s.mp4` (+ `_frame.png`) | 책 읽다 멈칫 → 오잇! 책장 넘기기 (Seedance 2.0 fast → 1080p, 6초 전체) | **자연스러운 모션**: 규칙적이지 않은 타이밍 & 예비 동작 & 여운. 끝이 시작 표정으로 돌아옴. #Feel & #Story 프롬프트 구조 참고 | 2026-11-22 | 같은 파일 |
| `bangsil/bangsil_smooth_vet-center-hug_v1.png` | 수의사 방실(안경 & 가운 & 청진기)이 강아지를 품 가운데 안음, 흰 배경 | 강아지를 정면으로 품 가운데 안는 자세(들어올리기 실패 뒤 한 번에 나옴), 수의사 의상 매끈 버전 | 2026-11-24 | `prompts/2026-11-24-bangsil-smooth-vet-puppy-poses.md` |
| `bangsil/bangsil_smooth_vet-puppy-exam_video_5s.mp4` (+ `_frame.png`) | 진료실에서 청진기 대고 강아지와 이마 & 볼 맞대기 (Seedance 2.0 fast → 1080p) | 앞발을 들지 않고 고개로만 교감하는 모션(손가락 4개 생기는 문제 회피), 방 배경 유지. 0.7초 & 3초쯤 눈웃음 구간 있음 | 2026-11-22 | `prompts/2026-11-21-bangsil-smooth-vet-puppy-video.md` |
| `bangsil/bangsil_smooth_book-read_v1.png` | 연분홍 두꺼운 책을 자기 쪽으로 펼쳐 읽기, 정면 | 책 펼쳐 든 두 손, 웃음① 입 다문 미소, 책 색(캔디 핑크) | 2026-11-25 | `prompts/2026-11-25-bangsil-smooth-book.md` |
| `bangsil/bangsil_smooth_book-think-45_v3.png` | 한 팔로 책 들고 다른 손은 턱에, 깜짝 표정, 화면 오른쪽을 봄 | **턱 손 자세** & 깜짝 표정(`Feel_3_Surprised`, W선 없는 동그란 입이 정답). 원본 Left_3Q 각도로 만든 뒤 좌우 반전 — 반전 레퍼런스를 넣으면 사시가 됨 | 2026-11-25 | 같은 파일 |
