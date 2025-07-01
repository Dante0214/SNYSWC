print('Hello Mars')
arr=[]
try:
    with open("mission_computer_main.log",'r',encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        for line in f:
            line = line.strip().split(',')
            if len(line) ==len(header):
               arr.append(dict(zip(header,line)))
            # print(line)
            arr.append(line)

except FileNotFoundError as e:
   print(e)
except PermissionError as e:
   print(e)
except UnicodeDecodeError as e:
   print(e)
except IOError as e:
   print(e)

print(arr)
# print(arr[0])
# dictionaries = [{arr[i][j]: arr[i][j+1] for j in range(0, len(arr[i]), 2)} for i in range(len(arr))]
# print(dictionaries)
# print(arr)
# mission_computer_main.log 파일을 읽어들여서 출력한다. 콤마를 기준으로 날짜 및 시간과 로그 내용을 분류해서 Python의 리스트(List) 객체로 전환한다.
# (여기서 말하는 리스트는 배열이 아니라 파이썬에서 제공하는 리스트 타입의 객체를 의미한다.)
# 전환된 리스트 객체를 화면에 출력한다.
# 리스트 객체를 시간의 역순으로 정렬(sort)한다.
# 리스트 객체를 사전(Dict) 객체로 전환한다.
# 사전 객체로 전환된 내용을 mission_computer_main.json 파일로 저장하는데 파일 포멧은 JSON(JavaScript Ontation)으로 저장한다.

# ,로 슬라이싱 하고 이차원배열로 arr[i][0] 솔트 