# oaispencil - Pencil 디자인 기획 스킬

## 문서 이력

| 버전 | 날짜 | 변경 내용 |
|------|------|----------|
| v05 | 2026-02-26 | 화면 간 간격 및 겹침 방지 가이드 추가 (18장) |
| v04 | 2026-02-26 | 연결선/화살표 추가 주의사항 추가 (17장) |
| v03 | 2026-02-26 | 텍스트 추가/좌표 설정 방지 가이드 추가 (14-16장) |
| v02 | 2026-02-25 | 최신 Pencil MCP 도구 추가 |
| v01 | 2026-02-25 | 초기 작성 |

> 공통: `v/guide/common_guide.md` | Pencil MCP 도구 참조

---

## 1. 개요

Pencil 도구를 활용한 웹/앱 UI 디자인 기획 및 프로토타입 생성.

- **역할**: UI/UX 디자이너 - 디자인 요구사항을 .pen 파일로 변환
- **도구**: Pencil MCP (pencil_batch_design, pencil_get_guidelines 등)
- **출력**: .pen 디자인 파일, 스타일 가이드

---

## 2. 서브명령어

| 명령어 | 설명 |
|--------|------|
| `oaispencil version` | 스킬 버전 정보 (v05) |
| `oaispencil status` | 서브명령어 리스트, 현재 상태 |
| `oaispencil new` | 새 디자인 문서 생성 |
| `oaispencil open [파일]` | 기존 .pen 파일 열기 |
| `oaispencil design` | 디자인 요구사항 분석 후 설계 |
| `oaispencil style [태그]` | 스타일 가이드 조회/적용 |
| `oaispencil guide` | 디자인 가이드라인 조회 |
| `oaispencil component` | 컴포넌트 목록 조회 |

---

## 3. Pencil MCP 도구

### 3.1 핵심 도구

| 도구 | 설명 |
|------|------|
| `pencil_open_document` | .pen 파일 열기/생성 |
| `pencil_get_editor_state` | 현재 에디터 상태 조회 |
| `pencil_get_style_guide` | 스타일 가이드 조회 |
| `pencil_get_style_guide_tags` | 사용 가능한 스타일 태그 조회 |
| `pencil_batch_design` | 디자인 연산 실행 (I/C/U/R/D/G) |
| `pencil_batch_get` | 노드 조회 (패턴/ID 기반) |
| `pencil_get_screenshot` | 노드 스크린샷 캡처 |
| `pencil_get_variables` | 디자인 변수/테마 조회 |
| `pencil_set_variables` | 디자인 변수/테마 설정 |
| `pencil_get_guidelines` | 디자인 가이드라인 조회 |
| `pencil_snapshot_layout` | 레이아웃 구조 분석 |
| `pencil_find_empty_space_on_canvas` | 캔버스 빈 공간 찾기 |
| `pencil_replace_all_matching_properties` | 일치하는 속성 일괄 변경 |
| `pencil_search_all_unique_properties` | 고유 속성 검색 |

---

## 4. batch_design 연산

```javascript
// Insert (생성)
nodeId = I(parentId, {type: "frame", layout: "vertical"})

// Copy (복제)
copiedId = C(path, parent, {positionPadding: 100})

// Update (수정)
U(path, {content: "New Text", fill: "#FF0000"})

// Replace (교체)
replacedId = R(path, {type: "text", content: "New"})

// Delete (삭제)
D(nodeId)

// Image 생성
G(nodeId, "ai", "prompt")  // AI 이미지
G(nodeId, "stock", "keywords")  // 스톡 사진
```

---

## 5. 가이드라인 조회

### 5.1 guideline 주제

Pencil에서 제공하는 공식 가이드라인을 조회합니다.

```javascript
pencil_get_guidelines({ topic: "code" })      // .pen 파일에서 코드 생성 가이드
pencil_get_guidelines({ topic: "table" })      // 테이블 디자인 가이드
pencil_get_guidelines({ topic: "tailwind" })   // Tailwind CSS 구현 가이드
pencil_get_guidelines({ topic: "landing-page" })  // 랜딩페이지 디자인 가이드
pencil_get_guidelines({ topic: "design-system" }) // 디자인 시스템 컴포넌트 가이드
```

---

## 6. 속성 검색 & 변경

### 6.1 고유 속성 검색

문서 내 노드들의 특정 속성 값을 검색합니다.

```javascript
pencil_search_all_unique_properties({
  parents: ["frameId1", "frameId2"],
  properties: ["fillColor", "fontSize", "padding", "gap", "textColor"]
})
```

### 6.2 일괄 속성 변경

