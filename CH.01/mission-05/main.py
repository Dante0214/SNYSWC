import numpy as np

file_paths = [
    "mars_base_main_parts-001.csv",
    "mars_base_main_parts-002.csv",
    "mars_base_main_parts-003.csv",
]

# 각 CSV 파일을 numpy ndarray로 읽어들이기
arr1 = np.genfromtxt(
    file_paths[0], delimiter=",", names=True, dtype=None, encoding="utf-8"
)
arr2 = np.genfromtxt(
    file_paths[1], delimiter=",", names=True, dtype=None, encoding="utf-8"
)
arr3 = np.genfromtxt(
    file_paths[2], delimiter=",", names=True, dtype=None, encoding="utf-8"
)
parts = np.concatenate([arr1, arr2, arr3])
averaged_parts = []
all_parts_name = np.unique(parts[parts.dtype.names[0]])


for part_name in all_parts_name:
    strengths = parts[parts[parts.dtype.names[0]] == part_name][parts.dtype.names[1]]
    avg_strengths = np.round(np.mean(strengths), 3)
    averaged_parts.append((part_name, avg_strengths))
# print(averaged_parts)
parts_below_50 = []
for name, strength in averaged_parts:
    if strength < 50:
        parts_below_50.append((name, strength))
print(parts_below_50)

header_names = ",".join([parts.dtype.names[0], parts.dtype.names[1]])
lines = [header_names]
for name, strength in parts_below_50:
    lines.append(f"{name},{strength}")
# print(lines)
output_content = "\n".join(lines)
# print(output_content)
with open("parts_to_work_on.csv", "w", encoding="utf-8") as f:
    f.write(output_content)
