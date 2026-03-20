# d0002_plan.md - EasyOCR 제품 라벨 인식 구현 계획

## 문서 이력 관리

| 버전 | 날짜 | 변경 내용 | 작성자 |
|------|------|----------|--------|
| v1.0 | 2026-01-28 | 최초 작성 | Claude |

---

## 1. 구현 개요

### 1.1 프로젝트 요약

본 프로젝트는 EasyOCR 라이브러리를 활용하여 제품 라벨 이미지에서 텍스트를 자동으로 인식하고 구조화된 데이터로 변환하는 시스템을 구축하는 것을 목표로 합니다.

### 1.2 핵심 목표

1. 제품 라벨 이미지에서 텍스트 자동 인식 (한국어/영어)
2. EasyOCR의 성능 및 정확도 검증
3. 이미지 전처리를 통한 인식률 향상
4. 구조화된 결과 출력 및 저장 (JSON)
5. 배치 처리 기능으로 다중 이미지 일괄 처리

### 1.3 프로젝트 범위

- 정적 이미지 파일 (JPG, PNG) 처리
- CRAFT 기반 텍스트 감지 + CRNN 기반 인식
- OpenCV 기반 이미지 전처리
- 신뢰도 기반 결과 필터링 및 시각화
- 배치 처리 및 성능 최적화

### 1.4 기술 스택

| 구분 | 기술 | 용도 |
|------|------|------|
| 언어 | Python 3.13+ | 메인 개발 언어 |
| OCR | EasyOCR 1.7+ | 텍스트 인식 |
| 전처리 | OpenCV 4.8+ | 이미지 전처리 |
| 이미지 처리 | Pillow 10.0+ | 이미지 로드/저장 |
| 백엔드 | PyTorch 2.0+ | EasyOCR 백엔드 |
| 패키지 관리 | uv | 의존성 관리 |

---

## 2. WBS (Work Breakdown Structure)

### Epic 1: 환경 설정 및 프로젝트 구조

프로젝트 개발 환경 구축 및 기본 구조 설정

#### Feature 1.1: 개발 환경 설정

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E001-F001-T001 | Python 3.13 환경 구성 | .python-version 파일 생성 및 Python 버전 검증 | Pending | High |
| E001-F001-T002 | uv 패키지 관리자 설정 | pyproject.toml 작성 및 의존성 정의 | Pending | High |
| E001-F001-T003 | 핵심 라이브러리 설치 | easyocr, opencv-python, pillow, numpy, torch 설치 | Pending | High |
| E001-F001-T004 | 선택적 라이브러리 설치 | pandas, matplotlib, pytest 설치 | Pending | Medium |

#### Feature 1.2: 폴더 구조 생성

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E001-F002-T001 | 소스 디렉토리 생성 | src/ 폴더 생성 및 __init__.py 추가 | Pending | High |
| E001-F002-T002 | 데이터 디렉토리 생성 | data/01_sample/, data/output/ 폴더 생성 | Pending | High |
| E001-F002-T003 | 테스트 디렉토리 생성 | tests/ 폴더 생성 및 구조 설정 | Pending | Medium |
| E001-F002-T004 | 문서 디렉토리 확인 | doc/ 폴더 내 필수 문서 존재 확인 | Pending | Medium |
| E001-F002-T005 | 임시 디렉토리 생성 | tmp/debug/ 폴더 생성 | Pending | Low |

---

### Epic 2: 이미지 전처리 모듈

OCR 성능 향상을 위한 이미지 전처리 기능 구현

#### Feature 2.1: 기본 이미지 처리

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E002-F001-T001 | 이미지 로드 함수 구현 | Pillow/OpenCV를 이용한 이미지 읽기 | Pending | High |
| E002-F001-T002 | 파일 형식 검증 | JPG, PNG 형식 확인 및 예외 처리 | Pending | High |
| E002-F001-T003 | 이미지 크기 확인 | 최소/최대 해상도 검증 (640x480 ~ 10MB) | Pending | Medium |
| E002-F001-T004 | 이미지 메타데이터 추출 | 파일명, 크기, 해상도 정보 추출 | Pending | Low |

