"""
EasyOCR 제품 라벨 인식 테스트
Version: v1.0
Author: oais
Date: 2026-01-28
Description: data/01_sample/ 이미지 -> EasyOCR -> data/output/ JSON 결과
"""
import json
import time
from pathlib import Path
import easyocr
import cv2
import numpy as np

# 설정
INPUT_DIR = Path("data/01_sample")
OUTPUT_DIR = Path("data/output")
LANGUAGES = ["ko", "en"]
CONFIDENCE_THRESHOLD = 0.3


def init_reader():
    """EasyOCR Reader 초기화"""
    print(f"EasyOCR Reader 초기화 중... (언어: {', '.join(LANGUAGES)})")
    reader = easyocr.Reader(LANGUAGES, gpu=True)
    print("Reader 초기화 완료")
    return reader


def preprocess_image(image_path):
    """이미지 전처리 (OpenCV)"""
    print(f"  이미지 전처리 중: {image_path.name}")

    # 이미지 로드
    img = cv2.imread(str(image_path))

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 노이즈 제거 (가우시안 블러)
    denoised = cv2.GaussianBlur(gray, (3, 3), 0)

    # 대비 강화 (CLAHE - Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced = clahe.apply(denoised)

    print(f"  전처리 완료: {image_path.name}")
    return enhanced


def run_ocr(reader, image_path):
    """OCR 실행 및 결과 반환"""
    print(f"  OCR 실행 중: {image_path.name}")
    start_time = time.time()

    # 이미지 전처리
    processed_img = preprocess_image(image_path)

    # OCR 실행
    results = reader.readtext(processed_img)

    processing_time = time.time() - start_time
    print(f"  OCR 완료: {image_path.name} (처리시간: {processing_time:.2f}초)")

    # 결과 정리
    ocr_results = []
    total_confidence = 0.0

    for (bbox, text, confidence) in results:
        if confidence >= CONFIDENCE_THRESHOLD:
            ocr_results.append({
                "text": text,
                "confidence": round(confidence, 4),
                "bbox": [[int(x), int(y)] for x, y in bbox]
            })
            total_confidence += confidence

    avg_confidence = round(total_confidence / len(ocr_results), 4) if ocr_results else 0.0

    result = {
        "input_file": image_path.name,
        "processing_time_sec": round(processing_time, 2),
        "results": ocr_results,
        "total_texts": len(ocr_results),
        "avg_confidence": avg_confidence
    }

    return result


def save_result(result, output_path):
    """결과를 JSON으로 저장"""
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"  결과 저장 완료: {output_path.name}")


def process_single_image(reader, image_path):
    """단일 이미지 처리 파이프라인"""
    print(f"\n[처리 시작] {image_path.name}")

    # OCR 실행
    result = run_ocr(reader, image_path)

    # 결과 저장
    output_filename = image_path.stem + "_result.json"
    output_path = OUTPUT_DIR / output_filename
    save_result(result, output_path)

    print(f"[처리 완료] {image_path.name} - 인식된 텍스트: {result['total_texts']}개, 평균 신뢰도: {result['avg_confidence']:.2%}")

    return result


def main():
    """메인 실행"""
    print("=" * 60)
    print("EasyOCR 제품 라벨 인식 테스트 v1.0")
    print("=" * 60)

    # OUTPUT_DIR 생성
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n출력 폴더 확인/생성: {OUTPUT_DIR}")

    # Reader 초기화
    reader = init_reader()

    # 이미지 파일 수집
    image_files = sorted(list(INPUT_DIR.glob("*.png")) + list(INPUT_DIR.glob("*.jpg")))
    print(f"\n처리할 이미지 파일 수: {len(image_files)}개")

    # 이미지 순회 및 처리
    all_results = []
    total_start_time = time.time()

    for image_path in image_files:
        result = process_single_image(reader, image_path)
        all_results.append(result)

    total_processing_time = time.time() - total_start_time

    # 요약 출력
    print("\n" + "=" * 60)
    print("처리 요약")
    print("=" * 60)
    print(f"총 처리 파일 수: {len(all_results)}개")
    print(f"총 처리 시간: {total_processing_time:.2f}초")
    print(f"파일당 평균 처리 시간: {total_processing_time / len(all_results):.2f}초")

    total_texts = sum(r['total_texts'] for r in all_results)
    overall_avg_confidence = sum(r['avg_confidence'] * r['total_texts'] for r in all_results) / total_texts if total_texts > 0 else 0.0

    print(f"총 인식된 텍스트: {total_texts}개")
    print(f"전체 평균 신뢰도: {overall_avg_confidence:.2%}")
    print(f"\n결과 저장 위치: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