조건에 맞는 노드들의 속성을 한 번에 변경합니다.

```javascript
// 색상 일괄 변경
pencil_replace_all_matching_properties({
  parents: ["parentFrameId"],
  properties: {
    fillColor: [
      { from: "#FFFFFF", to: "#F5F5F5" },
      { from: "#000000", to: "#1A1A1A" }
    ],
    textColor: [
      { from: "#666666", to: "#888888" }
    ]
  }
})

// 폰트 크기 일괄 변경
pencil_replace_all_matching_properties({
  parents: ["parentFrameId"],
  properties: {
    fontSize: [
      { from: 14, to: 16 },
      { from: 12, to: 14 }
    ]
  }
})
```

---

## 7. 빈 공간 찾기

### 7.1 캔버스에서 빈 공간 검색

새로운 프레임이나 요소를 배치할 빈 공간을 찾습니다.

```javascript
// 특정 노드 주변의 빈 공간 찾기
pencil_find_empty_space_on_canvas({
  nodeId: "existingFrameId",  // 기준 노드 ID
  direction: "right",          // 빈 공간 방향 (top, right, bottom, left)
  width: 400,                // 필요한 너비
  height: 300,               // 필요한 높이
  padding: 20                // 다른 요소와의 최소 간격
})

// 캔버스 전체에서 빈 공간 찾기
pencil_find_empty_space_on_canvas({
  width: 800,
  height: 600,
  padding: 50
})
```

---

## 8. 변수 & 테마 관리

### 8.1 변수 조회

```javascript
pencil_get_variables({ filePath: "design.pen" })
```

### 8.2 변수 설정

```javascript
pencil_set_variables({
  filePath: "design.pen",
  replace: false,  // true: 기존 변수 완전히 교체, false: 병합
  variables: {
    "primary-color": "#3B82F6",
    "secondary-color": "#10B981",
    "font-heading": "Inter",
    "font-body": "Roboto"
  }
})
```

---

## 9. 워크플로우

### 9.1 new (새 문서 생성)

1. pencil_open_document("new") → 새 문서 생성
2. pencil_get_editor_state → 에디터 상태 확인
3. pencil_get_guidelines({ topic: "..." }) → 가이드라인 조회 (선택)
4. pencil_set_variables → 테마/변수 설정 (선택)
5. 기본 프레임 생성

### 9.2 design (디자인 설계)

1. 요구사항 분석 → 필요한 화면/컴포넌트 정의
2. pencil_get_style_guide_tags → 사용 가능한 스타일 조회
3. pencil_get_guidelines → 관련 가이드라인 조회
4. pencil_batch_design → 프레임/컴포넌트 생성
5. pencil_search_all_unique_properties → 속성 일관성 확인
6. pencil_get_screenshot → 결과 검증

### 9.3 속성 일괄 변경

1. pencil_snapshot_layout → 현재 레이아웃 분석
2. pencil_search_all_unique_properties → 변경할 속성 확인
3. pencil_replace_all_matching_properties → 속성 일괄 변경
4. pencil_get_screenshot → 변경 결과 검증

---

## 10. 스타일 가이드

### 10.1 주요 태그 카테고리

| 카테고리 | 태그 예시 |
|----------|----------|
| UI 유형 | webapp, dashboard, mobile-app, landing-page |
| 스타일 | minimal, brutalist, clean, sophisticated |
| 색상 | pastel, vibrant, monochrome, neon |
| 느낌 | friendly, professional, playful, premium |

---

## 11. 실전 예시

### 11.1 대시보드 레이아웃 생성

```javascript
// 1. 메인 프레임 업데이트 - 레이아웃 설정
U("frameId", {placeholder: true, layout: "horizontal", gap: 16})

// 2. 사이드바 삽입
sidebar = I("frameId", {type: "ref", ref: "JRlf7", width: 240, height: "fill_container"})

// 3. 메인 콘텐츠 영역
mainContent = I("frameId", {type: "frame", layout: "vertical", gap: 24, padding: 32})

// 4. 카드 컴포넌트 추가
card1 = I("stats", {type: "ref", ref: "QMBKc", width: "fill_container", height: 120})
card2 = I("stats", {type: "ref", ref: "QMBKc", width: "fill_container", height: 120})
card3 = I("stats", {type: "ref", ref: "QMBKc", width: "fill_container", height: 120})
```

### 11.2 색상 테마 일괄 변경

```javascript
// 다크 모드로 변경
pencil_replace_all_matching_properties({
  parents: ["mainContainer"],
  properties: {
    fillColor: [
      { from: "#FFFFFF", to: "#1A1A1A" },
      { from: "#F5F5F5", to: "#2D2D2D" }
    ],
    textColor: [
      { from: "#000000", to: "#FFFFFF" },
      { from: "#666666", to: "#AAAAAA" }
    ]
  }
})
```

