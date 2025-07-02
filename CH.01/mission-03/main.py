csv_filepath = "Mars_Base_Inventory_List.csv"
danger_data_csv_filepath = "Mars_Base_Inventory_danger.csv"
data = []
header = []


# CSV 파일 읽기 
try:
    with open(csv_filepath, 'r', encoding='cp949') as file:
        # 헤더 읽기
        header_line = file.readline().strip() # 한 줄을 읽고 양쪽 공백 제거
        header = header_line.split(',') # 쉼표(,)를 기준으로 분리하여 리스트로 저장

        # 데이터 읽기
        for line in file:
            row = line.strip().split(',') # 각 줄을 읽고 쉼표로 분리
            data.append(row)
except FileNotFoundError as e:
    print(e)
except IOError as e:
    print(e)
except Exception as e:
    print(e)

flammability_index = -1
try:
    flammability_index = header.index('Flammability')
except ValueError:
    print("헤더에 Flammability가 없습니다")
    # 에러 처리 로직 추가 (예: 프로그램 종료 또는 기본값 설정

# 마지막 열을 기준으로 내림차순 정렬

data.sort(key=lambda x: float(x[flammability_index]) , reverse=True)
print(data)


# 위험 데이터 필터링 (마지막 열 값이 0.7 이상)
danger_data = []
for row in data:
    if row and len(row) > 0: # 행이 비어있지 않은지 확인
        try:
            if float(row[-1]) >= 0.7:
                danger_data.append(row)
        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)

# 데이터를 새 CSV 파일에 쓰기 
try:    
    with open(danger_data_csv_filepath, 'w', encoding='cp949') as file:
        # 헤더 작성
        file.write(','.join(header) + '\n') # 헤더 리스트를 쉼표로 연결하여 한 줄로 작성
        # 위험 데이터 작성
        for row in danger_data:
            file.write(','.join(row) + '\n') # 각 행의 리스트를 쉼표로 연결하여 한 줄로 작성

except IOError as e:
    print(e)
except Exception as e:
    print(e)