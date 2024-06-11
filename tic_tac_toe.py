arr = [['x', '0', 'x'],
       ['o', 'x', 'o'],
       ['x', 'o', 'o']]


def test(matrix: list[list]) -> None:
    rows_count = len(matrix)
    for rows in matrix:
        column_count = len(rows)
        assert column_count == rows_count, 'its not square'

    for i in range(rows_count):
        col_win = row_win = diag_win1 = diag_win2 = True
        for j in range(rows_count):
            if row_win and matrix[i][j] != matrix[i][0]:
                row_win = False
            if col_win and matrix[j][i] != matrix[0][i]:
                col_win = False

            if diag_win1 and matrix[j][j] != matrix[0][0]:
                diag_win1 = False

            if diag_win2 and matrix[j][rows_count - 1 - j] != matrix[0][rows_count - 1]:
                diag_win2 = False

        if row_win:
            print(f"{i} row {matrix[i][0]} wins")
            return
        if col_win:
            print(f"{j} col {matrix[0][j]} wins")
            return
        if diag_win1:
            print(f"diag1 {matrix[0][0]} wins")
            return
        if diag_win2:
            print(f"diag2 {matrix[0][rows_count - 1]} wins")
            return

    print(f'No wins')


if __name__ == '__main__':
    test(arr)
