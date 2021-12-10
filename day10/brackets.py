with open("input.txt") as f:
    syntax_lines = [line.strip("\n") for line in f]


opening_brackets = ["(", "[", "{", "<"]
closing_brackets = [")", "]", "}", ">"]
error_points = [3, 57, 1197, 25137]
correction_points = [1, 2, 3, 4]

error_scores = dict(
    zip(closing_brackets, error_points)
)
correction_scores = dict(
    zip(opening_brackets, correction_points)
)

open_to_close_brackets = dict(
    zip(opening_brackets, closing_brackets)
)


def find_error(line):
    current = line[0]
    stack = []
    for bracket in line[1:]:
        if bracket in opening_brackets:
            if current:
                stack.append(current)
            current = bracket
            continue
        if open_to_close_brackets[current] == bracket:
            if len(stack) != 0:
                current = stack.pop()
            else:
                current = None
        else:
            return bracket
    else:
        stack.append(current)
    return ["".join(stack)]


def part1():

    mistakes = []
    incomplete = []
    for line in syntax_lines:
        result = find_error(line)
        if isinstance(result, str):
            mistakes.append(result)
        else:
            incomplete.append("".join(result))
    print(sum([error_scores[bracket] for bracket in mistakes]))
    return incomplete


def part2(brackets: list):
    scores = []
    for unclosed_brackets in brackets:
        current_score = 0
        for bracket in reversed(unclosed_brackets):
            current_score = current_score * 5 + correction_scores[bracket]
        scores.append(current_score)
    middle = len(scores) // 2
    print(list(sorted(scores))[middle])


if __name__ == "__main__":
    todo = part1()
    print(correction_scores)
    part2(todo)