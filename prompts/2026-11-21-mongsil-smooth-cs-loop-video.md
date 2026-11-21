# 몽실 매끈 고객센터 상담 5초 루프 영상

- 날짜: 2026-11-21
- 캐릭터: 몽실 (매끈)
- 요청(한국어): 고객센터에서 상담해주는 몽실이 이미지를 영상으로. 클링으로, 매끈 시트 기준
- 상태: 미확인
- 모델 & 모드 & 길이 & 비율: Kling 3.0 & std & 5초 & 16:9 (사운드 off)
- 시작 프레임 & 끝 프레임: 사용자 제공 이미지 같은 장 (media 78d61b48-8495-4081-8a84-820f3a8a1f09). 끝 프레임을 같게 넣어 루프로 만듦
- 첨부 레퍼런스: 없음. Kling 3.0은 start_image & end_image 두 슬롯만 받아서 매끈 시트(b248495e-…)를 넣을 자리가 없었다
- job: d684d53d-e8ac-402d-9cd0-de879da750c0
- 결과: https://d8j0ntlcm91z4.cloudfront.net/user_3EWRwwFkTW4zqBlyAMkG4zr0B0i/hf_20261121_133019_d684d53d-e8ac-402d-9cd0-de879da750c0.mp4 (1280×720 & 24fps & 5.04초)
- 크레딧: 7.5 사용 (753.47 → 745.97)

## 프롬프트

```
Locked static camera, no zoom, no pan. The cute smooth 3D cat character keeps exactly the same face, head shape, brown ear patch, whiskers, colours, pink polo shirt with name tag and headset as the start frame for the whole video. Gentle customer-service call loop, 5 seconds: 0-1.5s the cat looks at the laptop screen and types softly, both front paws staying on the keyboard, one ear gives a small twitch. 1.5-3.5s the cat lifts its head slightly toward the camera, smiles and speaks into the headset microphone with small soft mouth movements, nodding twice in a friendly, attentive way. 3.5-5s it looks back down at the laptop and types again, returning to exactly the same pose as the first frame so the video loops seamlessly. Subtle, slow, cute motion only. The chair barely sways. Background stays plain flat pastel pink.
Negative: camera movement, zoom, face change, eyes getting bigger, extra whiskers, paws leaving the keyboard, waving, fingers, distorted paws, new objects, text, subtitles, logo changes, background change, fast motion, jitter, flicker.
```

## 검수 메모

- 타자 → 눈웃음 & 입 벌려 말하기 & 끄덕임 → 다시 타자 흐름으로 나옴
- 앞발은 끝까지 키보드 위에 있음. 얼굴 형태 & 무늬 & 수염 유지
- 첫 프레임과 마지막 프레임 평균 차이 1.3/255로 루프 이음 거의 없음
- 확인된 사실: Kling 3.0에는 레퍼런스 이미지 슬롯이 없다. 시트를 꼭 넣어야 하는 영상은 다른 모델이 필요하다
