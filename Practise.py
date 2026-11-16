""" Print the below statement
This below code is print a statement"""

print("This is my first line of code")


# Creating variables

name = "Sandy"
age = 32

print(name)
print(age)


# Adding two numbers using variables

num1 = 10
num2 = 5

sum = num1 + num2

print("Sum:", sum)

# example 2

num1 = 20
num2 = 30

total = num1 + num2
print("Total:", total)


# Arithmetic operators

a = 10
b = 3

#Addition
print("Addition:", a + b)

#Subtraction
print("Subtraction", a - b)

#Multiplication
print("Multiplication:", a * b)

#Division
print("Division:", a / b)

#Floor Division
print("Floor Division:", a // b)

#Modulus
print("Modulo:", a % b)

#Exponential
print("Exponential:",a ** b)

#Comparison Operators

a1 = 10
b1 = 5

#Equal to
print("EqualsTo:", a == b)

#Not Equal to
print("NotEqualsTo:", a != b)

#Greater tha
print("GreaterThan:", a > b)

#Less Than
print("LessThan:", a < b)

#Greater than or equal to
print("GreaterThanOrEqualTo:", a >= b)

#Less than or equal to
print("LessThanOrEqualTo:", a <= b )

#Logical Operator

a2 = 10
b2 = 5

# AND operator
print("AND:", a2 > 5 and b2 < 10  )

# OR operator
print("OR:", a2 > 5 or b2 > 10 )

# NOT operator
print("NOT:", not (a2 > 5))


#looping through a list

fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(fruits)

#looping through a string
name = "Sandy"
for nam in name:
    print(nam)


while a <=5:
    print(a)
    a += 1

#checking for even and odd
numbers = [1,2,3,4,5]
for number in numbers:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


#Grade Checker
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# Grade check with error validation.

marks = int(input("Enter your marks: "))

if 0 <= marks <= 100:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
else :
    print("Invalid marks! Please enter marks between 0 and 100.")

#Sum of even numbers
total = 0

for i in range(1, 6):
    total += i

print("Sum of numbers from 1 to 5:", total)



# Topic: Positive, Negative, Odd or Even

number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")

elif number < 0:
    if number % 2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")

else:
    print("0 is even, 0 is zero")



# Topic: Grade Checker Using if-elif-else

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")



# Topic: Grade Checker With Error Validation

marks = int(input("Enter your marks: "))

if 0 <= marks <= 100:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")



# Topic: Sum of Even Numbers Using for Loop

total = 0

for i in range(1, 6):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)



# Topic: Guessing Game With Limited Attempts

secret_number = 7
attempts = 0

while attempts < 3:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess == secret_number:
        print("Congratulations! You guessed it.")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

else:
    print("Game Over! No attempts left.")



# Topic: Logical Operators Using and

age = int(input("Enter your age: "))

has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")




# Topic: Calculator With Arithmetic and Comparison Operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Modulus:", a % b)
else:
    print("Cannot divide by zero")

if a > b:
    print("First number is greater")
elif a < b:
    print("Second number is greater")
else:
    print("Both numbers are equal")



# Topic: Number Classification - Positive, Negative, Even, Odd, Small, Medium, Large

num = int(input("Enter a number: "))

# Check positive, negative, even or odd
if num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")

elif num < 0:
    if num % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")

else:
    print("The number is zero")

# Classify number by size
if num < 10:
    print("Small Number")
elif num <= 100:
    print("Medium Number")
else:
    print("Large Number")


def course_name(course):
    print("My course is", course)


course_name("Python")

def greet(name):
    print("hello", name)


greet("Rahul")
greet("Anita")



def add(a,b):
    return a+b


add(1, 2)
add(3,4)


def greet(name="Student"):
    print("hello", name)

greet("Student")
greet()

def add(a,b):
    return a+b

result = add(3,4)
print(result)


def power(base, exponent = 2):
    return base ** exponent


print(power(2,3))
print(power(2))




def add_number(*args):
    return sum(args)


print(add_number(2,3))
print(add_number(2,3,4,5,6,7,8,9))



def print_values(*args):
    for value in args:
        print(value)

print_values("apple", "banana", "cherry")