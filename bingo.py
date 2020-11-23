board1 = [[37, 39, 66, 67, 47], [15, 90, 40, 35, 69], [0, 30, 41, 72, 22]]
board2 = [[88, 59, 54, 22, 6], [17, 30, 75, 19, 43], [53, 78, 44, 70, 0]]
board3 = [[37, 63, 0, 18, 53], [44, 19, 83, 24, 56], [65, 78, 75, 52, 2]]
board4 = [[82, 60, 8, 35, 72], [34, 0, 1, 90, 11], [89, 37, 27, 54, 45]]

board1_check = [[False, False, False, False, False], [False, False, False, False, False],
                [True, False, False, False, False]]
board2_check = [[False, False, False, False, False], [False, False, False, False, False],
                [False, False, False, False, True]]
board3_check = [[False, False, True, False, False], [False, False, False, False, False],
                [False, False, False, False, False]]
board4_check = [[False, False, False, False, False], [False, True, False, False, False],
                [False, False, False, False, False]]

board1_win = False
board2_win = False
board3_win = False
board4_win = False


def check_board(input, board, board_check):
    for idx1, list in enumerate(board):
        for idx2, value in enumerate(list):
            if input == value:
                board_check[idx1][idx2] = True
                return board_check
            else:
                pass
    return board_check


def win_row(board_check, nr_rows=1):
    checked_nr_row = 0
    for list in board_check:
        if all(list):
            checked_nr_row += 1
            if checked_nr_row == nr_rows:
                return True
    return False


def win_col(board_check, nr_cols=1):
    checked_nr_col = 0
    total_rows = len(board_check[0])
    for i in range(5):
        a = [m[i] for m in board_check]
        if all(a):
            checked_nr_col +=1
            if checked_nr_col == nr_cols:
                return True
    return False
def check_winner():
    if board1_win:
        print('board1_win')
    elif board2_win:
        print('board2_win')
    elif board3_win:
        print('board3_win')
    elif board4_win:
        print('board4_win')
    else:
        pass

while True:
    # Input
    Input = int(input('New calling:'))

    # Update checks
    check_board(Input, board1, board1_check)
    check_board(Input, board2, board2_check)
    check_board(Input, board3, board3_check)
    check_board(Input, board4, board4_check)
    # print(board1_check)
    # print(board2_check)
    # Check winnings
    # Row
    nr_rows = 1
    board1_win = win_row(board1_check, nr_rows=nr_rows)
    board2_win = win_row(board2_check, nr_rows=nr_rows)
    board3_win = win_row(board3_check, nr_rows=nr_rows)
    board4_win = win_row(board4_check, nr_rows=nr_rows)
    check_winner()
    # Column
    nr_cols = 1
    board1_win = win_col(board1_check, nr_cols=nr_cols)
    board2_win = win_col(board2_check, nr_cols=nr_cols)
    board3_win = win_col(board3_check, nr_cols=nr_cols)
    board4_win = win_col(board4_check, nr_cols=nr_cols)
    check_winner()
    # print(board1_check)
    # print(board2_check)
    # print(board3_check)
    # print(board4_check)
