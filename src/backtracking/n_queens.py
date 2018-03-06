import copy

__author__ = 'J.R.'


# the problem of placing n queens on an n×n chessboard such that no two queens attack each other
def n_queens(m):
    if m <= 0:
        return None
    result = list()
    cols = [-1] * m
    calculate(0, cols, result)
    return result


def calculate(row, cols, result):
    if row == len(cols):
        result.append(copy.deepcopy(cols))
    n = len(cols)
    for col in range(n):
        if validate(row, col, cols):
            cols[row] = col
            calculate(row + 1, cols, result)
            cols[row] = -1


def validate(row, col, cols):
    for r in range(row):
        c = cols[r]
        if c == col:
            return False
        cols_dist = abs(col - c)
        rows_dist = abs(row - r)
        if cols_dist == rows_dist:
            return False
    return True


if __name__ == '__main__':
    m = 8
    print(n_queens(m))
