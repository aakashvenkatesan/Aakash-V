x = [[12, 7, 2],
     [4, 5, 6],
     [1, 2, 3]]
y = [[1, 3, 5],
     [2, 4, 6],
     [8, 9, 10]]
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]

for r in result:
    print(r)