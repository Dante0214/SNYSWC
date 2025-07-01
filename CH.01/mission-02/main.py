import json

json_file = "mission_computer_main.json"
log_file = "mission_computer_main.log"

logs = []

with open(log_file, "r", encoding="utf-8") as f:
    # 1. 헤더 읽기 및 필드 분리
    header_line = f.readline().strip()
    headers = header_line.split(",")

    # 2. 데이터 처리
    for line in f:
        line = line.strip()
        if not line:
            continue
        fields = line.split(",", len(headers) - 1)  # 헤더 수에 맞게 분리

        # 3. 딕셔너리 형태로 매핑
        log_entry = dict(zip(headers, fields))
        logs.append(log_entry)
print(logs)
# 4. 시간 기준 역순 정렬
logs.sort(reverse=True, key=lambda x: x["timestamp"])

# 5. id 추가 및 최종 리스트 변환
log_list = []
for idx, log in enumerate(logs, start=1):
    log_entry = {
        "id": idx,
        "timestamp": log["timestamp"],
        "event_type": log["event"],
        "message": log["message"]
    }
    log_list.append(log_entry)

# 6. JSON 저장
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(log_list, f, indent=4, ensure_ascii=False)

print(f"=== JSON 파일 '{json_file}' 저장 완료 ===")
