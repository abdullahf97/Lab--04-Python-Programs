print('Program Exercise 7')

mat1 = [[5, 4],
        [7, 2]]
mat2 = [[6, 2],
        [3, 5]]
result= [[0, 0],
           [0, 0]]
for a in range(len(mat1)):
    for b in range(len(mat2)):
        for c in range(len(mat2)):
            result[a][b] += mat1[a][c]*mat2[c][b]
for r in result:
    print(r)
