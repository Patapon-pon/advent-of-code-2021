with open("input.txt", "r") as f:
    data = [int(line.strip("\n")) for line in f]

# part 1 solution
# previous = data[0]
# increase_count = 0
#
# for measurement in data[1:]:
#     if measurement > previous:
#         increase_count += 1
#     previous = measurement
#
# print(increase_count)


# part 2 solution
previous = sum(data[:3])
increase_count = 0
for i in range(len(data[1:len(data)-1])):
    increase_thrice = sum(data[i:i+3])
    if increase_thrice > previous:
        increase_count += 1
    previous = increase_thrice

print(increase_count)
