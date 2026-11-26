# 방실 펠트 수의사 & 강아지 볼 비비기 영상

- 날짜: 2026-11-26
- 캐릭터: 방실 (펠트) + 크림색 강아지
- 요청(한국어): 수의사 방실이 강아지를 안고 볼을 맞댄 이미지(사용자 제공, 2044×1150)로 작은 모션
- 상태: 사용자 승인 (2차, 2초~끝 트림본)
- 쓰임: 수의사상담 서비스 배너 (374×200 영역, 왼쪽 텍스트 + 오른쪽 영상)

## 모델

- Claude 제안: Kling 3.0 Frames (작은 움직임, 원본 유지). 대안으로 Seedance 2.0 fast 제시
- 사용자 결정: "화면 확대는 락가이드 걸어주고, 시트를 넣을 수 있는 씨댄스로" → Seedance 2.0 fast
- 시작 & 끝 프레임: 사용자 이미지 그대로 (이미 16:9 & 정중앙). media 3c592f4d-f883-42e6-bcb2-1fc294f67797
- 레퍼런스: 방실 펠트 시트 (743b126a-…)
- 설정: 480p & 5초 & 16:9 & 오디오 off

## 1차

- 프롬프트 요지: #Scene & #Expression(둘 다 눈웃음 유지, EyeLock 없음) & #NoEffects & #FramingLock(크기 & 위치 & 여백 고정, 카메라 쪽으로 돌지 않음) & #Story(볼 한 번 부비기 → 강아지 살짝 기댐 & 꼬리 살랑 → 방실 꼬리 한 번) & #Feel(small, slow and cozy) & #Identity & #Outfit & #Paws(토닥 금지) & #Tail & #Negative
- job: d43cac21-d6f3-4233-8a44-e73afef0fc9e, 업스케일 e96e619b-b1bd-45f1-af53-80501431d195
- 검수: 화면 확대 없음, 얼굴 & 안경 & 청진기 유지
- 사용자 반응: "동작들이 너무 작아서 보이질 않아"

## 2차

- 수정: #Story를 크게 — 둘이 같이 좌우로 약 10도 흔들림 → 방실이 고개 기울여 볼을 두 번 꾹 부빔(볼 눌림 & 귀 튕김) → 강아지가 신나서 들썩이며 턱을 들고 파고듦, 귀 펄럭 & 꼬리 크게 → 방실 꼬리 크게 & 발끝 톡. #Feel에 "lively, bouncy, clearly readable motion even at small size, squash and stretch". 네거티브에 "tiny barely visible motion, frozen bodies"
- job: 8149c46b-0720-4d79-bc73-c0e9a876d6c4, 업스케일 a5d1538b-2c28-41ca-bf1a-bb06be874ed9 → 1920×1080
- 검수: FramingLock 유지(확대 없음), 움직임이 작게 봐도 보임. 강아지가 한 번 엉덩이를 들썩이는 순간 있음
- 사용자 요청: 2초부터 끝까지만 남김 → BANGSIL_vet_puppy_cuddle_3s_1080p_v2_trim.mp4 (3초, 시작이 원본 이미지와 달라 루프 이음매가 생길 수 있음)
- 크레딧: 1차 & 2차 합계 약 12

## 확인된 사실

- 씨댄스 + 강한 #FramingLock("크기 & 위치 & 여백을 시작 프레임과 같게, 카메라 쪽으로 돌지 않음")에서 볼 맞대기 장면도 화면 확대가 없었다 (2회 확인: 1차 & 2차)
- 배너처럼 작게 쓰는 영상은 "small, slow" 위주로 쓰면 움직임이 안 보인다. 처음부터 몸 전체 흔들림 & 각도(약 10도) & squash and stretch & "clearly readable even at small size"를 넣는다 (1회 관찰)
