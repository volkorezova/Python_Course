# Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність
# дублікатів і приберіть їх. Результат запишіть у файл result_<your_second_name>.csv
import csv

file1 = "random.csv"
file2 = "random-michaels.csv"

rows1 = []
rows2 = []

# read the first csv file
with open(file1, encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    rows1 = list(reader)

# read the second csv file
with open(file2, encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # пропускаємо header
    rows2 = list(reader)

duplicates = []
for row in rows1:
    if row in rows2:
        duplicates.append(row)

# remove duplicates
unique_rows = [row for row in rows1 if row not in duplicates]

with open("result_volkorezova.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(unique_rows)

print("Result saved to result_volkorezova.csv")
