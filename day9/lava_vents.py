from dataclasses import dataclass
from typing import Type, List


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


def is_lower_adjacent(point: Point) -> bool:
    if point.y > 0 and vent_map[point.y - 1][point.x].value <= point.value:
        return False
    elif point.y < len(vent_map) - 1 and vent_map[point.y + 1][point.x].value <= point.value:
        return False
    elif point.x > 0 and vent_map[point.y][point.x - 1].value <= point.value:
        return False
    elif point.x < len(vent_map[point.y]) - 1 and vent_map[point.y][point.x + 1].value <= point.value:
        return False
    return True


low_points: List[Point] = list(filter(is_lower_adjacent, [cell for row in vent_map for cell in row]))
print(sum([point.value + 1 for point in low_points]))
