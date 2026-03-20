"""
Sample Label Image Generator for OCR Testing
Version: 1.0.0
Description: Generate 10 sample product label images with Korean and English text
"""

from PIL import Image, ImageDraw, ImageFont
import os

def get_font(size=20, korean=False):
    """Get font for text rendering"""
    try:
        if korean:
            # Try Korean fonts
            font_paths = [
                "C:/Windows/Fonts/malgun.ttf",  # Malgun Gothic
                "C:/Windows/Fonts/gulim.ttc",   # Gulim
                "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",  # Linux
            ]
            for path in font_paths:
                if os.path.exists(path):
                    return ImageFont.truetype(path, size)
        else:
            # Try English fonts
            font_paths = [
                "C:/Windows/Fonts/arial.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            ]
            for path in font_paths:
                if os.path.exists(path):
                    return ImageFont.truetype(path, size)
    except:
        pass

    # Fallback to default font
    return ImageFont.load_default()

def create_label_food_01():
    """식품 라벨 - 한국어"""
    img = Image.new('RGB', (700, 500), color='white')
    draw = ImageDraw.Draw(img)

    font_title = get_font(36, korean=True)
    font_normal = get_font(20, korean=True)
    font_small = get_font(16, korean=True)

    y = 30
    draw.text((50, y), "유기농 현미 누룽지", fill='black', font=font_title)
    y += 60
    draw.text((50, y), "제조일자: 2024-01-15", fill='black', font=font_normal)
    y += 35
    draw.text((50, y), "유통기한: 2024-07-15", fill='black', font=font_normal)
    y += 45
    draw.text((50, y), "[영양성분]", fill='black', font=font_normal)
    y += 35
    draw.text((50, y), "열량: 380kcal (1회 제공량 100g당)", fill='black', font=font_small)
    y += 30
    draw.text((50, y), "탄수화물 85g, 단백질 7g, 지방 2g", fill='black', font=font_small)
    y += 30
    draw.text((50, y), "나트륨 5mg, 당류 0g", fill='black', font=font_small)
    y += 45
    draw.text((50, y), "원재료: 유기농현미 100%", fill='black', font=font_small)
    y += 35
    draw.text((50, y), "제조사: (주)건강식품", fill='black', font=font_small)

    return img

def create_label_food_02():
    """음료 라벨 - 한국어+영어 혼합"""
    img = Image.new('RGB', (650, 450), color='#FFF8DC')
    draw = ImageDraw.Draw(img)

    font_title = get_font(32, korean=True)
    font_normal = get_font(18, korean=True)
    font_eng = get_font(16, korean=False)

    y = 25
    draw.text((40, y), "제주 감귤 주스", fill='#FF6347', font=font_title)
    y += 50
    draw.text((40, y), "Jeju Tangerine Juice 100%", fill='#FF6347', font=font_eng)
    y += 45
    draw.text((40, y), "내용량: 500ml", fill='black', font=font_normal)
    y += 35
    draw.text((40, y), "유통기한: 2024-06-30", fill='black', font=font_normal)
    y += 40
    draw.text((40, y), "원재료: 제주감귤농축액 30%, 정제수, 설탕", fill='black', font=font_normal)
    y += 35
    draw.text((40, y), "비타민C, 구연산", fill='black', font=font_normal)
    y += 50
    draw.text((40, y), "보관방법: 개봉 후 냉장보관", fill='black', font=font_normal)
    y += 35
    draw.text((40, y), "Customer Service: 1588-1234", fill='black', font=font_eng)

    return img

def create_label_food_03():
    """과자 라벨 - 한국어"""
    img = Image.new('RGB', (750, 520), color='#FFFACD')
    draw = ImageDraw.Draw(img)

    font_title = get_font(38, korean=True)
    font_normal = get_font(19, korean=True)
    font_small = get_font(15, korean=True)

    y = 35
    draw.text((55, y), "초코칩 쿠키", fill='#8B4513', font=font_title)
    y += 55
    draw.text((55, y), "Choco Chip Cookie", fill='#8B4513', font=get_font(22, korean=False))
    y += 50
    draw.text((55, y), "중량: 200g (10개입)", fill='black', font=font_normal)
    y += 35
    draw.text((55, y), "제조일: 2024-01-20 / 유통기한: 2024-04-20", fill='black', font=font_normal)
    y += 45
    draw.text((55, y), "원재료명:", fill='black', font=font_normal)
    y += 32
    draw.text((55, y), "밀가루, 설탕, 버터, 초코칩(카카오매스, 코코아버터),", fill='black', font=font_small)
    y += 28
    draw.text((55, y), "달걀, 베이킹파우더, 소금, 바닐라향", fill='black', font=font_small)
    y += 40
    draw.text((55, y), "알레르기 유발성분: 밀, 우유, 대두, 계란 함유", fill='red', font=font_normal)
    y += 45
    draw.text((55, y), "제조원: 달콤제과 주식회사", fill='black', font=font_small)

    return img

def create_label_cosmetic_01():
    """화장품 라벨 - 영어 위주"""
    img = Image.new('RGB', (680, 480), color='#F0F8FF')
    draw = ImageDraw.Draw(img)

    font_title = get_font(34, korean=False)
    font_normal = get_font(17, korean=False)
    font_small = get_font(14, korean=False)

    y = 30
    draw.text((45, y), "HYDRATING ESSENCE", fill='#4169E1', font=font_title)
    y += 50
    draw.text((45, y), "Moisture Boosting Formula", fill='#4169E1', font=get_font(20, korean=False))
    y += 45
    draw.text((45, y), "Net Wt: 50ml / 1.69 fl.oz", fill='black', font=font_normal)
    y += 35
    draw.text((45, y), "Exp Date: 2025-12-31", fill='black', font=font_normal)
    y += 45
    draw.text((45, y), "Key Ingredients:", fill='black', font=font_normal)
    y += 30
    draw.text((45, y), "Hyaluronic Acid, Niacinamide, Ceramide,", fill='black', font=font_small)
    y += 25
    draw.text((45, y), "Glycerin, Panthenol, Beta-Glucan", fill='black', font=font_small)
    y += 40
    draw.text((45, y), "Directions: Apply to face after cleansing.", fill='black', font=font_small)
    y += 25
    draw.text((45, y), "Gently pat until fully absorbed.", fill='black', font=font_small)
    y += 40
    draw.text((45, y), "Made in Korea", fill='black', font=font_normal)

    return img

def create_label_cosmetic_02():
    """스킨케어 라벨 - 한국어+영어"""
    img = Image.new('RGB', (720, 500), color='#FFF0F5')
    draw = ImageDraw.Draw(img)

    font_title = get_font(35, korean=True)
    font_normal = get_font(18, korean=True)
    font_eng = get_font(16, korean=False)

    y = 28
    draw.text((48, y), "수분 진정 크림", fill='#DA70D6', font=font_title)
    y += 48
    draw.text((48, y), "Soothing Moisture Cream", fill='#DA70D6', font=font_eng)
    y += 48
    draw.text((48, y), "용량: 100ml", fill='black', font=font_normal)
    y += 35
    draw.text((48, y), "사용기한: 개봉 후 12개월", fill='black', font=font_normal)
    y += 42
    draw.text((48, y), "주요성분: 센텔라아시아티카추출물, 히알루론산,", fill='black', font=get_font(16, korean=True))
    y += 30
    draw.text((48, y), "판테놀, 알로에베라잎추출물", fill='black', font=get_font(16, korean=True))
    y += 45
    draw.text((48, y), "사용방법: 기초 단계 마지막에 적당량을 얼굴에", fill='black', font=get_font(16, korean=True))
    y += 28
    draw.text((48, y), "골고루 펴 발라줍니다.", fill='black', font=get_font(16, korean=True))
    y += 45
    draw.text((48, y), "제조국: 대한민국", fill='black', font=font_normal)

    return img

def create_label_medicine_01():
    """의약품 라벨 - 한국어"""
    img = Image.new('RGB', (700, 550), color='white')
    draw = ImageDraw.Draw(img)

    font_title = get_font(30, korean=True)
    font_normal = get_font(18, korean=True)
    font_small = get_font(15, korean=True)

    y = 25
    draw.text((45, y), "[일반의약품] 해열진통제", fill='red', font=font_title)
    y += 50
    draw.text((45, y), "제품명: 아세트정 500mg", fill='black', font=font_normal)
    y += 38
    draw.text((45, y), "효능효과: 두통, 치통, 발열, 근육통, 생리통", fill='black', font=font_normal)
    y += 40
    draw.text((45, y), "용법용량:", fill='black', font=font_normal)
    y += 32
    draw.text((45, y), "성인 1회 1정, 1일 3회, 식후 30분 복용", fill='black', font=font_small)
    y += 28
    draw.text((45, y), "4시간 이상 간격을 두고 복용", fill='black', font=font_small)
    y += 40
    draw.text((45, y), "사용기한: 2026-03-31", fill='black', font=font_normal)
    y += 38
    draw.text((45, y), "주의사항:", fill='red', font=font_normal)
    y += 32
    draw.text((45, y), "- 임산부, 수유부는 복용 전 의사와 상담", fill='red', font=font_small)
    y += 28
    draw.text((45, y), "- 어린이의 손이 닿지 않는 곳에 보관", fill='red', font=font_small)
    y += 28
    draw.text((45, y), "- 직사광선을 피하여 보관", fill='red', font=font_small)
    y += 45
    draw.text((45, y), "제조사: 건강제약(주)", fill='black', font=font_small)

    return img

def create_label_medicine_02():
    """건강보조식품 라벨 - 한국어+영어"""
    img = Image.new('RGB', (730, 520), color='#F5F5DC')
    draw = ImageDraw.Draw(img)

    font_title = get_font(32, korean=True)
    font_normal = get_font(18, korean=True)
    font_eng = get_font(15, korean=False)

    y = 28
    draw.text((48, y), "프리미엄 멀티비타민", fill='#006400', font=font_title)
    y += 48
    draw.text((48, y), "Premium Multi-Vitamin Complex", fill='#006400', font=font_eng)
    y += 48
    draw.text((48, y), "내용량: 90정 (3개월분)", fill='black', font=font_normal)
    y += 35
    draw.text((48, y), "1일 섭취량: 1정 (식사 후)", fill='black', font=font_normal)
    y += 42
    draw.text((48, y), "주요성분 (1정당):", fill='black', font=font_normal)
    y += 32
    draw.text((48, y), "비타민A 700ug, 비타민C 100mg, 비타민D 10ug,", fill='black', font=get_font(15, korean=True))
    y += 28
    draw.text((48, y), "비타민E 11mg, 비타민B1 1.2mg, 비타민B2 1.4mg,", fill='black', font=get_font(15, korean=True))
    y += 28
    draw.text((48, y), "비타민B6 1.5mg, 비타민B12 2.4ug, 엽산 400ug", fill='black', font=get_font(15, korean=True))
    y += 42
    draw.text((48, y), "기능성: 항산화, 면역기능, 뼈 건강, 에너지 생성", fill='black', font=font_normal)
    y += 45
    draw.text((48, y), "유통기한: 2025-08-31", fill='black', font=font_normal)
    y += 35
    draw.text((48, y), "제조원: 뉴트리헬스(주)", fill='black', font=get_font(16, korean=True))

    return img

def create_label_electronics_01():
    """전자제품 라벨 - 영어+숫자"""
    img = Image.new('RGB', (660, 460), color='#E8E8E8')
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, korean=False)
    font_normal = get_font(16, korean=False)
    font_small = get_font(14, korean=False)

    y = 25
    draw.text((42, y), "WIRELESS EARBUDS PRO", fill='#1C1C1C', font=font_title)
    y += 45
    draw.text((42, y), "Model: WE-2024-BT5.3", fill='black', font=font_normal)
    y += 35
    draw.text((42, y), "Specifications:", fill='black', font=font_normal)
    y += 30
    draw.text((42, y), "- Bluetooth Version: 5.3", fill='black', font=font_small)
    y += 25
    draw.text((42, y), "- Battery Life: Up to 8 hours", fill='black', font=font_small)
    y += 25
    draw.text((42, y), "- Charging Time: 1.5 hours", fill='black', font=font_small)
    y += 25
    draw.text((42, y), "- Frequency Range: 20Hz - 20kHz", fill='black', font=font_small)
    y += 25
    draw.text((42, y), "- Input: DC 5V 500mA", fill='black', font=font_small)
    y += 35
    draw.text((42, y), "Safety Certifications: CE, FCC, RoHS", fill='black', font=font_normal)
    y += 35
    draw.text((42, y), "Serial No: WE2024KR0012345", fill='black', font=font_small)
    y += 30
    draw.text((42, y), "Made in Korea", fill='black', font=font_normal)
    y += 30
    draw.text((42, y), "Date of Manufacture: 2024-01-10", fill='black', font=font_small)

    return img

