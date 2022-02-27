#Assignment 4

   #1st program
print("    1st program  ")
def towerofhanoi(n,source,destination,start):
   if n==1:
      print("Move disk 1 from source ",source,"to destination",destination)
      return
   towerofhanoi(n-1,source,start,destination)
   print("Move disk ",n,"from source",source,"to destination",destination)
   towerofhanoi(n-1,start,destination,source)
   #calling function
n=3
towerofhanoi(n,'A','B','C')



#2nd program(1st method)
print("    2nd program   ")
from math import factorial
print(" Printing Pascal triangle using loop method ")
num=int(input("Enter the number of rows : "))
for i in range(num):
  for j in range(num-i+1):
     print(end=" ")
  for j in range(i+1):
     print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")

  print()


#2nd program(2nd method)
print("   2nd program   ")
n=int(input("Enter the number of rows : "))
print("Printing Pascal triangle using recursion")
def pascal(n,orgn=n):
  if n==0:
    return
    
  pascal(n-1,orgn)

  print(' '*(orgn-n),end='')
  first=1                     
#first number is always 1
  for i in range(1,n+1):
     print(first,end='  ')
     first=first*(n-i)//i
  print()
pascal(n)





  #3rd program
print(   "3rd program(a) ")
a=int(input("Enter first value : "))
b=int(input("Enter second value : "))
c,d=divmod(a,b)
print("Quotient is : ",c)
print("Remainder is : ",d)
def x(a,b):
  pass
     
print(callable(x))
#using callable()function

print("   3rd program(b)  ")
k=(a,b,c,d)
if all([v!=0 for v in k]):
    print("All values are non zero")

else:
    print("Atleast one value is zero")

print("   3rd program(c)  ")
listr=[c,d]
for i in range(4,7):
    listr.append(i)
listv2=[]
#adding values>4 from listr to listv2
for i in listr:
    if i>4:
       listv2.append(i)
 # making a new list listv3 having same elments as listv2 but in string form
listv3=list(map(str,listv2))       
v=",".join(listv3)
print(f"Values greater than 4 is {v}")
set2=frozenset(v)
print("(e)Immutable set is : ",set2)
print("Largest value in the set is : ",max(set2))
q=max(set2)
print("(f)Hash value is : ",hash(q))


        

    
  #4th program 
print("    4th program  ")
class Student:
   def __init__(self,name,sid):
      self.name=name
      self.sid=sid
   def __del__(self):
     print("Object destroyed")
  # creating object 
obj1=Student("Sukrit Malhotra",21105024)
print("The name of student is ",obj1.name,"and Sid is ",obj1.sid)
  #printing details
del obj1





  #5th program
print("  5th program  ")
class Employee:
  def __init__(self,name,salary):
     self.name=name
     self.salary=salary
emp1=Employee("Mehak",40000)
print("1st employee is ",emp1.name,"with salary ",emp1.salary) 
#printing details              
emp2=Employee("Ashok",50000)
print("2nd employee is ",emp2.name,"with salary ",emp2.salary)
emp3=Employee("Viren",60000)
print("3rd employee is ",emp3.name,"with salary ",emp3.salary)
emp1.salary=70000
print("Updated salary of ",emp1.name,"is ",emp1.salary)
del emp3                          
#deleting the object
print("The record of employee Viren deleted")





  #6th program
print("  6th program  ")
word=str(input("Enter first word "))
check=str(input("Enter word testing your friendship")) 
#inputing second word       
def count_dic(word):
  count={}
  list1=list(word)
  
  num=len(list1)
  for i in range(num):
     if list1[i] in count:
        count[list1[i]]+=1
     else:
        count[list1[i]]=1
  return count
#test to verify result
if count_dic(word)!=count_dic(check):   
  print("Their friendship is fake")
elif count_dic(word)==count_dic(check):
  print("Their friendship is true")

