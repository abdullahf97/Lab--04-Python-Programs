print("Abdullah Farooq, 18B-104-CS, Sec 'A'")
print( " Lab 4 - 9 Nov 2018")
print("Question - 10")

n=5;
for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')
