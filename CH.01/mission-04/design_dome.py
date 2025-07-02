# 전역 변수 선언
dome_data = {"재질": None, "지름": None, "두께": None, "면적": None, "무게": None}

# 재질 밀도 (g/cm3)
material_density = {"유리": 2.4, "알루미늄": 2.7, "탄소강": 7.85}

# 화성 중력
MARS_GRAVITY_FACTOR = 0.38


# 돔의 반구 면적 및 무게를 계산하는 함수
def sphere_area(diameter, material="유리", thickness=1):
    global dome_data

    radius = diameter / 2  # 지름 -> 반지름 (단위: m)
    area_m2 = 2 * 3.14 * (radius**2)  # 반구의 겉면적 (m^2)

    area_cm2 = area_m2 * 10000  # m^2 -> cm^2
    volume_cm3 = area_cm2 * thickness  # 부피 (cm^3)
    # 있으면 재질의 밀도 없으면 유리
    density = material_density.get(
        material, material_density["유리"]
    )  # 재질 밀도 (g/cm3)

    weight_g = volume_cm3 * density  # 무게 (g)
    weight_kg = weight_g / 1000  # g -> kg

    # 화성 중력 반영
    weight_kg *= MARS_GRAVITY_FACTOR

    # 결과 소수점 이하 3자리로 반올림
    area_m2 = round(area_m2, 3)
    weight_kg = round(weight_kg, 3)

    # 전역 변수에 저장
    dome_data["재질"] = material
    dome_data["지름"] = diameter
    dome_data["두께"] = thickness
    dome_data["면적"] = area_m2
    dome_data["무게"] = weight_kg


while True:
    material_input = input(
        "재질을 입력하세요 (유리, 알루미늄, 탄소강) 종료하려면 '1' 입력: "
    )
    if material_input == "1":
        print("프로그램을 종료합니다.")
        break

    diameter_input = input("지름을 입력하세요 (m), 0이면 안됨: ")
    try:
        diameter_value = float(diameter_input)
        if diameter_value == 0:
            print("지름은 0이 될 수 없습니다. 다시 입력하세요.")
            continue
    except ValueError:
        print("유효한 숫자를 입력하세요.")
        continue

    thickness_input = input(
        "두께를 입력하세요 (기본값 1cm, Enter 입력 시 기본값 적용): "
    )
    if thickness_input.strip() == "":
        thickness_value = 1
    else:
        try:
            thickness_value = float(thickness_input)
        except ValueError:
            print("유효한 숫자를 입력하세요.")
            continue

    # 함수 호출
    sphere_area(diameter_value, material_input, thickness_value)

    # 출력
    print(
        f"재질 =⇒ {dome_data['재질']}, 지름 =⇒ {dome_data['지름']}, 두께 =⇒ {dome_data['두께']}, 면적 =⇒ {dome_data['면적']}, 무게 =⇒ {dome_data['무게']} kg"
    )
