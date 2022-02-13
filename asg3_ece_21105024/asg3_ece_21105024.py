#Assignment 3


   #1st program
print("    1st program  ")
stn=str(input("Enter the string : "))
length=len(stn)
count=dict()
i=0
stk=stn.split()
if ' ' in stn:
 while i<length:
    count=0
    for j in stk:
        if stk[i]==j:
            count+=1
    print(stk[i],"Present",count,"Times")
    i+=1 
else:
  for expr in stn:
    if expr in count:
       count[expr]+=1
    else:
       count[expr]=1
  print(count)



     #2nd program
print("    2nd program  ")
date=int(input("Enter the date: "))
month=int(input("Enter the month(1-12): "))
year=int(input("Enter the year: "))
if year%400==0:
   leapyear=True
elif year%100==0:
   leapyear=False
elif year%4==0:
   leapyear=True
else:
   leapyear=False
if month in (1,3,5,7,8,10,12):
 day=31
elif month in (4,6,9,11):
 day=30
elif month==2 and leapyear==True:
 day=29 
elif month==2 and leapyear==False:
 day=28
if date<day:
 date+=1
else:
 date=1
if month==12:
    month=1
    year+=1
elif leapyear==True and date==29:
  month=2
else:
  month+=1
if year==2026 and date==1 and month==1:
  print("Invalid output date")
elif year<1800 or year>=2026:
  print("Invalid year input")
else:
  print("The next date of input date is [dd-mm-yyyy] %d-%d-%d." % (date,month,year))





     #3rd program
print("   3rd program  ")

n1=int(input("Enter 1st number : "))
n2=int(input("Enter 2nd number : "))
n3=int(input("Enter 3rd number : "))
a=[(x,x**2) for x in [n1,n2,n3]]
print(a)





      #4th program
print("   4th program  ")
grade=float(input("Enter the grade points: "))
if grade==10:
   print("Your grade is 'A+' and Outstanding Performance.")
elif 9<=grade<10:
   print("Your grade is 'A' and Excellent Performance.")
elif 8<=grade<9:
   print("Your grade is 'B+' and Very Good Performance.")
elif 7<=grade<8:
   print("Your grade is 'B' and Good Performance.")
elif 6<=grade<7:
   print("Your grade is 'C+' and Average Performance.")
elif 5<=grade<6:
   print("Your grade is 'C' and Below Average Performance.")
elif 4<=grade<5:
   print("Your grade is 'D' and Poor Performance.")
else:
   print("Error, grade out of range")



     #5th program
print("   5th program  ")
n=6
for i in range(n):
  for j in range(i):
     print(' ',end='')
  for j in range(2*(n-i)-1):
      print(chr(65+j),end='')
  print()

 
       
      
       #6th program
print("   6th program  ")
data={}
while True:
 k=input("Do you want to enter input values,press Y or N\n")
 c=ord(k)
 if c==89:
  name=str(input("Enter the name of the student\n"))
  sid=int(input("Enter the SID of the student\n"))        
  data[sid]=name
 elif c==78:
  print("Thanks")
  break

print("The record of student input data",data)
print("Sorting using student names",sorted(data.values()))
print("Sorting using SID",sorted(data.items()))
f=int(input("Search\n"))
if f in data:
  print(data[f])



     
      #7th program
print("   7th program  ")
a=0
b=1
count=0
sum=0
fibonacciSeries=[0,1]
num=int(input("Enter the number of terms : "))
if num<=0:
  print("Enter a positive value")
elif num==1:
  print("Fibonacci sequence is : ")
  print(a)
else:
   for i in range(2,num):
       nextElement=fibonacciSeries[i-1]+fibonacciSeries[i-2]
       fibonacciSeries.append(nextElement)
       sum+=fibonacciSeries[i-1]

sum+=fibonacciSeries[i]       
print(fibonacciSeries)
print("Average of resultant fibonacci series is : ",sum/num)


    




      #8th program
print("   8th program  ")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
Set4={1,2,3,4,5,6,7,8,9,10}
Seta=(Set1|Set2)-(Set1&Set2)
print(Seta)
Setb=(Set1|Set2|Set3)-((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print(Setb)
Setc=(Set1|Set2|Set3)-((Setb)|(Set1&Set2&Set3))
print(Setc)
Setd=Set4-Set1
print(Setd)
Sete=((Set4)-(Set1|Set2|Set3))
print(Sete)
