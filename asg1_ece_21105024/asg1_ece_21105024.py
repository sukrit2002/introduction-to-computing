#Assignment 1


             #1st program
print("   1st program    ")
numb1=int(input("Enter first number : "))
numb2=int(input("Enter second number : "))
numb3=int(input("Enter third number : "))
avg=(numb1+numb2+numb3)/3
print("avg is : ",avg)



        

             #2nd program
print("   2nd program   ")
rate=0.20
standard=10000
dependent=3000
gross=float(input("Enter gross income : "))
number1=int(input("Enter number of dependents : "))
taxable=gross-standard-((dependent)*(number1))
tax=(taxable)*rate
print("Tax to be paid is : ",tax)






            #3rd program
print("    3rd program   ")
print("Student=[SID,Name,Gender,Department,CGPA] ")
student=[21105024,'Sukrit','M','ECE',9.2]
print("student= ",student)






            #4th program
print("   4th program   ")
print("Marks of five students")
Marks=[32,43,12,54,8]
print("List before sorting : ",Marks)
Marks.sort()
print("Marks after sorting : ",Marks)






           #5th program(a)
print("   5th program(a)  ")
color=['Red','Green','White','Black','Pink','Yellow']
print("List before removing 4th element : ",color)
color.pop(3)
print("List after removing 4th element : ",color)




           #5th program(b)
print("     5th program(b)   ")
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=[];color.insert(3,'Purple')
print("Output is : ",color)