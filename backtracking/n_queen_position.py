
N = 4
def n_queen(board, row) ->bool:
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if n_queen(board, row+1):
                return True

            # This is backtracking, it override 1 to 0 again
            board[row][col] = 0
    return False


def is_safe(board, row, col) -> bool:

    return False


if __name__ == "__main__":
    b = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    n_queen(b, 4)