#### Feature 2.2: 전처리 기법 구현

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E002-F002-T001 | 그레이스케일 변환 | 컬러 이미지를 흑백으로 변환 | Pending | High |
| E002-F002-T002 | 노이즈 제거 | Gaussian Blur를 이용한 잡음 제거 | Pending | High |
| E002-F002-T003 | 이진화 처리 | Adaptive Threshold를 이용한 이진화 | Pending | High |
| E002-F002-T004 | 대비 강화 | CLAHE를 이용한 저조도 이미지 개선 | Pending | Medium |
| E002-F002-T005 | 리사이징 | 장변 기준 1280px로 크기 조정 | Pending | Medium |
| E002-F002-T006 | 전처리 파이프라인 통합 | 모든 전처리 기법을 하나의 파이프라인으로 통합 | Pending | High |

#### Feature 2.3: 전처리 유틸리티

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E002-F003-T001 | 전처리 옵션 클래스 | 전처리 파라미터 관리 클래스 구현 | Pending | Medium |
| E002-F003-T002 | 전후 비교 시각화 | 전처리 전후 이미지 비교 함수 | Pending | Low |
| E002-F003-T003 | 전처리 결과 저장 | 디버그용 전처리 이미지 저장 | Pending | Low |

---

### Epic 3: OCR 엔진 (EasyOCR)

EasyOCR을 이용한 텍스트 감지 및 인식 기능 구현

#### Feature 3.1: EasyOCR 초기화

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E003-F001-T001 | Reader 객체 생성 | EasyOCR Reader 초기화 (언어: ko, en) | Pending | High |
| E003-F001-T002 | GPU 감지 및 설정 | CUDA 사용 가능 여부 확인 및 GPU 설정 | Pending | Medium |
| E003-F001-T003 | 모델 다운로드 관리 | 최초 실행 시 모델 자동 다운로드 처리 | Pending | High |
| E003-F001-T004 | Reader 객체 캐싱 | 반복 실행 시 Reader 재사용으로 성능 향상 | Pending | Medium |

#### Feature 3.2: 텍스트 감지 및 인식

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E003-F002-T001 | readtext() 메서드 실행 | EasyOCR의 readtext() 호출 | Pending | High |
| E003-F002-T002 | CRAFT 텍스트 감지 | 이미지에서 텍스트 영역 감지 | Pending | High |
| E003-F002-T003 | CRNN 텍스트 인식 | 감지된 영역의 문자열 인식 | Pending | High |
| E003-F002-T004 | 바운딩박스 추출 | 텍스트 영역 좌표 추출 | Pending | High |
| E003-F002-T005 | 신뢰도 추출 | 각 텍스트의 신뢰도 점수 추출 | Pending | High |

#### Feature 3.3: 언어별 처리

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E003-F003-T001 | 한국어 인식 설정 | 한국어 텍스트 인식 최적화 | Pending | High |
| E003-F003-T002 | 영어 인식 설정 | 영어 텍스트 인식 최적화 | Pending | High |
| E003-F003-T003 | 혼합 언어 처리 | 한국어/영어 혼재 텍스트 처리 | Pending | Medium |
| E003-F003-T004 | 언어별 결과 분류 | 인식 결과를 언어별로 분류 (선택 기능) | Pending | Low |

---

### Epic 4: 결과 후처리 및 저장

OCR 결과 정제, 구조화 및 파일 저장 기능 구현

#### Feature 4.1: 결과 정제

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E004-F001-T001 | 신뢰도 필터링 | 신뢰도 0.3 미만 결과 제거 | Pending | High |
| E004-F001-T002 | 중복 영역 제거 | IoU 기반 중복 바운딩박스 제거 | Pending | Medium |
| E004-F001-T003 | 좌표 정규화 | 바운딩박스 좌표를 원본 이미지 크기 기준으로 정규화 | Pending | Medium |
| E004-F001-T004 | 공백 문자 처리 | 불필요한 공백 제거 및 정리 | Pending | Low |

