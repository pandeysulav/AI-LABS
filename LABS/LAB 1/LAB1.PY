# '''
# QUESTION NO. 1
# '''
# print("024BSCIT043-SULAV PANDEY")
# a = 10
# b = 5

# add = a + b
# multiply = a*b
# division = a/b
# quotient = a//b
# modulus = a%b

# print(add)
# print(multiply)
# print(division)
# print(quotient)
# print(modulus)

# '''
# QUESTION NO. 2
# '''
# print("024BSCIT043-SULAV PANDEY")
# a = int(input("Enter a number:"))
# if a % 2 == 0:
#     print(f"{a} is even")
# else:
#     print(f"{a} is odd")


# '''
# QUESTION NO. 3
# '''
# print("024BSCIT043-SULAV PANDEY")
# a = int(input("Enter a number:\n"))
# if a == 0:
#     print(f"{a} is zero.")
# elif a > 0:
#     print(f"{a} is positive.")
# else :
#     print(f"{a} is negative.")


# '''
# QUESTION NO. 4
# '''
# print("024BSCIT043-SULAV PANDEY")
# a = int(input("Enter your marks:\n"))
# if a >= 80:
#     print("You achieved distinction.\n")
# elif a>=65:
#     print("You achieved first division.\n")
# elif a>=55:
#     print("You achieved second division.\n")
# elif a>=40:
#     print("You achieved third division. \n")
# else:
#     print("Sorry, you have failed.\n")



# '''
# QUESTION NO. 5
# '''
# print("024BSCIT043-SULAV PANDEY")
# n = int(input("Enter your number:\n"))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
 
# print(f"The factorial of the given number is: {fact}")

# '''
# QUESTION NO. 6
# '''
# print("024BSCIT043-SULAV PANDEY")

# print("Prime numbers between 1 and 100:")

# for n in range(2, 101):
#     prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         print(n, end=" ")


# '''
# QUESTION NO. 7
# '''
# print("024BSCIT043-SULAV PANDEY")
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# count = len(words)
# print(f"Total number of words: {count}")

# '''
# QUESTION NO. 8
# '''
# print("024BSCIT043-SULAV PANDEY")

# string = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for char in string.lower():
#     if char.isalpha():
#         if char in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print(f"Vowels: {vowels}")
# print(f"Consonants: {consonants}")

# '''
# QUESTION NO. 9
# '''
# print("024BSCIT043-SULAV PANDEY")
# studentdict = {
#     "Name" : "Sulav Pandey",
#     "Age" : "19",
#     "Faculty" : "Computer Science", 
#     "Semester" : 4
# }

# print("\n Student Information ")
# for key,value in studentdict.items():
#     print(f"{key}:{value}")
# '''
# QUESTION NO. 10
# '''
# import statistics

# print("024BSCIT043-SULAV PANDEY")

# students = {
#     "Sulav"  : 85,
#     "Aarav"  : 92,
#     "Sita"   : 78,
#     "Ram"    : 95,
#     "Priya"  : 88
# }

# print("\nStudent Marks")
# for name, marks in students.items():
#     print(f"{name}: {marks}")

# highest_marks = max(students.values())
# lowest_marks  = min(students.values())
# average       = float(statistics.mean(students.values()))

# for name, mark in students.items():
#     if mark == highest_marks:
#         highest = name
#     if mark == lowest_marks:
#         lowest = name

# print(f"\nHighest Scorer : {highest} ({highest_marks})")
# print(f"Lowest Scorer  : {lowest} ({lowest_marks})")
# print(f"Average Marks  : {average:.2f}")

# '''
# QUESTION NO. 11
# '''
# print("024BSCIT043-SULAV PANDEY")
# print("Lambda function for squaring a number...")
# x = lambda x: x*x
# print(f"The square of number 2 is: {x(2)}\n")

# print("Lambda function for comparing the greatest among two numbers...")
# larger = lambda x,y : x if x > y else y
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print(f"The larger between two numbers is: {larger(a,b)}")
# '''
# QUESTION NO. 12
# '''
# print("024BSCIT043-SULAV PANDEY")

# numbers = [1, 2, 3, 4, 5]

# squares = list(map(lambda x: x**2, numbers))

# print(f"Original list : {numbers}")
# print(f"Squared list  : {squares}")

# '''
# QUESTION NO. 13
# '''
# print("024BSCIT043-SULAV PANDEY")
# n = [5, 12, 17, 18, 24, 32]

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# even_numbers = list(filter(even, n))

# print(f"Original list    : {n}")
# print(f"Even numbers     : {even_numbers}")

# '''
# QUESTION NO. 14
# '''
# # print("024BSCIT043-SULAV PANDEY")
# print("024BSCIT043-SULAV PANDEY")

# sentence = input("Enter a sentence: ")

# words = sentence.lower().split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print("\nWord Occurrences:")
# for word, count in word_count.items():
#     print(f"{word}: {count}")
# '''
# QUESTION NO. 15
# '''
# print("024BSCIT043-SULAV PANDEY")
# ages = [18, 20, 19, 21, 22, 18, 20, 23, 21, 19]

# mean_age    = sum(ages) / len(ages)
# maximum_age = max(ages)
# minimum_age = min(ages)

# above_mean = 0
# for age in ages:
#     if age > mean_age:
#         above_mean += 1

# print(f"Ages           : {ages}")
# print(f"Mean Age       : {mean_age}")
# print(f"Maximum Age    : {maximum_age}")
# print(f"Minimum Age    : {minimum_age}")
# print(f"Above Mean Age : {above_mean} students")