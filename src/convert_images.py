"""
이미지 포맷 변환기
Version: v1.0
Author: oais
Date: 2026-01-29
Description: data/01_sample/의 이미지들을 JPG로 변환
"""

import os
from pathlib import Path
from PIL import Image

# 설정
INPUT_DIR = Path("data/01_sample")
OUTPUT_DIR = Path("data/converted_jpg")
TARGET_FILES = [f"{i:02d}" for i in range(1, 16)]  # 01~15


def convert_to_jpg(input_path, output_path):
    """이미지를 JPG로 변환"""
    try:
        print(f"  변환 중: {input_path.name} -> JPG")

        # 이미지 열기
        with Image.open(input_path) as img:
            # 이미지가 RGB가 아니면 RGB로 변환
            if img.mode in ("RGBA", "LA", "P"):
                # 투명한 배경을 흰색으로
                background = Image.new("RGB", img.size, (255, 255, 255))
                if img.mode == "P":
                    img = img.convert("RGBA")
                if img.mode in ("RGBA", "LA"):
                    background.paste(img, mask=img.split()[-1])  # alpha channel as mask
                img = background
            elif img.mode != "RGB":
                img = img.convert("RGB")

            # JPG로 저장
            img.save(output_path, "JPEG", quality=95, optimize=True)

        print(f"  변환 완료: {output_path.name}")
        return True

    except Exception as e:
        print(f"  변환 실패: {input_path.name} - 에러: {str(e)}")
        return False


def find_image_file(base_name, directory):
    """숫자 기본 이름으로 이미지 파일 찾기"""
    extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"]

    for ext in extensions:
        file_path = directory / (base_name + ext)
        if file_path.exists():
            return file_path

    return None


def main():
    """메인 실행"""
    print("=" * 60)
    print("이미지 포맷 변환기 v1.0")
    print("=" * 60)

    # 출력 디렉토리 생성
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n출력 디렉토리: {OUTPUT_DIR}")

    converted_count = 0
    failed_count = 0

    print(f"\n총 {len(TARGET_FILES)}개 파일 처리 시작...")

    for base_name in TARGET_FILES:
        print(f"\n[{base_name}] 처리 중...")

        # 입력 파일 찾기
        input_file = find_image_file(base_name, INPUT_DIR)

        if input_file is None:
            print(f"  [에러] 파일 없음: {base_name}.*")
            failed_count += 1
            continue

        print(f"  [발견] {input_file.name}")

        # 출력 파일 경로
        output_file = OUTPUT_DIR / f"{base_name}.jpg"

        # 변환
        if convert_to_jpg(input_file, output_file):
            converted_count += 1
        else:
            failed_count += 1

    # 요약
    print("\n" + "=" * 60)
    print("변환 요약")
    print("=" * 60)
    print(f"총 대상 파일: {len(TARGET_FILES)}개")
    print(f"변환 성공: {converted_count}개")
    print(f"변환 실패: {failed_count}개")
    print(f"출력 위치: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
