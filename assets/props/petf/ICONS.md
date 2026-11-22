# 펫프 아이콘 에셋 (petf-icon-studio)

`CLAUDE.md`에서 옮긴 표다 (2026-11-22). 사용 조건과 규칙은 아래 그대로 따른다.

**사용자가 펫프 아이콘(에셋 이름이나 "펫프 아이콘")을 직접 부를 때만 쓴다.** 부르지 않으면 이 표를 쓰지 않고 `CLAUDE.md` 소품 표나 `## Prop` 문장으로 처리한다 (2026-11-19 사용자 지시). 부르면 새로 묘사하지 않고 [`yuns2eo/petf-icon-studio`](https://github.com/yuns2eo/petf-icon-studio)에 등록된 에셋을 쓴다. 아래 Element는 그 저장소 `references/{common|cat|dog}/{파일}_Front.png`와 같은 이미지다.

- STEP 1(의상 & 소품)에서 소품이 아래 표에 있으면 그 Element를 넣는다. 프롬프트에는 "the prop is exactly <<<ID>>>: same shape, silhouette, proportions, parts, and every engraved / embossed mark, motif, and symbol" 문장을 넣는다.
- **모양 & 형태 & 각인(음각 & 양각 로고, 발바닥 & 뼈다귀 무늬, 기호)은 에셋과 똑같아야 한다.** 재질(젤리 & 광택 & 펠트)은 장면에 맞게 달라져도 된다.
- 에셋에 원래 있는 각인은 유지한다. 에셋에 없는 문구 & 로고는 여전히 생성하지 않고 Figma에서 얹는다 (`templates/scene.md` 7번).
- Element는 정면 한 장만 주입된다. 정면이 아닌 각도가 필요하면 petf-icon-studio의 `{파일}_4View.png`를 `media_upload`해서 `medias`로 함께 첨부한다.
- 같은 사물이 `CLAUDE.md` 소품 표와 이 표에 둘 다 있으면(선물상자, 쿠폰, 코인) **임의로 고르지 말고 어느 쪽을 쓸지 사용자에게 묻는다.**
- 고양이 & 강아지 버전이 둘 다 있는 사물(사료그릇, 사료캔, 사료봉투)은 요청에 종이 없으면 묻는다. 몽실이나 방실이 장면이라고 고양이로 정하지 않는다.
- 이 표에 없는 펫프 아이콘을 요청받으면 petf-icon-studio `library/JELLY_Object_Library.md`와 Higgsfield Element 목록(`manage_reference_elements` list)에서 이름으로 찾는다. 찾으면 이 표에 추가하고, 없으면 사용자에게 알린다.

| 구분 | Element 이름 | ID | petf 파일 |
|---|---|---|---|
| 공통 | 쿠폰1 | `cba59651-6614-4dc9-936b-0f51bee031bf` | `Coupon_Pink` (4가지 포즈 시트, 한 장만 그린다) |
| 공통 | 쿠폰2 | `83f7b321-1225-4bef-9b80-9b0ca77713b0` | `Coupon_Teal` (4가지 포즈 시트, 한 장만 그린다) |
| 공통 | 할인쿠폰 | `9e7ecd83-6a0b-489a-8d6a-a7727863a48a` | `Discount_Ticket` |
| 공통 | 가격태그 | `ce4528d6-d862-423a-a209-d3773a8dbef5` | `Price_Tags` |
| 공통 | 선물상자 | `668f217e-28dc-4238-88b6-d8a764abf630` | `Gift_Box` |
| 공통 | 장바구니 | `7f6862f2-fd54-48a8-9a3a-46de001feecb` | `Shopping_Basket` |
| 공통 | 쇼핑카트 | `9a2f78ef-8d1a-4bac-8d8e-ff94ceafcf1f` | `Shopping_Cart` |
| 공통 | 포인트코인 | `889888aa-a13f-42c6-a3d3-4d95d64cc465` | `Point_Coin` |
| 공통 | 코인1 (하트코인 핑크) | `08481f5f-887a-4b78-9ec2-b79e34264e24` | `Heart_Coin_Pink` |
| 공통 | 코인2 (하트코인 실버) | `6b90ba39-76af-4613-a20c-1721f29e80e2` | `Heart_Coin_Silver` |
| 공통 | 택배상자 | `b8237ed4-2c67-4a1a-9eb5-f28025e375d3` | `Parcel_Box` |
| 공통 | 지갑 | `6587b6f2-6323-4c86-b076-4d5c14fe56cb` | `Wallet` |
| 공통 | 말풍선 | `01b8ddd4-29d5-4d94-b0ab-409403dbb7fe` | `Speech_Bubble` |
| 공통 | 종 | `1e055add-c2f3-497d-968b-0399b7d73f44` | `Bell` |
| 공통 | 자명종 | `f5855127-dd6c-4dea-9754-9f3423e68790` | `Alarm_Clock` |
| 공통 | 배송트럭 | `73232719-99ed-4345-ae90-80d475e72fbe` | `Delivery_Truck` |
| 공통 | 달력 | `dccf082f-e29f-4842-b329-e8879932c1f4` | `Calendar` |
| 공통 | 발바닥 | `07181e21-67a6-478e-a3d3-6bd09237163c` | `Paw` (아이콘 소품. 몽실이 손발바닥 패드는 위 디테일 Element) |
| 고양이 | 사료그릇 | `68720491-d337-4d1c-a5db-dfeb17bee145` | `Food_Bowl` |
| 고양이 | 사료캔1 | `4e29763e-e677-4f9e-b0a8-985679e29249` | `Food_Can_1` |
| 고양이 | 사료캔2 | `1e82bd0f-04a2-46c2-9bde-ca4597349f6f` | `Food_Can_2` |
| 고양이 | 사료봉투_고양이 | `ef5f4d1e-f772-4c33-a7c1-cc9d1b144350` | `Food_Pouch` |
| 고양이 | 사료통1 (간식통) | `4861d539-8b76-40d2-833c-e8ee5187615b` | `Food_Jar_1` |
| 고양이 | 사료통2 (간식통) | `5ad8eab3-3386-4614-949f-698297bc9921` | `Food_Jar_2` |
| 고양이 | 자동급식기_고양이 | `6555c897-8dea-4866-997b-88d44240551f` | `Auto_Feeder` |
| 고양이 | 급수기_고양이 | `507822ce-bf38-418a-a87d-ed2b2174035f` | `Water_Fountain` |
| 고양이 | 이동장_고양이 | `4eb438a1-5d83-4419-9717-9f5dc2308277` | `Carrier` |
| 고양이 | 빗_고양이 | `2abd01b3-0d03-4e0a-a9c2-ed2d9aaa03f4` | `Slicker_Brush` |
| 고양이 | 분무기 | `131ce07e-863a-4e3c-80a2-23b8172ef26b` | `Spray_Bottle` |
| 고양이 | 낚싯대_고양이 | `f0892018-eb74-433b-b19f-7a23ee4187db` | `Wand_Toy` |
| 고양이 | 화장실_고양이 | `216a5c92-27bd-4a1e-9ad0-1206c909d504` | `Litter_Box` |
| 고양이 | 캣타워_고양이 | `445e0f75-4ec0-4432-8b21-9f17fe8c6a06` | `Cat_Tower` |
| 강아지 | 사료그릇2 | `dc0827ae-f1dc-4f0d-b97b-4183cb0cf189` | `Food_Bowl` |
| 강아지 | 사료캔_강아지 | `573411b3-e413-4a60-940e-ed9df969577e` | `Food_Can` |
| 강아지 | 사료봉투_강아지 | `472b3e80-ea13-4ba6-8eda-3575d408a3a2` | `Food_Pouch` |
| 강아지 | 간식통_강아지 | `4b13b03c-97fa-4a23-9c27-a4672d0383dd` | `Treat_Jar` |
| 강아지 | 간식볼_강아지 | `d8fb17a1-ddb3-4e77-a442-44d02eb31da6` | `Treat_Ball` |
| 강아지 | 리드줄_강아지 | `6a64315c-95c2-4adb-a72e-383bb4d4222c` | `Leash` |
| 강아지 | 방석_강아지 | `fecd3d6d-a740-4653-a63c-162d649aa1d5` | `Bed` |
| 강아지 | 양치세트_강아지 | `e08e57c0-e5a3-43f0-8478-185179dcfd15` | `Toothbrush_Set` |

겹치는 사물 (사용자에게 물어볼 것):

| 사물 | 몽실스튜디오 소품 | petf 에셋 |
|---|---|---|
| 선물상자 | `펫프_선물상자` (광택 & 무광 & 젤리 & 박스안 & 뚜껑) | `선물상자` (`Gift_Box`) |
| 쿠폰 | `쿠폰_광택` 등 6종 | `쿠폰1` & `쿠폰2` & `할인쿠폰` |
| 코인 | `펫프_코인_광택` & `_무광` & `_젤리` & `_실버` & `_실버무광` & `_투명젤리` (Higgsfield에만 등록됨) | `포인트코인` & `코인1` & `코인2` |