#### Feature 4.2: 결과 구조화

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E004-F002-T001 | 결과 딕셔너리 생성 | text, confidence, bbox, language 포함 딕셔너리 생성 | Pending | High |
| E004-F002-T002 | 메타데이터 추가 | 파일명, 처리 시간 등 메타데이터 추가 | Pending | Medium |
| E004-F002-T003 | JSON 스키마 정의 | 출력 JSON 구조 정의 및 검증 | Pending | Medium |

#### Feature 4.3: 결과 저장

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E004-F003-T001 | JSON 파일 저장 | data/output/ 폴더에 JSON 형식으로 저장 | Pending | High |
| E004-F003-T002 | 파일명 자동 생성 | 원본 파일명 기반 출력 파일명 생성 | Pending | Medium |
| E004-F003-T003 | 저장 경로 검증 | 출력 디렉토리 존재 확인 및 자동 생성 | Pending | Medium |
| E004-F003-T004 | 인코딩 처리 | UTF-8 인코딩으로 한글 깨짐 방지 | Pending | High |

#### Feature 4.4: 시각화

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E004-F004-T001 | 바운딩박스 그리기 | 원본 이미지에 인식 영역 표시 | Pending | Medium |
| E004-F004-T002 | 텍스트 오버레이 | 인식된 텍스트를 이미지에 표시 | Pending | Low |
| E004-F004-T003 | 신뢰도 색상 표시 | 신뢰도에 따라 바운딩박스 색상 변경 | Pending | Low |
| E004-F004-T004 | 시각화 이미지 저장 | 시각화 결과를 이미지 파일로 저장 | Pending | Medium |

---

### Epic 5: 통합 및 배치 처리

메인 스크립트 작성 및 배치 처리 기능 구현

#### Feature 5.1: 메인 스크립트 (test_ocr.py)

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E005-F001-T001 | CLI 인자 파싱 | argparse를 이용한 명령줄 인자 처리 | Pending | High |
| E005-F001-T002 | 단일 이미지 처리 모드 | --input 옵션으로 단일 이미지 처리 | Pending | High |
| E005-F001-T003 | 전체 파이프라인 통합 | 전처리 → OCR → 후처리 → 저장 통합 | Pending | High |
| E005-F001-T004 | 에러 핸들링 | 예외 상황 처리 및 로깅 | Pending | High |
| E005-F001-T005 | 처리 시간 측정 | 각 단계별 소요 시간 측정 및 출력 | Pending | Medium |

#### Feature 5.2: 배치 처리

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E005-F002-T001 | 폴더 스캔 기능 | 지정 폴더 내 모든 이미지 파일 검색 | Pending | High |
| E005-F002-T002 | 확장자 필터링 | --extensions 옵션으로 처리 파일 형식 선택 | Pending | Medium |
| E005-F002-T003 | 다중 이미지 순차 처리 | 이미지 리스트를 순차적으로 처리 | Pending | High |
| E005-F002-T004 | 배치 결과 집계 | 전체 이미지 처리 결과 통계 출력 | Pending | Medium |
| E005-F002-T005 | 부분 실패 처리 | 일부 이미지 실패 시 계속 진행 | Pending | High |

#### Feature 5.3: 성능 최적화

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E005-F003-T001 | Reader 객체 재사용 | 배치 처리 시 Reader 객체 한 번만 초기화 | Pending | High |
| E005-F003-T002 | GPU 메모리 관리 | GPU 사용 시 메모리 누수 방지 | Pending | Medium |
| E005-F003-T003 | 병렬 처리 고려 | 멀티스레딩/멀티프로세싱 검토 (선택) | Pending | Low |
| E005-F003-T004 | 캐싱 전략 | 중복 이미지 처리 방지 | Pending | Low |