def create_label_mixed_01():
    """혼합 라벨 - 한국어+영어+숫자"""
    img = Image.new('RGB', (740, 510), color='#FAFAD2')
    draw = ImageDraw.Draw(img)

    font_title = get_font(33, korean=True)
    font_normal = get_font(18, korean=True)
    font_eng = get_font(16, korean=False)

    y = 30
    draw.text((50, y), "유기농 프리미엄 녹차", fill='#2F4F2F', font=font_title)
    y += 50
    draw.text((50, y), "Organic Premium Green Tea", fill='#2F4F2F', font=font_eng)
    y += 45
    draw.text((50, y), "제품코드: GT-2024-ORG-001", fill='black', font=get_font(16, korean=False))
    y += 35
    draw.text((50, y), "중량: 100g (티백 50개, 2g x 50)", fill='black', font=font_normal)
    y += 35
    draw.text((50, y), "원산지: 전라남도 보성 (100% 국내산)", fill='black', font=font_normal)
    y += 38
    draw.text((50, y), "제조일자: 2024-01-05", fill='black', font=font_normal)
    y += 30
    draw.text((50, y), "유통기한: 2025-01-04 (제조일로부터 12개월)", fill='black', font=font_normal)
    y += 45
    draw.text((50, y), "인증: 유기농인증 EU-Organic, USDA Organic", fill='black', font=get_font(15, korean=True))
    y += 40
    draw.text((50, y), "보관방법: 직사광선을 피하고 서늘한 곳에 보관", fill='black', font=get_font(16, korean=True))
    y += 40
    draw.text((50, y), "Customer Service: 1588-5678", fill='black', font=font_eng)
    y += 30
    draw.text((50, y), "제조사: (주)보성녹차 / www.bosungtea.kr", fill='black', font=get_font(15, korean=True))

    return img

