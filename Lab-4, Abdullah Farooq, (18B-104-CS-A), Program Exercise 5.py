print('Program Exercise 5')

print('Enter a range and I will return a table. ')
ini_range = eval(input('Initial range: '))
fin_range = eval(input('Final range: '))
for x in range(ini_range, fin_range+1):
    for y in range(ini_range, fin_range+1):
        print(x*y, end="\t")
    print("\n")