#### Feature 5.4: 유틸리티 함수 (utils.py)

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E005-F004-T001 | 파일 경로 검증 함수 | 파일 존재 여부 및 권한 확인 | Pending | High |
| E005-F004-T002 | 로깅 설정 함수 | 로그 레벨 및 포맷 설정 | Pending | Medium |
| E005-F004-T003 | 이미지 형식 변환 함수 | 다양한 형식 간 변환 유틸리티 | Pending | Low |
| E005-F004-T004 | 좌표 변환 함수 | 바운딩박스 좌표 변환 유틸리티 | Pending | Medium |

---

### Epic 6: 테스트 및 품질 보증

단위 테스트, 통합 테스트 및 성능 평가

#### Feature 6.1: 단위 테스트

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E006-F001-T001 | preprocessor 테스트 | 전처리 함수별 단위 테스트 작성 | Pending | High |
| E006-F001-T002 | ocr_engine 테스트 | OCR 실행 함수 테스트 작성 | Pending | High |
| E006-F001-T003 | postprocessor 테스트 | 후처리 함수 테스트 작성 | Pending | High |
| E006-F001-T004 | utils 테스트 | 유틸리티 함수 테스트 작성 | Pending | Medium |
| E006-F001-T005 | pytest 설정 | pytest.ini 및 conftest.py 작성 | Pending | Medium |

#### Feature 6.2: 통합 테스트

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E006-F002-T001 | 전체 파이프라인 테스트 | 이미지 입력부터 결과 저장까지 E2E 테스트 | Pending | High |
| E006-F002-T002 | 배치 처리 테스트 | 다중 이미지 배치 처리 테스트 | Pending | Medium |
| E006-F002-T003 | 에러 복구 테스트 | 예외 상황 처리 테스트 | Pending | Medium |

#### Feature 6.3: 테스트 데이터 준비

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E006-F003-T001 | 샘플 이미지 수집 | 식품/의약품/화장품 라벨 이미지 50개 수집 | Pending | High |
| E006-F003-T002 | 이미지 품질 다양화 | 고/중/저해상도, 다양한 조명 조건 | Pending | Medium |
| E006-F003-T003 | Ground Truth 작성 | 샘플 이미지의 정답 텍스트 작성 | Pending | Medium |

#### Feature 6.4: 성능 평가

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E006-F004-T001 | 정확도 평가 함수 | Character/Word Accuracy 계산 함수 작성 | Pending | Medium |
| E006-F004-T002 | 처리 속도 측정 | 평균, 중앙값, 95 percentile 측정 | Pending | Medium |
| E006-F004-T003 | 메모리 사용량 측정 | 피크 메모리 사용량 모니터링 | Pending | Low |
| E006-F004-T004 | 성능 리포트 생성 | 테스트 결과를 종합한 성능 리포트 작성 | Pending | Medium |

---

### Epic 7: 문서화 및 배포 준비

프로젝트 문서 작성 및 배포 준비

#### Feature 7.1: 코드 문서화

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E007-F001-T001 | Docstring 작성 | 모든 함수/클래스에 Google Style Docstring 작성 | Pending | Medium |
| E007-F001-T002 | Type Hints 추가 | 타입 힌트를 통한 코드 가독성 향상 | Pending | Medium |
| E007-F001-T003 | 인라인 주석 추가 | 복잡한 로직에 주석 추가 | Pending | Low |

#### Feature 7.2: 프로젝트 문서 작성

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E007-F002-T001 | README.md 작성 | 프로젝트 소개, 설치, 실행 방법 작성 | Pending | High |
| E007-F002-T002 | d0003_test.md 업데이트 | 테스트 시나리오 및 체크리스트 작성 | Pending | Medium |
| E007-F002-T003 | d0004_todo.md 관리 | TODO 항목 및 디버깅 내역 정리 | Pending | Medium |
| E007-F002-T004 | d0005_lib.md 작성 | 사용 라이브러리 및 종속성 문서화 | Pending | Medium |

