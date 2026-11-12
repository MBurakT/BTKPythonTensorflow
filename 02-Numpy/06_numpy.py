import numpy as np

# matrix
benim_listem = [[10, 20, 30], [20, 30, 40], [40, 50, 60]]
benim_matrix_dizim = np.array(benim_listem)
print(benim_matrix_dizim)
print(benim_matrix_dizim[0])
print(benim_matrix_dizim[1][2])
print(benim_matrix_dizim[1, 2])
print(benim_matrix_dizim[1:, 2])
print(benim_matrix_dizim[0:, 2])
print(benim_matrix_dizim[2:, 2:])
print(benim_matrix_dizim[2:, 0:])
yeni_liste = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]
]
yeni_matrix = np.array(yeni_liste)
print(yeni_matrix[[4, 2, 0]])
