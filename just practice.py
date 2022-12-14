'''
print("Arithmatic Operation")

num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))


Add = num1 + num2
sub = num1-num2
mul = num1 *num2
div = num1 / num2

print(Add)
print(sub)
print(mul)
print(div)

print("Bye")
'''
'''
# Area of Triagle

b = float(input("Enter breadth:"))
h = float(input("Enter height:"))

Area = 1/2 * b *h

print(Area)
'''

#Swap two variables

'''
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

temp1 = a
a = b
b = temp1

print(a)
print(b)
'''
'''
import random
random_list = random.sample(range(10,40),6)
print(random_list)
'''



#Take 4 input from the user first name, last name, phone number, percentage and display the data


'''
first_name = input("Enter fists name:")
last_name = input("Enter last name:")
ph_no = int(input("Enter phone number:"))
percentage = float(input("Enter percentage:"))

print(first_name)
print(last_name)
print(ph_no)
print(percentage)
'''

#Area of Rectangle

'''
w =int(input("Enter Width:"))
h =int(input("Enter Height:"))
Area = w*h
print("Area of Rectangle:",Area)
'''

#Write a program to convert temperature from celsius to fahrenheit
 
#T(F) = T(C)x(9/5) + 32
'''
Cel = float(input("Enter temperature in celsius:"))

fah = (Cel * 1.8) + 32

print("Temperatue in Fahrenheit:",fah)

fah = float(input("Enter temperature in fahrenheit:"))

Cel = (fah-32)/1.8

print("Temperature in Celsius:", Cel)
'''

 #Calculate percentage and highest marks

'''
s1 = int(input("Enter marks in sub1:"))
s2 = int(input("Enter marks in sub2:"))
s3 = int(input("Enter marks in sub3:"))
s4 = int(input("Enter marks in sub4:"))
s5 = int(input("Enter marks in sub5:"))

perc = (s1+s2+s3+s4+s5)/5

print("percentage of marks:",perc)
print("percentage of marks:%.2f" %(perc))

Highest_marks =(max(s1,s2,s3,s4,s5))
print("Highest marks:",Highest_marks)
print("Highest marks: %i" %(Highest_marks))
'''

#Replace function
'''
str1 = input("Enter the string:")
str2 = str1.replace("a", "$")
print(str2)
'''

'''
str1 = input("Enter the string:")
str2 = str1.replace(" ", "-")
print(str2)
'''

#If -else block
# show pass & fail marks using if else block

'''
marks = int(input("Enter the marks:"))

if marks<35:
    print("fail")
    print("Prepare hard for the next year")
else:
    print("pass")
    print("Enjoy the party")
'''

#if -elif-elif-else
'''
marks = int(input("Enter the marks:"))

if marks<35:
    print("fail")
elif marks<=50:
    print("Grade c")
elif marks <=75:
    print("Grade B")
else:
    print("Grade A")
   '''

#compare the two numbers and print the big number
'''
n1 =float(input("Enter the number:"))
n2 =float(input("Enter the number:"))

if n1>n2:
    print("n1 is bigger than n2")

elif n1<n2:
    print("n2 is bigger than n1")

else:
    print("both are equal")
   '''

#

'''
ph = input("enter the phone number:")

if ph.isdigit() == True:
    print("Input is digit")
else:
    print("Input is not digit")
'''
'''
ph = input("enter the phone number:")

if ph.isdigit() and len(ph)==10:
    print("Input is valid")
else:
    print("Input is not valid")
'''
'''
name = input("enter the name:")

if name.isalpha():
    print("Input is valid") 
else:
    print("Input is not valid")
   '''
#number is even or odd
'''
n1 =int(input("Enter the number"))

if n1%2 ==0:
    print("Even number")
else:
    print("odd number")
'''
#check for vowel or consonant
'''
ch = input("Enter the character:")

if ch in "aeiouAEIOU":
    print("vowel")
else:
    print("consonant")
'''
#check for vowel or consonant
#using nested if block
'''
ch = input("Enter the character:")

if ch.isalpha() and len(ch) == 1:
    if ch in "aeiouAEIOU":
        print("vowel")
    else:
       print("consonant")

else:
    print("invalid")
'''

