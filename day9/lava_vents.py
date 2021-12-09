from dataclasses import dataclass
from functools import reduce
from typing import List


@dataclass
class Point:
    y: int
    x: int
    value: int


with open("input.txt") as f:
    vent_map: List[List[Point]] = []
    for y, line in enumerate(f):
        line = line.strip("\n")
        row = []
        for x, cell in enumerate(line):
            row.append(Point(y, x, int(cell)))
        vent_map.append(row)


def get_adjacent_points(point: Point) -> List[Point]:
    adjacent_points = []
    if point.y > 0:
        adjacent_points.append(vent_map[point.y - 1][point.x])
    if point.y < len(vent_map) - 1:
        adjacent_points.append(vent_map[point.y + 1][point.x])
    if point.x > 0:
        adjacent_points.append(vent_map[point.y][point.x - 1])
    if point.x < len(vent_map[point.y]) - 1:
        adjacent_points.append(vent_map[point.y][point.x + 1])
    return adjacent_points


def is_lower_adjacent(point: Point) -> bool:
    for neighbor in get_adjacent_points(point):
        if neighbor.value <= point.value:
            return False
    return True


def find_basin_size(start: Point) -> int:
    """
    Count the points inside the basin using breadth-first search.
    Ignore points with value of 9.

    :param start: starting point
    :return: size of the basin
    """
    size = 0
    queue = [start]
    visited = [start]
    while len(queue) != 0:
        current = queue.pop(0)
        size += 1
        for neighbor in get_adjacent_points(current):
            if neighbor.value == 9:
                continue
            diff = neighbor.value - current.value
            if diff > 0 and neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
    return size


# PART 1
low_points: List[Point] = list(filter(is_lower_adjacent, [cell for row in vent_map for cell in row]))
print(sum([point.value + 1 for point in low_points]))

# PART 2
basin_sizes: List[int] = [find_basin_size(point) for point in low_points]
print(reduce(lambda a, b: a * b, list(sorted(basin_sizes))[-3:]))
