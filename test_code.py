def solve_sudoku():
    row, col = find_empty_cell(board)

    if row is None:
        return True

    for num in range(1, 10):
        if is_valid_move(board, row, col, str(num)):
            board[row][col] = str(num)

            if solve_sudoku():
                return True

            board[row][col] = ""

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == "":
                return (row, col)
    return None, None

def is_valid_move(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False

    return True


board = [
    ['', '9', '', '2', '5', '', '6', '8', ''],
    ['', '', '5', '9', '1', '', '', '2', ''],
    ['', '4', '3', '', '8', '7', '9', '', '5'],
    ['4', '', '7', '1', '', '2', '5', '', '8'],
    ['', '8', '', '', '7', '', '', '3', '2'],
    ['9', '', '', '', '', '', '', '', '4'],
    ['3', '', '4', '8', '', '', '', '', ''],
    ['1', '5', '', '', '2', '', '3', '', ''],
    ['6', '', '', '', '', '5', '8', '', '1']
    ]

solve_sudoku()
for i in board:
    print(i)