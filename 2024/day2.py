import fileinput
from typing import List, Tuple

lines = list(fileinput.input(files="day2.txt"))

def get_min_max_gap(report:List[int]) -> Tuple[int,int]:
    min_gap = -1
    max_gap = -1

    for index in range(1,len(report)):
        size_gap = abs(report[index] - report[index - 1])
        if min_gap == -1 or size_gap < min_gap:
            min_gap = size_gap 
        if max_gap == -1 or size_gap > max_gap:
            max_gap = size_gap 
    
    return min_gap, max_gap 

def is_increasing(report:List[int]) -> bool:
    for index in range(1, len(report)):
        if report[index - 1] > report[index]:
            return False 
    return True 

def is_decreasing(report:List[int]) -> bool:
    for index in range(1, len(report)):
        if report[index - 1] < report[index]:
            return False 
    return True

def is_safe(report:List[int]) -> bool:
    min_gap, max_gap = get_min_max_gap(report)
    is_monotonic = is_increasing(report) or is_decreasing(report)
    has_valid_level_difference = (min_gap >= 1) and (max_gap <= 3)
    return is_monotonic and has_valid_level_difference

reports = []

for line in lines:
    line = line.strip() 
    report = list(map(int, line.split()))
    reports.append(report)

part1 = 0
unsafe_reports = []
for report in reports:
    if is_safe(report):
        part1 += 1
    else:
        unsafe_reports.append(report)

part2 = part1
for unsafe_report in unsafe_reports:
    for index_to_remove in range(len(unsafe_report)):
        report_after_removal = unsafe_report[:index_to_remove] + unsafe_report[index_to_remove + 1:]
        if is_safe(report_after_removal):
            part2 += 1
            break

print(f"part1 = {part1}")
print(f"part2 = {part2}")