#### Feature 7.3: 배포 준비

| ID | Task | 설명 | 상태 | 우선순위 |
|----|------|------|------|---------|
| E007-F003-T001 | pyproject.toml 최종 검토 | 의존성 버전 확정 및 메타데이터 작성 | Pending | High |
| E007-F003-T002 | .gitignore 작성 | 불필요한 파일 제외 설정 | Pending | Medium |
| E007-F003-T003 | 라이선스 파일 추가 | LICENSE 파일 추가 (선택) | Pending | Low |

---

## 3. 스프린트 계획

### Sprint 1: 환경 설정 + 핵심 OCR (2-3일)

목표: 기본 개발 환경 구축 및 단일 이미지 OCR 처리 가능한 최소 기능 구현

#### 포함 Epic/Feature

- **Epic 1**: 환경 설정 및 프로젝트 구조
  - Feature 1.1: 개발 환경 설정
  - Feature 1.2: 폴더 구조 생성
- **Epic 3**: OCR 엔진
  - Feature 3.1: EasyOCR 초기화
  - Feature 3.2: 텍스트 감지 및 인식
  - Feature 3.3: 언어별 처리
- **Epic 5**: 통합 및 배치 처리
  - Feature 5.1: 메인 스크립트 (기본 기능만)

#### 주요 Task

1. Python 3.13 환경 구성 및 uv 설정
2. 핵심 라이브러리 설치 (easyocr, opencv, pillow)
3. 폴더 구조 생성
4. EasyOCR Reader 초기화
5. 단일 이미지 OCR 실행 및 결과 출력
6. 기본 CLI 인자 파싱 구현

#### 완료 조건

- uv run python src/test_ocr.py --input [이미지경로] 실행 시 텍스트 인식 결과 콘솔 출력
- 한국어/영어 혼합 텍스트 인식 가능
- 신뢰도 및 바운딩박스 좌표 출력

---

### Sprint 2: 전처리 + 후처리 (2-3일)

목표: 이미지 전처리 및 결과 후처리, 구조화된 출력 저장

#### 포함 Epic/Feature

- **Epic 2**: 이미지 전처리 모듈
  - Feature 2.1: 기본 이미지 처리
  - Feature 2.2: 전처리 기법 구현
  - Feature 2.3: 전처리 유틸리티
- **Epic 4**: 결과 후처리 및 저장
  - Feature 4.1: 결과 정제
  - Feature 4.2: 결과 구조화
  - Feature 4.3: 결과 저장
  - Feature 4.4: 시각화

#### 주요 Task

1. 이미지 로드 및 형식 검증
2. 그레이스케일, 이진화, 노이즈 제거 구현
3. 전처리 파이프라인 통합
4. 신뢰도 필터링 및 중복 제거
5. JSON 결과 파일 저장
6. 바운딩박스 시각화 구현

#### 완료 조건

- --preprocess 옵션으로 전처리 적용 가능
- data/output/ 폴더에 JSON 결과 저장
- --visualize 옵션으로 바운딩박스 시각화 이미지 생성

---

### Sprint 3: 배치 처리 + 최적화 + 테스트 (2-3일)

목표: 배치 처리 기능, 성능 최적화, 테스트 및 문서화

#### 포함 Epic/Feature

- **Epic 5**: 통합 및 배치 처리
  - Feature 5.2: 배치 처리
  - Feature 5.3: 성능 최적화
  - Feature 5.4: 유틸리티 함수
- **Epic 6**: 테스트 및 품질 보증
  - Feature 6.1: 단위 테스트
  - Feature 6.2: 통합 테스트
  - Feature 6.3: 테스트 데이터 준비
  - Feature 6.4: 성능 평가
- **Epic 7**: 문서화 및 배포 준비
  - Feature 7.1: 코드 문서화
  - Feature 7.2: 프로젝트 문서 작성
  - Feature 7.3: 배포 준비

#### 주요 Task

