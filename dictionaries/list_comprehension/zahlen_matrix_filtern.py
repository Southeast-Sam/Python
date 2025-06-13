matrix = [
    [1, 4, 5, 6],
    [7, 8, 10, 13],
    [2, 3, 12, 14],
    [9, 11, 16, 18]
]
matrix_gerade_zahlen = [[zahl for zahl in zeile if zahl % 2 == 0] for zeile in matrix]
print("Matrix mit geraden Zahlen:", matrix_gerade_zahlen)