### 11.3 빈 공간에 새 요소 배치

```javascript
// 사이드바 오른쪽에 빈 공간 찾기
space = pencil_find_empty_space_on_canvas({
  nodeId: "sidebar",
  direction: "right",
  width: 600,
  height: "fill_container",
  padding: 24
})

// 찾은 공간에 콘텐츠 영역 생성
contentArea = I("document", {
  type: "frame",
  layout: "vertical",
  x: space.x,
  y: space.y,
  width: space.width,
  height: space.height
})
```

---

## 12. 관련 스킬

| 스킬 | 용도 |
|------|------|
| oaisdoc | 디자인 요구사항 문서화 |
| oaisprd | PRD 기반 UI 요구사항 정의 |
| oaisreport | 디자인 결과 리포트 생성 |

---

## 13. 제한사항

- 단일 HTML 파일 배포 시 .pen → HTML 변환 필요
- 복잡한 인터랙티브 기능은 HTML/JS로 별도 구현
- 이미지 생성은 AI/스톡 서비스 의존 (네트워크 필요)
- 속성 변경은 기존에 존재하는 값만/from-to로 변경 가능

---

## 14. 텍스트 추가 및 좌표 설정 방지 가이드

### 14.1 핵심 규칙: rectangle에 텍스트 추가 금지

**❌ 잘못된 방법:**
```javascript
// rectangle 노드 안에 텍스트 추가 시도 (실패함 - rectangle은 자식을 가질 수 없음)
I("rectangleId", {type: "text", content: "버튼 텍스트"})
```

**✅ 올바른 방법:**
```javascript
// 1. rectangle을 frame으로 교체
R("rectangleId", {type: "frame", cornerRadius: 10, fill: "#FFFFFF", width: 80, height: 36, layout: "vertical", justifyContent: "center", alignItems: "center"})

// 2. frame 안에 텍스트 추가
I("newFrameId", {type: "text", content: "버튼 텍스트", fill: "#000000", fontFamily: "Plus Jakarta Sans", fontSize: 14, textGrowth: "auto"})
```

### 14.2 batch_design 연산 순서 문제

**❌ 잘못된 방법:**
```javascript
// 한 번에 여러 연산 실행 시 parent가 아직 생성되지 않음
D("oldNode")
I("parentId", {type: "frame"})  // 아직 생성 안 됨
I("parentId/child", {type: "text"})  // 실패!
```

**✅ 올바른 방법:**
```javascript
// 연산은 순차적으로 적용됨 - 한 번에 하나만 실행
// 1단계: 부모 노드 생성
I("parentId", {type: "frame", name: "myFrame"})

// 2단계: 부모 노드 확인 후 자식 추가
// (별도 batch_design 호출에서)
I("parentId", {type: "text", content: "Hello"})
```

### 14.3 텍스트 추가 체크리스트

텍스트를 추가할 때마다 확인:
- [ ] 부모 노드가 frame인가? (rectangle이면 frame으로 교체)
- [ ] frame에 `layout: "vertical"` 설정했는가?
- [ ] frame에 `justifyContent: "center"` 설정했는가?
- [ ] frame에 `alignItems: "center"` 설정했는가?
- [ ] 텍스트에 `textGrowth: "auto"` 설정했는가?

### 14.4 자주 하는 실수 패턴

| 실수 | 원인 | 해결책 |
|------|------|--------|
| 텍스트가 버튼 밖으로 나감 | rectangle에 텍스트 추가 | frame으로 교체 |
| 텍스트가 왼쪽 상단에 붙음 | layout 속성 없음 | justifyContent/alignItems 추가 |
| 텍스트가 보이지 않음 | fill 색상 없음 | fill 속성 필수 |
| 연산 실패 | parent 노드 순서 | 연산 분리 (별도 호출) |

### 14.5 스크린샷 검증 필수

**작업 후 반드시 스크린샷으로 확인:**
```javascript
pencil_get_screenshot({ filePath: "design.pen", nodeId: "targetNodeId" })
```

- 텍스트가 정확한 위치에 있는가?
- 텍스트가 잘리는 현상 없는가?
- 다른 요소와 겹치지 않는가?

---

## 15. 팝업 화면 설계 체크리스트

### 15.1 필수 요소 확인