1. 폴더 스캔 및 다중 이미지 처리
2. Reader 객체 재사용 및 GPU 메모리 관리
3. 유틸리티 함수 작성
4. 단위 테스트 및 통합 테스트 작성
5. 샘플 이미지 50개 수집 및 Ground Truth 작성
6. 성능 평가 및 리포트 생성
7. Docstring, Type Hints 추가
8. README.md 및 관련 문서 작성

#### 완료 조건

- --batch 옵션으로 폴더 내 모든 이미지 일괄 처리
- pytest 실행 시 모든 테스트 통과
- 성능 평가 리포트 생성 (정확도, 처리 속도)
- 문서 완성 (README, d0003, d0004, d0005)

---

## 4. 기술 설계

### 4.1 모듈 구조

```
src/
├── test_ocr.py           # 메인 실행 파일 (CLI 진입점)
├── ocr_engine.py         # EasyOCR 래퍼 클래스
├── preprocessor.py       # 이미지 전처리 모듈
├── postprocessor.py      # 결과 후처리 모듈
├── visualizer.py         # 바운딩박스 시각화
└── utils.py              # 유틸리티 함수
```

#### 모듈별 책임

| 모듈 | 책임 | 주요 함수/클래스 |
|------|------|-----------------|
| test_ocr.py | CLI 인자 파싱, 전체 파이프라인 조율, 배치 처리 | main(), process_single(), process_batch() |
| ocr_engine.py | EasyOCR Reader 관리, OCR 실행 | OCREngine 클래스, detect_text() |
| preprocessor.py | 이미지 전처리 (그레이스케일, 이진화 등) | ImagePreprocessor 클래스, preprocess() |
| postprocessor.py | 결과 정제 (필터링, 정규화, 구조화) | PostProcessor 클래스, filter_results() |
| visualizer.py | 바운딩박스 그리기, 시각화 이미지 생성 | Visualizer 클래스, draw_bboxes() |
| utils.py | 파일 검증, 로깅, 좌표 변환 등 | validate_file(), setup_logger(), convert_coords() |

### 4.2 데이터 흐름

```
[이미지 입력]
    ↓
[utils.validate_file()]  → 파일 검증
    ↓
[preprocessor.preprocess()]  → 전처리
    ↓
[ocr_engine.detect_text()]  → OCR 실행
    ↓
[postprocessor.filter_results()]  → 결과 정제
    ↓
[postprocessor.structure_results()]  → 구조화
    ↓
[visualizer.draw_bboxes()] (선택)  → 시각화
    ↓
[저장: JSON 파일, 시각화 이미지]
    ↓
[결과 출력]
```

### 4.3 주요 클래스 설계

#### OCREngine 클래스

```python
class OCREngine:
    """
    EasyOCR을 래핑하는 OCR 엔진 클래스
    """
    def __init__(self, languages=['ko', 'en'], gpu=False):
        """
        Args:
            languages: 인식 언어 목록
            gpu: GPU 사용 여부
        """
        pass

    def detect_text(self, image):
        """
        이미지에서 텍스트 감지 및 인식

        Args:
            image: numpy array 형식 이미지

        Returns:
            List[Dict]: 인식 결과 리스트
        """
        pass
```

#### ImagePreprocessor 클래스

```python
class ImagePreprocessor:
    """
    이미지 전처리 파이프라인
    """
    def __init__(self, options=None):
        """
        Args:
            options: 전처리 옵션 딕셔너리
        """
        pass

    def preprocess(self, image):
        """
        전처리 파이프라인 실행

        Args:
            image: 원본 이미지

        Returns:
            전처리된 이미지
        """
        pass

    def grayscale(self, image):
        """그레이스케일 변환"""
        pass

    def denoise(self, image):
        """노이즈 제거"""
        pass

    def binarize(self, image):
        """이진화"""
        pass
```

#### PostProcessor 클래스

