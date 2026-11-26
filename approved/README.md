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

### 방실

| 파일 | 장면 | 참고하기 좋은 경우 | 날짜 | 기록 |
|---|---|---|---|---|
| `bangsil/bangsil_felt_vet-exam-table-puppy-45_v8.png` | 수의사 방실(안경 & 가운 & 청진기)이 진료대 위 아픈 아기 강아지를 살핌, 45도 | 진지하고 걱정하는 표정 + 입 다문 물결 입, 진료대 & 강아지 소품, 수의사 의상 | 2026-11-25 | `prompts/2026-11-19-bangsil-felt-vet.md` |
| `bangsil/bangsil_felt_vet-puppy-cuddle_video_3s.mp4` (+ `_frame.png`) | 수의사 방실이 강아지를 안고 볼 비비기 (Seedance 2.0 fast → 1080p, 2초~끝 트림) | 두 캐릭터 볼 맞대기 교감, 화면 확대 없이 큰 동작 내기, 배너용 작은 크기에서도 보이는 모션 | 2026-11-26 | `prompts/2026-11-26-bangsil-felt-vet-puppy-cuddle-video.md` |
