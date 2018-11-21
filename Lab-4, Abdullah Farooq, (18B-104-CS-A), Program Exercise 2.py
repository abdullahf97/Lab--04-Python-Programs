print('Program Exercise 2')

a1 = eval(input('Enter the first term of the sequence: '))
d = eval(input('Enter the common difference of the sequence: '))
n = eval(input('Enter the nth term of the sequence: '))
an = a1 + (n-1)*d
print(an)
prompt = input('Do you want to continue?: ') 
for yes in prompt:
    if prompt == "yes":
        n2=eval(input('Enter the next nth term: '))
        an2= a1+(n2-1)*d
        print(an2)
        prompt = input('Do you want to continue?: ')
else:
    print("End")
