with open("input.txt") as f:
    h_positions = [int(pos) for pos in f.readline().split(",")]

h_positions = sorted(h_positions)


def min_fuel_p2(positions) -> int:
    fuel_count = dict()
    avg = sum(h_positions) // len(h_positions)
    median = h_positions[len(h_positions) // 2]
    min_bound = avg - (avg - median)
    max_bound = avg + (avg - median)

    for pos_target in range(min_bound, max_bound):
        fuel_count[pos_target] = 0
        for pos in positions:
            fuel_count[pos_target] += sum(range(abs(pos - pos_target) + 1))

    return min(fuel_count.values())


def min_fuel_p1(positions) -> int:
    fuel_count = dict()
    avg = sum(h_positions) // len(h_positions)
    median = h_positions[len(h_positions) // 2]
    min_bound = avg - (avg - median)
    max_bound = avg + (avg - median)

    for pos_target in range(min_bound, max_bound):
        fuel_count[pos_target] = 0
        for pos in positions:
            fuel_count[pos_target] += abs(pos - pos_target)

    return min(fuel_count.values())


print(min_fuel_p1(h_positions))
print(min_fuel_p2(h_positions))
