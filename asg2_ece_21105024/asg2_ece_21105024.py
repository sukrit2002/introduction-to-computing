#Assignment-2



           #1st program
print("  1st program (a)  ")
word="Python is a case sensitive language"
length=len(word)
print("Length of given string is : ",length)


print("   1st program (b)  ")
reverse=word[::-1]
print("The given string in reverse order is :",reverse)


print("   1st program (c)  ")
word_new=word[10:26]
print(word_new)


print("    1st program (d)  ")
letter=word[0:10] + "object oriented" + word[26:]
print(letter)


print("     1st program (e)  ")
k=word.find('a')
print("Index of substring a is : ",k)


print("     1st program (f)  ")
print(word.replace(" ",""))






        #2nd program
print("      2nd program  ")
print("Hey,%s Here!\n"
    "My SID is %d\n"
    "I am from %s Department and My CGPA is %f" %('Sukrit',21105024,'ECE',9.9))






         #3rd program
print("      3rd program  ")
a=56
b=10
print("a&b is : ",a&b)
print("a|b is : ",a|b)
print("a^b is : ",a^b)
print("Left shift a with 2 bits gives : ",a<<2)
print("Left shift b with 2 bits gives : ",b<<2)
print("Right shift a with 2 bits gives : ",a>>2)
print("Right shift b with 4 bits gives : ",b>>4)








          #4th program
print("       4th program  ")
a=input("First number is : ")
b=input("Second number is : ")
c=input("Third number is : ")
if a>=b and a>=c:
  print("Greatest number is : ",a)
elif b>=a and b>=c:
  print("Greatest number is : ",b)
elif c>=a and c>=b:
  print("Greatest number is : ",c)







           #5th program
print("        5th program  ")
check=str(input("Enter the string : "))
if 'name' in check:
   print("Yes")
else:
   print("No")






 
            #6th program
print("         6th program  ")
a=int(input("First side is : "))
b=int(input("Second side is : "))
c=int(input("Third side is : "))
if a>b+c or b>a+c or c>b+a:
  print("No")
else:
  print("Yes")