```python
class PostProcessor:
    """
    OCR 결과 후처리
    """
    def filter_results(self, results, confidence_threshold=0.3):
        """
        신뢰도 기반 필터링

        Args:
            results: OCR 원시 결과
            confidence_threshold: 신뢰도 임계값

        Returns:
            필터링된 결과
        """
        pass

    def structure_results(self, results, metadata=None):
        """
        결과를 구조화된 딕셔너리로 변환

        Args:
            results: 필터링된 결과
            metadata: 메타데이터 (파일명, 처리 시간 등)

        Returns:
            구조화된 결과 딕셔너리
        """
        pass
```

### 4.4 데이터 스키마

#### OCR 결과 JSON 스키마

```json
{
  "filename": "sample_label.jpg",
  "timestamp": "2026-01-28T10:30:00",
  "processing_time": 3.45,
  "image_size": {
    "width": 1920,
    "height": 1080
  },
  "results": [
    {
      "text": "유통기한: 2026.12.31",
      "confidence": 0.92,
      "bbox": [[10, 20], [200, 20], [200, 50], [10, 50]],
      "language": "ko"
    },
    {
      "text": "Product Name",
      "confidence": 0.88,
      "bbox": [[10, 60], [180, 60], [180, 90], [10, 90]],
      "language": "en"
    }
  ],
  "summary": {
    "total_detected": 15,
    "total_accepted": 12,
    "average_confidence": 0.85
  }
}
```

---

## 5. 리스크 관리

### 5.1 기술적 리스크

| 리스크 | 영향도 | 발생 가능성 | 대응 방안 |
|--------|--------|------------|----------|
| 한국어 인식률이 목표(70%) 미달 | High | Medium | 전처리 강화, 이미지 품질 향상, 후처리 규칙 추가 |
| GPU 미지원 환경에서 처리 속도 저하 | Medium | High | CPU 최적화, 배치 크기 조정, 처리 시간 완화 |
| 메모리 부족으로 대용량 이미지 처리 실패 | Medium | Medium | 이미지 리사이징, 메모리 모니터링, 스트리밍 처리 |
| EasyOCR 모델 다운로드 실패 | Low | Low | 모델 로컬 캐싱, 대체 다운로드 경로 제공 |
| 특정 폰트/스타일 인식 실패 | Medium | Medium | 다양한 샘플 테스트, 전처리 파라미터 튜닝 |

### 5.2 일정 리스크

| 리스크 | 영향도 | 발생 가능성 | 대응 방안 |
|--------|--------|------------|----------|
| 테스트 데이터 수집 지연 | Medium | Medium | 온라인 공개 데이터셋 활용, 샘플 수 축소 |
| 성능 최적화 시간 부족 | Low | Medium | Sprint 3에서 우선순위 조정, 선택 기능 제외 |
| 문서 작성 시간 부족 | Low | Low | 코드 작성과 병행하여 Docstring 우선 작성 |

### 5.3 품질 리스크

| 리스크 | 영향도 | 발생 가능성 | 대응 방안 |
|--------|--------|------------|----------|
| 테스트 커버리지 부족 | Medium | Medium | 핵심 모듈 우선 테스트, 자동화 테스트 도입 |
| 에러 핸들링 누락 | High | Medium | 예외 상황 체크리스트 작성, 코드 리뷰 |
| 한글 인코딩 문제 | Medium | Low | UTF-8 인코딩 강제, 인코딩 테스트 추가 |

---

## 6. 진행 추적

### 6.1 Epic 진행 상황

| Epic | 완료율 | 상태 | 담당자 | 비고 |
|------|--------|------|--------|------|
| Epic 1: 환경 설정 및 프로젝트 구조 | 0% | Not Started | - | Sprint 1 |
| Epic 2: 이미지 전처리 모듈 | 0% | Not Started | - | Sprint 2 |
| Epic 3: OCR 엔진 | 0% | Not Started | - | Sprint 1 |
| Epic 4: 결과 후처리 및 저장 | 0% | Not Started | - | Sprint 2 |
| Epic 5: 통합 및 배치 처리 | 0% | Not Started | - | Sprint 1, 3 |
| Epic 6: 테스트 및 품질 보증 | 0% | Not Started | - | Sprint 3 |
| Epic 7: 문서화 및 배포 준비 | 0% | Not Started | - | Sprint 3 |

