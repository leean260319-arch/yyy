#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""모든 oais 스킬에 version 서브명령어 추가"""

import re
from pathlib import Path

V_DIR = Path(__file__).parent.parent / "v"

def get_skill_name(filepath: Path) -> str:
    """파일명에서 스킬명 추출 (예: oaisenv.md -> oaisenv)"""
    return filepath.stem

def get_current_version(content: str) -> str:
    """문서 이력 관리에서 최신 버전 추출"""
    # | v07 | 2026-01-26 | ... 형식에서 버전 추출
    match = re.search(r'\|\s*(v[\d.]+)\s*\|', content)
    if match:
        return match.group(1)
    return "v01"

def add_version_command(filepath: Path) -> bool:
    """version 서브명령어 추가"""
    content = filepath.read_text(encoding='utf-8')
    skill_name = get_skill_name(filepath)
    version = get_current_version(content)

    # 이미 version 명령어가 있는지 확인
    if f'`{skill_name} version`' in content:
        print(f"[SKIP] {filepath.name}: version 명령어 이미 존재")
        return False

    # 서브명령어 테이블 찾기
    # 패턴 1: "| 명령어 | 설명 |" 또는 "| 명령어 | 설명 | 출력 |"
    # 패턴 2: "| `skill status` | ... |" 형식의 첫 번째 행 찾기

    # 테이블 헤더 찾기
    table_patterns = [
        r'(\|\s*명령어\s*\|\s*설명\s*\|\s*출력\s*\|\n\|[-|]+\n)',  # 3열
        r'(\|\s*명령어\s*\|\s*설명\s*\|\n\|[-|]+\n)',  # 2열
    ]

    for pattern in table_patterns:
        match = re.search(pattern, content)
        if match:
            # status 명령어 행 찾기
            status_pattern = rf'(\| `{skill_name} status`[^\n]+\n)'
            status_match = re.search(status_pattern, content)

            if status_match:
                # status 행 다음에 version 추가
                if '| 출력 |' in match.group(1):
                    version_row = f'| `{skill_name} version` | 스킬 버전 정보 ({version}) | 터미널 |\n'
                else:
                    version_row = f'| `{skill_name} version` | 스킬 버전 정보 ({version}) |\n'

                new_content = content.replace(
                    status_match.group(1),
                    status_match.group(1) + version_row
                )
                filepath.write_text(new_content, encoding='utf-8')
                print(f"[OK] {filepath.name}: version 명령어 추가 ({version})")
                return True
            else:
                # status가 없으면 테이블 헤더 다음에 추가
                if '| 출력 |' in match.group(1):
                    version_row = f'| `{skill_name} version` | 스킬 버전 정보 ({version}) | 터미널 |\n'
                else:
                    version_row = f'| `{skill_name} version` | 스킬 버전 정보 ({version}) |\n'

                insert_pos = match.end()
                new_content = content[:insert_pos] + version_row + content[insert_pos:]
                filepath.write_text(new_content, encoding='utf-8')
                print(f"[OK] {filepath.name}: version 명령어 추가 (테이블 시작) ({version})")
                return True

    # 서브명령어 섹션 찾기 (## 서브명령어 또는 ## 2. 서브명령어)
    section_match = re.search(r'(##\s*\d*\.?\s*서브명령어\s*\n+)', content)
    if section_match:
        # 간단한 테이블 추가
        version_table = f"""
| 명령어 | 설명 |
|--------|------|
| `{skill_name} version` | 스킬 버전 정보 ({version}) |

"""
        insert_pos = section_match.end()
        new_content = content[:insert_pos] + version_table + content[insert_pos:]
        filepath.write_text(new_content, encoding='utf-8')
        print(f"[OK] {filepath.name}: version 테이블 생성 ({version})")
        return True

    print(f"[WARN] {filepath.name}: 서브명령어 섹션을 찾을 수 없음")
    return False

def main():
    print("# oais 스킬 version 서브명령어 추가\n")

    oais_files = sorted(V_DIR.glob("oais*.md"))
    print(f"대상 파일: {len(oais_files)}개\n")

    success = 0
    skip = 0
    fail = 0

    for filepath in oais_files:
        result = add_version_command(filepath)
        if result:
            success += 1
        elif result is False:
            skip += 1
        else:
            fail += 1

    print(f"\n## 결과")
    print(f"- 추가: {success}")
    print(f"- 스킵: {skip}")
    print(f"- 실패: {fail}")

if __name__ == "__main__":
    main()
