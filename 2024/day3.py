import fileinput
import re
from typing import Tuple

text = ''.join(fileinput.input(files="day3.txt"))

def parse_prefix(pattern:str, text:str) -> Tuple[int, bool]:
    if text.startswith(pattern):
        return text[len(pattern):], True
    else:
        return "", False

def parse_number(text:str) -> Tuple[int, str, bool]:
    number_str = re.match(r"\d+", text)
    if number_str:
        number_str = number_str.group()
        text_remain = text[len(number_str):]
        return int(number_str), text_remain, True 
    else:
        return -1,"", False
    

def compute_multiplication_score(text:str) -> int:
    text, flag_mul_lbracket = parse_prefix("mul(", text)
    number_left, text, flag_number_left = parse_number(text)
    text, flag_comma = parse_prefix(",", text)
    number_right, text, flag_number_right = parse_number(text)
    text, flab_rbracket = parse_prefix(")", text)
    flag = flag_mul_lbracket and flag_number_left and flag_comma and flag_number_right and flab_rbracket 

    if flag and 0 <= len(str(number_left)) <= 3 and 0 <= len(str(number_right)) <= 3:
        return number_left * number_right 
    else:
        return 0



part1 = 0
part2 = 0
is_enabled = True
for index_start in range(len(text)):
    subtext = text[index_start:]
    if parse_prefix("do()", subtext)[1]:
        is_enabled = True 
    if parse_prefix("don't()", subtext)[1]:
        is_enabled = False

    score = compute_multiplication_score(subtext)
    
    part1 += score
    if is_enabled:
        part2 += score

print(f"part1 = {part1}")
print(f"part2 = {part2}")