팝업 화면 생성 시 반드시 포함:
- [ ] 헤더: 제목 + 닫기(X) 버튼
- [ ] 콘텐츠: 기능별 필요한 입력요소
- [ ] 푸터: 취소/확인 버튼 (있어야 함!)
- [ ] 버튼 텍스트: 모든 버튼에 텍스트 추가

### 15.2 버튼 텍스트 추가 패턴

```javascript
// 취소 버튼
R("cancelRect", {type: "frame", cornerRadius: 10, fill: "#FFFFFF", width: 80, height: 36, layout: "vertical", justifyContent: "center", alignItems: "center", stroke: {...}})
I("cancelFrame", {type: "text", content: "취소", fill: "#6B6B6B", fontFamily: "Plus Jakarta Sans", fontSize: 14, textGrowth: "auto"})

// 확인 버튼  
R("confirmRect", {type: "frame", cornerRadius: 10, fill: "#7C9070", width: 80, height: 36, layout: "vertical", justifyContent: "center", alignItems: "center"})
I("confirmFrame", {type: "text", content: "확인", fill: "#FFFFFF", fontFamily: "Plus Jakarta Sans", fontSize: 14, textGrowth: "auto"})
```

### 15.3 PRD vs 구현 비교

화면 구현 전/후:
1. PRD 요구사항 체크
2. 누락된 요소 파악
3. 구현 완료 후 검증

---

## 16. 모던 UI 스타일 적용

### 16.1 스칸디나비안 스타일 가이드

현재 프로젝트에서 사용 중인 스타일:

| 속성 | 값 |
|------|-----|
| 배경색 | #F7F6F3 (warm parchment) |
| 카드 배경 | #FFFFFF |
| 기본 색상 | #7C9070 (sage green) |
| 텍스트 primary | #2D2D2D |
| 텍스트 secondary | #6B6B6B |
| 테두리 | #F0EFEC |
| 모서리 반경 | 10-16px |
| 폰트 | Plus Jakarta Sans |

### 16.2 스타일 적용 예시

```javascript
// 메인 프레임
U("mainFrame", {fill: "#F7F6F3", cornerRadius: 16})

// 버튼
U("buttonFrame", {fill: "#7C9070", cornerRadius: 12, layout: "vertical", justifyContent: "center", alignItems: "center"})

// 입력 필드
U("inputFrame", {fill: "#FFFFFF", cornerRadius: 8, stroke: {align: "center", fill: "#F0EFEC", thickness: 1}})

// 텍스트
U("textNode", {fill: "#2D2D2D", fontFamily: "Plus Jakarta Sans", fontSize: 14})
```

---

## 17. 연결선(화살표) 추가 시 주의사항

### 17.1 path/line 노드의 색상 문제

**❌ 잘못된 방법:**
```javascript
// stroke에 fill 색상 없으면 렌더링 안 됨
I("parent", {type: "path", stroke: {thickness: 2}})
```

**✅ 올바른 방법:**
```javascript
// stroke에 fill 색상 반드시 추가
I("parent", {type: "line", stroke: {fill: "#00FFFF", thickness: 3}})
```

### 17.2 flexbox 레이아웃에서 좌표 문제

**❌ 잘못된 방법:**
```javascript
// frame이 layout: "vertical" 또는 "horizontal" 일 때 x/y 무시됨
U("parentFrame", {layout: "vertical"})
I("parentFrame", {type: "line", x: 100, y: 200})  // 좌표 무시!
```

**✅ 올바른 방법:**
```javascript
// 1. frame을 layout: "none"으로 설정하거나
U("parentFrame", {layout: "none"})
I("parentFrame", {type: "line", x: 100, y: 200})

// 2. 또는 별도 컨테이너 사용
I("document", {type: "line", x: 100, y: 200})  // 최상위에서 직접 추가
```

### 17.3 캔버스 외부 배치 문제

**현상:** 노드는 추가했지만 스크린샷에서 안 보임

**원인:**
- 부모 프레임보다 큰 x/y 좌표
- 캔버스 크기보다 밖

**✅ 해결책:**
```javascript
// 1. 캔버스 크기 확인
pencil_snapshot_layout({maxDepth: 1})

// 2. 부모 프레임 크기 확인
pencil_batch_get({nodeIds: ["parentId"], readDepth: 1})

// 3. 좌표 재설정 (부모 안쪽으로)
U("lineNode", {x: 부모너비-50, y: 부모높이-10})
```

### 17.4 대안: 텍스트로 관계 표시

연결선이 복잡하면 버튼 텍스트에 팝업 번호 추가:
```javascript
// 버튼 텍스트에 팝업 번호 포함
U("buttonLabel", {content: "🌐 2. 사이트 선택"})
U("aiButtonLabel", {content: "🤖 3. AI 설정"})
```

