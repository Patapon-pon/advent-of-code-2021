with open("input.txt", "r") as f:
    data: list = [int(line.strip("\n")) for line in f]


def depth_counter(steps: int) -> int:
    previous = sum(data[:steps])
    depth_increase_counter = 0
    for i in range(len(data[1:len(data)])):
        depth_increase_by_steps = sum(data[i:i+steps])
        if depth_increase_by_steps > previous:
            depth_increase_counter += 1
        previous = depth_increase_by_steps
    return depth_increase_counter


print(depth_counter(1))     # PART 1
print(depth_counter(3))     # PART 2
