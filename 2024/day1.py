import fileinput

lines = list(fileinput.input(files="day1.txt"))

list_left = []
list_right = []
counter_list_right = dict()

for line in lines:
    x_string, y_string = line.strip().split()
    x_int, y_int = int(x_string), int(y_string)
    list_left.append(x_int)
    list_right.append(y_int)

    if y_int not in set(counter_list_right.keys()):
        counter_list_right[y_int] = 0
    counter_list_right[y_int] += 1 

list_left.sort()
list_right.sort()
part1 = sum([abs(x-y) for (x,y) in zip(list_left,list_right)])

part2 = 0 
for elem in list_left:
    if elem in set(counter_list_right.keys()):
        part2 += elem * counter_list_right[elem]

print(f"part1 = {part1}")
print(f"part2 = {part2}")