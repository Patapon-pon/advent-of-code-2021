BINGO_SUM_FOR_ROW_COL = -5


def load_data() -> (list, list):
    with open("input.txt", "r") as f:
        inputs = [int(item.strip("\n")) for item in f.readline().split(",")]
        boards = []

        board = []
        rest = f.readlines()
        for row in rest:
            row = row.strip("\n")
            if len(row) == 0:
                continue
            board.append([int(cell) for cell in row.split()])
            if len(board) == 5:
                boards.append(board)
                board = []
        return inputs, boards


guess_numbers, bingo_boards = load_data()


def mark_bingo_boards(number: int) -> None:
    for bingo_board in bingo_boards:
        for y, row in enumerate(bingo_board):
            for x, cell in enumerate(row):
                if cell == number:
                    bingo_board[y][x] = -1


def check_for_many_bingo() -> list:
    bingos = []
    for bingo_board in bingo_boards:
        for y, row in enumerate(bingo_board):
            if sum(row) == BINGO_SUM_FOR_ROW_COL:
                bingos.append(bingo_board)
        for column in zip(*bingo_board):
            if sum(column) == BINGO_SUM_FOR_ROW_COL:
                if bingo_board not in bingos:
                    bingos.append(bingo_board)
    return bingos


def check_for_bingo() -> list:
    for bingo_board in bingo_boards:
        for y, row in enumerate(bingo_board):
            if sum(row) == BINGO_SUM_FOR_ROW_COL:
                return bingo_board
        for column in zip(*bingo_board):
            if sum(column) == BINGO_SUM_FOR_ROW_COL:
                return bingo_board


def calculate_final_score(winning_board, winning_guess) -> int:
    final_sum = sum([item if item != -1 else 0 for row in winning_board for item in row])
    return final_sum * winning_guess


# PART 1
# for guess in guess_numbers:
#     mark_bingo_boards(guess)
#     result = check_for_bingo()
#     if result:
#         print(calculate_final_score(result, guess))
#         break

# PART 2
for guess in guess_numbers:
    mark_bingo_boards(guess)
    results = check_for_many_bingo()
    for result in results:
        print(calculate_final_score(result, guess))     # last print result is the answer
        bingo_boards.remove(result)
