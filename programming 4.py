#programming exercise 4

#taking Student name Father name roll no and subjects marks as input

name=input("Input your name")
fatherName=input("Input your Father name")
rollno=input("input you Roll no")
math=eval(input("Input your math subject number"))
english=eval(input("Input your english subject number"))
computer=eval(input("Input your computer subject number"))
science=eval(input("Input your science subject number"))
history=eval(input("Input your history subject number"))
Total=500

#printing student name father name and subject marks
print("************************")
print("Student Name:",name )
print("Father Name:",fatherName)
print("Roll number: ",rollno)
print("=================================")
print("subject","\t","marks")
print("mathematics" ,"\t",math)
print("english" ,"\t",english)
print("computer","\t",computer)
print("science","\t",science)
print("history","\t",history)

obtainedTotal=math+english+computer+science+history
persentage=(obtainedTotal/Total)*100

#checking grade through if and elif condition

if(persentage >=90):
    print("A+ Grade")
elif(persentage <90 and persentage >=80):
    print("A Grade")
elif(persentage <80 and persentage >=70):
    print("B Grade")
elif(persentage <70 and persentage >=60):
    print("C Grade")
else:
    print("fail")
             
