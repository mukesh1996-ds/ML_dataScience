'''
# chapeter 2
"""
Your task is to built a simple calculater by taking the input from the user.
"""
var1 = int(input("Enter the number:-"))
var2 = int(input('Enter the number:-'))
print('Numbers entered by the user is', var1, var2)

# initializing the operators
# Arithmetic operator:
addition = var1 + var2
print("Addition of the given number is:",addition)
subtraction = var1 - var2
print('Subtraction of the given number is:', subtraction)
multiplication = var1 * var2
print("Multiplication of the given number is:", multiplication)
division = var1 / var2
print('Division of the given number is:', division)

# Comparision  operator:
print(var1 == var2) # check for equal
print(var1> var2)
print(var1< var2)
print(var1>= var2)
print(var1<= var2)
print(var1 != var2)


# chapter 3: Strings and its functions

story = 'this is way of learning python for data science'
"""
Note: The indexing operation in string starts from 0 
"""
print(story[0])
print(story.capitalize()) # this will convert the first letter in capital


# chapter 4: List and tuple
"""
Defintion of list: A list is a container that store any type of value and it can be 
of any data type and the representation is given as [].
List can be accessed by using indexing.
List is MUTABLE. 
"""
from os import read


list1 = ['M','u','k','e','s','h', 25,2j+9]
print("Element in the list are",list1)
print(list1[5])
print(list1[7])

# methods of lists
list2 = [1,8,7,2,21,15]
print("List elements are: ",list2)
list2.append(5) # add the value at the end list 
print("New list is: ",list2)
list2.insert(5,10)
print("New inserted list is:",list2)
list2.sort()
print("Sorted list is ",list2)
list2.pop(5)
print("pop new list is: ",list2)

"""
Tuple: The tuple are IMUTABLE in nature, They are repersented in () and once 
initilized then they are not going to change. 
"""
a = () # empty tuple
b = (1,2,3) # tuple with some value
c = (1,) # tuple with one element will need  comma.

# methods:
tuples = (1,2,3,2,4,2,1,3,2,4,2,4,2,4,2,3,3,3)
print("Return the count of number ",tuples.count(3))
print("Return the position of the number with respect to index",tuples.index(2))

# chepter 5: Dictionary & set
"""
Dictionary is the collection of key and value pair. It is MUTABLE, can be indexed.
there is only one specific rule i.e. there should be only one unique key.
the representation is {key : value}
"""
dict1 = {'a':'Mukesh', 'b' : 'Kumar', 'age' : 25 }
print("The enter dictionary value is: ",dict1)

# methods 
print("This method will represent all the items in the dictionary",dict1.items())
print('This method will only return keys in the dictionary',dict1.keys())
dict1.update({'c' : 'Sharma'})
print("Update the value in the dictionary", dict1)

"""
set: It in unorder, unrepeatable, unindexed again represented by {}
"""
set1 = {1,8,5,3}
print(len(set1))

# Note from chapter 6 to chapter 8 look at the video
# chapter 9: File I/O operations
"""
When you are working with RAM and you preform some of the operation then your task 
is not stored premanently once turn off the system your data is lost. To avoid this 
we will be using file Input and Output.
Modes of opening the file:
1.  'r' = open for reading
2.  'w' = open for writting
3.  'a' = open for append 
4.  '+' = open for updating
5.  'rb' = read in binary mode
6.  'rt' = open to read in text mode
"""

# Opening a file 
# this build in operation will only help to open the file but not read.
readme = open('myfile.txt', 'r')
# this build in operation will help to read the file.
text = readme.read()
print('The entered text is:', text)
# once you have opened the file you also need to close it.
readme.close()

# to create a new file
f = open('text.txt', 'w')
f.write('this is the place where you can learning coding')
f.close()
# to read this 
file = open('text.txt', 'r')
text = file.read()
print('the entered text is ' , text)
file.close()
# the best way to open and read a file is with open
with open('text.txt') as f:
    print(f.read())

# condition statements: If,else and elif in python
# write a program to print which day ?

user = int(input('Enter the number of your choice:'))
if (user == 0):
    print('The number entered by the user is', user)
    print('the day is SUNDAY')
elif ( user == 1):
    print('The number entered by the user is', user)
    print('the day is MONDAY')
elif (user ==2):
    print('The number entered by the user is', user)
    print('the day is TUESDAY')
elif (user == 3):
    print('The number entered by the user is', user)
    print('the day is WEDNESDAY')
elif (user == 4):
    print('The number entered by the user is', user)
    print('the day is THURSDAY')
elif (user == 5):
    print('The number entered by the user is', user)
    print('the day is FRIDAY')
elif (user == 6):
    print('The number entered by the user is', user)
    print('the day is SATURDAY')
else:
    print('Please check the number and then enter it')


# write a program to find the greatest of 4 numbers.

user1 = int(input('enter the first number:-'))
user2 = int(input('enter the second number:-'))
user3 = int(input('enter the third number:-'))
user4 = int(input('enter the fourth number:-'))

if (user1 == user2):
    print('They are equal')
elif (user1 >= user3):
    print('user1 is greater than user3')
elif (user1 <= user4):
    print('user1 is lesser than user4')
else:
    print('they are not equal')

# write a program to find out whether a student is pass or fail if it requires 40% and attleast 33%
# to pass Assume there are three subjects and take the marks from the user.
sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam") 


# write a program to find whether the given username cointain lessthan 10 character.

statement = input('Enter the statement....:-')
print('The statement entered by the user is....:-', statement4)
if (len(statement)< 10):
    print('Yes the entered statement have less than 10 characters', statement)
else:
    print('No, the given statement have more characters.')

# loops 
# write a program to print 1 to 50 using the loop
# while loop
from os import name


i = 0
while(i<=5):
    print('i' + str(i))
    i = i +1
print('value printed ')

# write a program to print the value in the list.
i = 0
lst = ['mukesh', 'kumar', 'sharma', 'sanghi']
print('the type is ...:', type(lst))   
while(i<len(lst)):
    print(lst[i])
    i = i + 1
print('value is printed')

# for loop
for item in lst:
    print('list is ', item)

for i in range(10):
    print(i * 2)

# for loop using else
for i in range(10):
    print('The value of i is....:-',i)
else:
    print('The loop is executed successful')

# break statement: used to break the loop
for i in range(20):
    print('the value of i is...:', i)
    if (i == 4):
        break
print('The loop is successful breaked')
# continue
for i in range(20):
    print('the value of i is...:', i)
    if (i == 4):
        continue
print('The loop is successful breaked')

# pratice test:
# 1. write a program to print the multiplication table:
num = int(input('enter the value...:- '))
for i in range(1,11):
    #print(str(num) + 'X' + str(i) + '=' + str(i * num))
    print(f'{num} X {i} = {num * i}')

# 2. write a program to greet the names in list 
list1 = ['mukesh', 'sohan', 'sachine', 'rahul']

for i in list1:
    if name.startswith('s'):
        print('hello' + name)


# program to find prime number 
number1 = int(input('enter the number'))
print('The entered number is.....:-- ', number1)
prime = True
for i in range(1,number1):
    if number1%i == 0:
        prime = False
        break
if prime:
    print('The given number is prime')
else:
    print('the given number is not prime')

# sum of n natural number 
a = 0
while(a<100):
    print('the sum is...:- ', a)
    a = a+1

# factorial of a given number 
# what is n! i.e. n! = 1 X 2 X 3 X 4.....X n

num = int(input('enter the given number'))
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(f"The factorial of the given {num} is {factorial}")

# write a program to print the star pattern 
n = 5 
for i in range(4):
    print('*' * (i+1))
n =3
for i in range(3):
    print(' '* (n-i-1), end="")
    print('*'* (2*i+1), end="")
    print('  '* (n-i-1))


#  functions 
# manual
marks = [45,78, 56, 44]
precentage = (sum(marks)/400) * 100
print(precentage)

def precentage(a,b,c,d,e):
    cal = (a+b+c+d+e)/500 * 100
    return cal

val = precentage(50,55,80,40,33)
print(val)

# factorial 
# n! = n * (n-1)

def factorial(a):
    product = 1 
    for i in range(a):
        product = product * (i+1)
    return product

f = factorial(5)
print(f)

# pratice function 
# manual approach
marks1 = int(input('enter the marks of subject 1:- \n '))
marks2 = int(input('enter the marks of subject 2:- \n '))
marks3 = int(input('enter the marks of subject 3:- \n '))
marks4 = int(input('enter the marks of subject 4:- \n '))
marks5 = int(input('enter the marks of subject 5:- \n '))

precentage = ((marks1 + marks2 + marks3 + marks4 + marks5)/500) * 100
print("The precentage of obtained marks is :  \n", precentage)

if precentage > 33:
    print('Congrats you have cleared the exam')
else:
    print('Better luck next time')


# automatic function 

def calculate_precentage(a,b,c,d,e):
    precentage = ((a+b+c+d+e)/500)* 100
    return precentage

print(calculate_precentage(50,40,55,33,75))
def user (a):
    print('good day'+ a)

print(user('Mukesh'))

# write a program to find the factorial of a given number
# n! = 1 * 2 * 3 * 4 * ....* n-1 * n
# n! = (n-1)! * n
# 5! = 5*4*3*2*1 = 120

def factorial(a):
    product = 1
    for i in range(a):
        product = product * (i + 1)
    return product

print('The factorial of a given number is:', factorial(5))

# object oriented programming : It is mainly used for the purpose code reusability.
# oops
# what is procedural oriented programming ?
a = 1
b = 2 
print(f'The sun of {a} and {b} is', a+b)
"""
This above process is called procedural oriented programming.
Same thing with oops
"""
class number:
    def sum(self):
        return self.a + self.b

num = number()
num.a = 12
num.b = 13
s = num.sum()
print('The sum of given number is \n',s)

# ENCAPSULATION AND ABSTRACTION
# train form 
class TrainForm: # make a class
    formType = 'Application form'
    def train_details(self): # define a function 
        print(f'customer name is {self.name}') # print name
        print(f'train name is {self.train_name}') # print train name

application = TrainForm() # creating a object 
application.name = 'Mukesh' # entering the details
application.train_name = 'sec-danapur' # entering a details
application.train_details() # printing the details


class Employee:
    company = 'Google'
    def getsalary(self):
        print('Salary is 100K')
    def getincerment(self):
        print('you got the increment')
emp1 = Employee()
emp1.getsalary()
emp1.getincerment()

# static methods
class Employee:
    company = 'Google'

    def getsalary(self, signature):
        print(f'Salary of the employee working in {self.company} is {self.salary} \n {signature} ')

    def getincerment(self):
        print('you got the increment')
    
    @staticmethod 
    def greet():
        print('Good morning')    
    @staticmethod
    def time():
        print('the time is 09:00AM')
emp1 = Employee()
emp1.salary = 400000
emp1.getsalary('Thanks!')
emp1.getincerment()
emp1.greet()
emp1.time()

# __init__ (constructor)
class Employee:
    company = 'Sanghi Cyment'

    def __init__(self, name, salary, subunit): # constructor   
        self.name = name
        self.salry = salary
        self.subunit = subunit
        print('Employee is created')
    
    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the name of the employee is {self.salry}")
        print(f"the name of the employee is {self.subunit}")
        
    def getsalary(self, signature):
        print(f'Salary of the employee working in {self.company} is {self.salary} \n {signature} ')

    def getincerment(self):
        print('you got the increment')
    
    @staticmethod 
    def greet():
        print('Good morning')    

    @staticmethod
    def time():
        print('the time is 09:00AM')

emp1 = Employee('mukesh', 1000, 'YouTube')
emp1.getDetails()

# pratice test

class Information:
    company = 'Infosys'
    def __init__(self, name, organization, experience, salary):
        self.name = name
        self.organization = organization
        self.expreience = experience
        self.salary = salary
    
    def empInfo(self):
        print(f'The name of the employee is {self.name}')
        print(f'The name of the organization is {self.organization}')
        print(f'The employee having the experience of {self.expreience}')
        print(f'The salary of the employee is {self.salary}')

emp1 = Information('Mukesh', 'Infosys', 2, '2000K')
emp1.empInfo()

# write a class calculater to calculate the square, square root, cube root.  
class calculator:
    def __init__(self, num):
        self.num = num
    def square(self):
        print(f'The square of the number is {self.num **2}')

    def squareroot(self):
        print(f'The squareroot of the number is {self.num **0.5}')

    def cuberoot(self):
        print(f'The cube root of the number is {self.num **3}')

a = calculator(93)
a.square()
a.squareroot()
a.cuberoot()
'''

# inheritance
# single inheritance
class Employee:
    company = 'Google'

    def showDetails(self):
        print('This is an employee')

class Programmer(Employee):
    language = 'Python'
    comapany = 'YouTube'

    def getLanguage(self):
        print(f'the language is {self.language}')
    
    def showDetails(self):
        print('This is an programmer')


e = Employee()
p = Programmer()
e.showDetails()
p.showDetails()
print(p.company)