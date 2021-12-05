from typing import List, Tuple

with open("input.txt") as f:
    data: list = [line.strip("\n") for line in f]


pairs: List[List[str]] = [pair.split(" -> ") for pair in data]
max_x = max([int(item.split(",")[0]) for pair in pairs for item in pair])
max_y = max([int(item.split(",")[1]) for pair in pairs for item in pair])


def is_diagonal(points: Tuple[Tuple[int, int], Tuple[int, int]]):
    return points[0][0] != points[1][0] and points[0][1] != points[1][1]


def parse_pair(pair: List[str]) -> ((int, int), (int, int)):
    return (int(pair[0].split(",")[0]), int(pair[0].split(",")[1])),\
           (int(pair[1].split(",")[0]), int(pair[1].split(",")[1]))


def mark_points_not_diagonal(vents: List[List[int]], pair: Tuple[Tuple[int, int], Tuple[int, int]]) -> None:
    for y in range(min([pair[0][1], pair[1][1]]), max([pair[0][1], pair[1][1]]) + 1):
        for x in range(min([pair[0][0], pair[1][0]]), max([pair[0][0], pair[1][0]]) + 1):
            vents[y][x] = vents[y][x] + 1


def mark_points_diagonal(vents: List[List[int]], pair: Tuple[Tuple[int, int], Tuple[int, int]]) -> None:
    x_start = pair[0][0]
    y_start = pair[0][1]
    steps = (max(pair, key=lambda x: x[1])[1] - min(pair, key=lambda x: x[1])[1]) + 1
    x_direction = -1 if pair[0][0] - pair[1][0] > 0 else 1
    y_direction = -1 if pair[0][1] - pair[1][1] > 0 else 1
    for step in range(steps):
        vents[y_start + (step * y_direction)][x_start + (step * x_direction)] += 1


def count_intersections(vents: List[List[int]], min_geysers=2) -> int:
    count = 0
    for row in vents:
        for cell in row:
            if cell >= min_geysers:
                count += 1
    return count


def part_1(vents: List[List[int]]) -> int:
    for pair in pairs:
        p = parse_pair(pair)
        if not is_diagonal(p):
            mark_points_not_diagonal(vents, p)

    return count_intersections(vents)


def part_2(vents: List[List[int]]) -> int:
    for pair in pairs:
        p = parse_pair(pair)
        if not is_diagonal(p):
            mark_points_not_diagonal(vents, p)
        else:
            mark_points_diagonal(vents, p)
    return count_intersections(vents)


vent_map = []
for y_coord in range(max_y + 1):
    vent_row = []
    for x_coord in range(max_x + 1):
        vent_row.append(0)
    vent_map.append(vent_row)

print(part_1(vent_map))


vent_map = []
for y_coord in range(max_y + 1):
    vent_row = []
    for x_coord in range(max_x + 1):
        vent_row.append(0)
    vent_map.append(vent_row)

print(part_2(vent_map))
