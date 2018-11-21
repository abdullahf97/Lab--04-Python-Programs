print('Program Exercise 6')

x=[[4,2,5],
   [3,16,6],
   [1,5,9]]

y= [[6,18,15],
    [7,4,14],
    [9,15,11]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for a in range(len(x)):
    for b in range(len(x[0])):
        result[a][b] = x[a][b] + y[a][b]
for r in result:
    print(r)
