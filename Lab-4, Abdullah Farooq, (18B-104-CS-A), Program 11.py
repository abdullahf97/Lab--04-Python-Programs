print("Abdullah Farooq, 18B-104-CS, Sec 'A'")
print( " Lab 4 - 9 Nov 2018")
print("Question - 11")

print("This program will count total number of vowels from user defined sentence")
string=input("Enter your string: ")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("Number of vowels are: ")
print(vowels)
