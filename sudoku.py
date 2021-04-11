board = [
    [0, 8, 0, 0, 7, 2, 0, 0, 1],
    [0, 5, 0, 0, 3, 1, 6, 4, 9],
    [0, 0, 0, 0, 4, 0, 8, 0, 7],
    [0, 0, 8, 0, 5, 0, 4, 0, 0],
    [0, 4, 0, 0, 0, 0, 2, 0, 8],
    [6, 0, 1, 2, 0, 0, 0, 5, 0],
    [9, 2, 0, 7, 6, 3, 0, 8, 0],
    [0, 7, 0, 0, 1, 0, 0, 6, 2],
    [1, 6, 5, 9, 0, 0, 3, 0, 0]
]

new_board = [[0 for _ in range(9)] for _ in range(9)]


def valid_sudoku(board, num, pos):
    """This function check correctness of the sudoku board"""

    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def find_empty(board):
    """This function iterate through rows and columns of board and find first empty cell.
    Function returns x, y coordinates."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j

    return False


def print_board(board):
    """Function prints traditional board image"""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])

            else:
                if j == 0:
                    print(" " + str(board[i][j]) + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")


def solver(board):
    """Backtracking function solves sudoku board."""
    empty_cell_coordinates = find_empty(board)

    if not empty_cell_coordinates:
        return True
    else:
        row, col = empty_cell_coordinates

    for value in range(1, 10):
        if valid_sudoku(board, value, (row, col)):
            board[row][col] = value

            if solver(board):
                return True

            board[row][col] = 0

    return False


print_board(new_board)
solver(new_board)
print_board(new_board)