def create_label_mixed_02():
    """복잡한 라벨 - 여러 줄 텍스트"""
    img = Image.new('RGB', (780, 600), color='white')
    draw = ImageDraw.Draw(img)

    # Draw border
    draw.rectangle([(10, 10), (770, 590)], outline='black', width=2)

    font_title = get_font(34, korean=True)
    font_subtitle = get_font(22, korean=True)
    font_normal = get_font(17, korean=True)
    font_small = get_font(14, korean=True)
    font_eng = get_font(15, korean=False)

    y = 25
    draw.text((60, y), "프리미엄 건강기능식품", fill='#8B0000', font=font_title)
    y += 50
    draw.text((60, y), "홍삼 진액 골드", fill='#8B0000', font=font_subtitle)
    y += 42
    draw.text((60, y), "Korean Red Ginseng Extract Gold", fill='#8B0000', font=font_eng)
    y += 50
    draw.text((60, y), "[제품 정보]", fill='black', font=font_normal)
    y += 32
    draw.text((60, y), "내용량: 70ml x 30포 (총 2,100ml)", fill='black', font=font_small)
    y += 25
    draw.text((60, y), "1일 섭취량: 1포 (70ml), 아침 공복 또는 식후 섭취", fill='black', font=font_small)
    y += 25
    draw.text((60, y), "제조일자: 2024-02-01 / 유통기한: 2026-01-31", fill='black', font=font_small)
    y += 40
    draw.text((60, y), "[원료 및 함량] 1포(70ml)당", fill='black', font=font_normal)
    y += 30
    draw.text((60, y), "홍삼농축액 6,000mg (6년근 홍삼 30% 함유)", fill='black', font=font_small)
    y += 25
    draw.text((60, y), "진세노사이드 Rg1+Rb1+Rg3: 6mg", fill='black', font=font_small)
    y += 25
    draw.text((60, y), "부원료: 대추농축액, 생강농축액, 구기자추출물,", fill='black', font=font_small)
    y += 22
    draw.text((60, y), "꿀, 정제수", fill='black', font=font_small)
    y += 38
    draw.text((60, y), "[기능성 내용]", fill='black', font=font_normal)
    y += 28
    draw.text((60, y), "1. 면역력 증진에 도움을 줄 수 있음", fill='black', font=font_small)
    y += 22
    draw.text((60, y), "2. 피로 개선에 도움을 줄 수 있음", fill='black', font=font_small)
    y += 22
    draw.text((60, y), "3. 혈소판 응집억제를 통한 혈액흐름에 도움", fill='black', font=font_small)
    y += 22
    draw.text((60, y), "4. 기억력 개선에 도움을 줄 수 있음", fill='black', font=font_small)
    y += 38
    draw.text((60, y), "[섭취 시 주의사항]", fill='red', font=font_normal)
    y += 28
    draw.text((60, y), "특정 질환, 임산부, 수유부는 섭취 전 전문가 상담", fill='red', font=font_small)
    y += 22
    draw.text((60, y), "알레르기 체질은 성분 확인 후 섭취", fill='red', font=font_small)
    y += 38
    draw.text((60, y), "제조사: (주)고려인삼공사 / 충남 금산군", fill='black', font=font_small)
    y += 25
    draw.text((60, y), "고객센터: 080-123-4567 / www.koreanginseng.co.kr", fill='black', font=font_small)

    return img

def main():
    """Generate all sample label images"""
    # Create output directory if it doesn't exist
    output_dir = "data/01_sample"
    os.makedirs(output_dir, exist_ok=True)

    # Generate images
    labels = [
        ("label_food_01.png", create_label_food_01()),
        ("label_food_02.png", create_label_food_02()),
        ("label_food_03.png", create_label_food_03()),
        ("label_cosmetic_01.png", create_label_cosmetic_01()),
        ("label_cosmetic_02.png", create_label_cosmetic_02()),
        ("label_medicine_01.png", create_label_medicine_01()),
        ("label_medicine_02.png", create_label_medicine_02()),
        ("label_electronics_01.png", create_label_electronics_01()),
        ("label_mixed_01.png", create_label_mixed_01()),
        ("label_mixed_02.png", create_label_mixed_02()),
    ]

    print("Starting sample label image generation...")
    print(f"Output directory: {output_dir}")
    print()

    for filename, img in labels:
        filepath = os.path.join(output_dir, filename)
        img.save(filepath)
        print(f"Generated: {filename} ({img.size[0]}x{img.size[1]})")

    print()
    print(f"Successfully generated {len(labels)} sample label images!")
    print(f"All images saved to: {output_dir}")

if __name__ == "__main__":
    main()