### 6.2 주요 마일스톤

| 마일스톤 | 목표일 | 상태 | 설명 |
|---------|--------|------|------|
| M1: 환경 설정 완료 | Sprint 1 Day 1 | Pending | uv 설정, 라이브러리 설치 완료 |
| M2: 단일 이미지 OCR 실행 | Sprint 1 Day 2-3 | Pending | 기본 OCR 기능 동작 |
| M3: 전처리 파이프라인 완성 | Sprint 2 Day 1-2 | Pending | 모든 전처리 기법 구현 |
| M4: JSON 저장 및 시각화 | Sprint 2 Day 3 | Pending | 구조화된 결과 저장 |
| M5: 배치 처리 기능 완성 | Sprint 3 Day 1 | Pending | 다중 이미지 일괄 처리 |
| M6: 테스트 완료 | Sprint 3 Day 2 | Pending | 단위/통합 테스트 통과 |
| M7: 문서화 및 배포 준비 | Sprint 3 Day 3 | Pending | README 작성, 문서 정리 |

### 6.3 작업 우선순위

#### Must Have (필수)

1. 개발 환경 설정 (Epic 1)
2. EasyOCR 초기화 및 텍스트 인식 (Epic 3)
3. 기본 전처리 (그레이스케일, 이진화) (Epic 2)
4. 결과 정제 및 JSON 저장 (Epic 4)
5. 메인 스크립트 통합 (Epic 5)
6. 단위 테스트 (Epic 6)

#### Should Have (중요)

1. 고급 전처리 (노이즈 제거, 대비 강화) (Epic 2)
2. 바운딩박스 시각화 (Epic 4)
3. 배치 처리 (Epic 5)
4. 통합 테스트 (Epic 6)
5. 코드 문서화 (Epic 7)

#### Could Have (선택)

1. 언어별 분류 (Epic 3)
2. 병렬 처리 (Epic 5)
3. 성능 평가 리포트 (Epic 6)
4. 전처리 옵션 커스터마이징 (Epic 2)

### 6.4 문제점 및 해결 상황

| 문제 | 발견일 | 심각도 | 상태 | 해결 방안 |
|------|--------|--------|------|----------|
| - | - | - | - | - |

> 문제 발생 시 이 섹션을 업데이트하고, 해결된 내용은 doc/d0010_history.md로 이동

---

## 7. 참고 사항

### 7.1 코딩 컨벤션

- PEP 8 스타일 가이드 준수
- Google Style Docstring 사용
- Type Hints 필수 적용
- 함수/클래스명: snake_case / PascalCase
- 상수: UPPER_CASE

### 7.2 Git 커밋 메시지 규칙

```
type(scope): subject

body (optional)
```

- type: feat, fix, docs, style, refactor, test, chore
- 예시: `feat(ocr): add EasyOCR text detection`

### 7.3 필수 확인 사항

- 모든 임시 파일은 tmp/ 폴더에만 생성
- 프로젝트 루트에 .py 파일 생성 금지
- 에러 발생 시 d0004_todo.md에 기록
- 변경 사항은 d0010_history.md에 이력 관리

### 7.4 연관 문서

- doc/d0001_prd.md: 프로젝트 요구사항 정의서
- doc/d0003_test.md: 테스트 가이드
- doc/d0004_todo.md: TODO 및 디버깅
- doc/d0005_lib.md: 라이브러리 문서
- doc/d0010_history.md: 변경 이력

---

## 문서 종료

본 구현 계획은 EasyOCR 제품 라벨 인식 프로젝트의 전체 개발 로드맵을 제시합니다.
프로젝트 진행 중 계획 변경 시 본 문서를 업데이트하고 문서 이력 관리 섹션에 기록합니다.