#BMI = weight(kg)/(height(m)*height(m))
'''
w = float(input("Enter the weight:"))
h = float(input("Enter the height:"))

BMI = w/(h*h)

if BMI >= 27.5:
    print("High Risk")

elif BMI>=23 & BMI<=27.4:
        print("Moderate Risk")
elif BMI>=18.5 & BMI<=22.9:
        print("Low Risk")
elif BMI<= 18.5:
        print("Risk of nutritional deficiency disease")
else:
    print("Invalid Response")
'''

#Seperate even and odd numbers

'''
list1 = [1,2,3,4,5,6,7,8,9]
even = []
odd = []

for i in list1:
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''
'''
list1 = [1,2,3,4,5,6,7,8,9]
for i in list1:
    list1.append(i)
print(i)
'''
'''
list1 = []
for i in range(1000,1500):
    if i%7 == 0:
        list1.append(i)
print(list1)
'''

'''
num = int(input("Enter the number:"))
for i in range(1,11):
    print(num,"X",i, "=",num*i)
'''

#for loop with the string data type

'''
str1 = input("Enter a string:")
vowel = [] 
consonant = []

for i in str1:
    if i in "aeiouAEIOU":
        vowel.append(i)
    else:
        consonant.append(i)
print(vowel,"Total no of vowels:", len(vowel))
print(consonant,"Total no of consonants:",len(consonant))
'''
'''
str1 = input("Enter a string:")
alpha = []
digit = []
others = []

for i in str1:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        digit.append(i)
    else:
        others.append(i)
print(alpha,"Total characters:",len(alpha))
print(digit,"Total characters:",len(digit))
print(others,"Total characters:",len(others))
'''
#while loop
'''
n = 1
while n<=10:
    print(n)
    n = n+1
print("bye")
'''

#small calc program

'''
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Exit")

    ch = int(input("Enter your choice:"))

    if ch ==1:
        num1 =int(input("Enter the num1:"))
        num2 =int(input("Enter the num2:"))
        print("Addition", num1 +num2)
        print("_"*30)
    elif ch ==2:
        num1 =int(input("Enter the num1:"))
        num2 =int(input("Enter the num2:"))
        print("Subtraction", num1-num2)
        print("_"*30)
    elif ch ==3:
        num1 =int(input("Enter the num1:"))
        num2 =int(input("Enter the num2:"))
        print("Multiplication", num1 * num2)
        print("_"*30)
    elif ch ==4:
        break
'''

#Dictionary Examples
'''

squares = {}
for i in range(1,11):
    squares[i] = i*i
print(squares)

'''
'''
even = {}
odd = {}

for i in range(1,20):
    even[i] = i*i
    odd[i] = i*i*i
print(even)
print(odd)
'''

'''
even = {}
odd = {}

for i in range(1,20):
    if i%2 ==0:
        even[i] = i*i
    else:
        odd[i] = i*i*i
    
print(even)
print(odd)
'''
'''
student = {}
while True:
    print("1.Add new student")
    print("2.Check your result")
    print("Exit")

    ch = int(input("Enter your choice:"))

    if ch ==1:
        print("Add a new student details:")

        name = input("Enter name:")

        s1 = int(input("Enter marks in sub1:"))
        s2 = int(input("Enter marks in sub2:"))
        s3 = int(input("Enter marks in sub3:"))

        student[name] = [s1,s2,s3]

        print(student)

    elif ch ==2:

        n =input("Enter your name to check your result:")

        if n in student:
            print("Data found")
            print(student[n])
            perc = sum(student[name]/3)
            print("percentage:%.2f"%(perc))
            print("_________________")
        else:
            print("Data not found")
    elif ch == 3:
        print("___Bye___")
        break
        
'''



# practice examples

# python program to check prime numbers

'''
num = int(input("Enter a number:"))

if num >1:
    for i in range(2,num):
        if (num % i) ==0:
            print(num,"is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num,"is a prime number")
    
else:
    print(num,"is a prime number")
   '''

wish ='hello'
response ='hai'

print(wish)
print(response)

            
        
        
        


































    
        












































                 