### 17.5 체크리스트

연결선/화살표 추가 전:
- [ ] stroke에 fill 색상 추가했는가? (없으면 안 보임)
- [ ] 부모 프레임이 layout: "none"인가?
- [ ] 좌표가 부모 프레임 안에 있는가?
- [ ] 캔버스 크기보다不大的가?
- [ ] 스크린샷으로 검증했는가?

### 17.6 rectangle으로 대체

line/path가 안 보이면 rectangle로 대체:
```javascript
// 가로선
I("parent", {type: "rectangle", fill: "#00FFFF", width: 100, height: 3, x: 100, y: 200})

// 화살표 머리 (ellipse)
I("parent", {type: "ellipse", fill: "#00FFFF", width: 10, height: 10, x: 200, y: 200})
```

### 17.7 rectangle 노드의 좌표 문제

**⚠️ 중요:** rectangle이 flexbox 프레임 안에도 x/y가 적용됨

```javascript
// flexbox 레이아웃이든 상관없이 rectangle은 x/y 사용 가능
// 하지만 부모가 fill_container를 쓰면 문제가 생길 수 있음

// 해결: rectangle을 독립적으로 배치
I("document", {type: "rectangle", ...})  // 최상위에서 추가
```

---

## 18. 화면 간 간격 및 겹침 방지

### 18.1 문제 상황

화면(프레임)을 편집할 때 내부 요소가 추가되거나 크기가 변경되면 부모 프레임의 높이가 증가합니다. 이때 다른 화면들과 겹칠 수 있습니다.

**예시:**
```
메인 윈도우 (y: 0, height: 620)
  ↓ 크기 증가 (height: 730)
팝업 A (y: 711) ← 겹침!
```

### 18.2 레이아웃 분석 방법

**항상 먼저 스냅샷으로 분석:**
```javascript
pencil_snapshot_layout({maxDepth: 1})
```

**결과 해석:**
```
{id: "mainWindow", y: 0, height: 730}     // 0 ~ 730
{id: "popup1", y: 711, height: 600}       // 711 ~ 1311 → 겹침!
{id: "popup2", y: 800, height: 400}       // 800 ~ 1200 → 정상
```

### 18.3 겹침 확인 공식

**두 프레임 A와 B가 겹치지 않는 조건:**
```
A.y + A.height < B.y  (A가 B보다 위에 있음)
또는
B.y + B.height < A.y  (B가 A보다 위에 있음)
```

### 18.4 겹침 해결 Steps

**1단계: snapshot_layout으로 현재 상태 분석**
```javascript
pencil_snapshot_layout({maxDepth: 1})
```

**2단계: 겹치는 프레임의 y 좌표 재설정**
```javascript
// 아래쪽 팝업들을 이동
U("popupA", {y: 상단프레임높이 + 간격})
U("popupB", {y: popupA.y + popupA.height + 간격})
```

**3단계: 다시 스냅샷으로 검증**

### 18.5 권장 간격

| 상황 | 최소 간격 | 권장 간격 |
|------|----------|----------|
| 인접한 화면 | 20px | 50px |
| 관련 화면 그룹 | 50px | 100px |
| 완전히 독립된 화면 | 100px | 150px |

### 18.6 체크리스트

화면 추가/편집 후:
- [ ] pencil_snapshot_layout로 모든 프레임 위치 확인
- [ ] 각 프레임의 y + height가 다음 프레임의 y보다 작은지 확인
- [ ] 겹치는 경우 y 좌표 재설정
- [ ] 스크린샷으로 최종 검증
- [ ] 모든 팝업이 캔버스(width/height) 안에 있는지 확인

### 18.7 캔버스 크기 관리

화면이 많아지면 캔버스 크기도 증가:
```javascript
// 캔버스 크기 확인
pencil_snapshot_layout({maxDepth: 1})
// {id: "bi8Au", width: 800, height: 600}

// 캔버스 크기 조정
U("bi8Au", {width: 1500, height: 1200})
```

### 18.8 실전 예시

**문제:** 메인 윈도우 높이가 620→730으로 증가해서 저장 경로 팝업(y: 711)과 겹침

**해결:**
```javascript
// 1. 분석 결과
// 메인: y=0, height=730 (끝: 730)
// 저장경로: y=711 → 겹침!

// 2. 팝업 이동 (메인.height + 간격)
U("Suuf5", {y: 800})  // 730 + 70
U("aTtY1", {y: 800})  // 동일하게
U("fq1bk", {y: 800})  // 동일하게

// 3. 검증
pencil_snapshot_layout({maxDepth: 1})
```
