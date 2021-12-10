with open("input.txt") as f:
    syntax_lines = [line.strip("\n") for line in f]


class MissingBracketException(Exception):
    error: str

    def __init__(self, reason, error_sign):
        super().__init__(reason)
        self.error = error_sign


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


def find_missing_brackets(line):
    stack = []
    current = None
    for bracket in line:
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
            raise MissingBracketException(f"{bracket} was found instead of {open_to_close_brackets[current]}", bracket)
    else:
        stack.append(current)
    return stack


def part1():

    mistakes = []
    incomplete = []
    for line in syntax_lines:
        try:
            result = find_missing_brackets(line)
            incomplete.append("".join(result))
        except MissingBracketException as exception:
            mistakes.append(exception.error)
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
    part2(part1())