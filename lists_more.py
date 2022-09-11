# ----------- SORT -------------------------------------------------
# sort() method   = used with lists
# sorted() function = used with iterables

students = ['Juan', 'Pedro', 'Artime', 'Ceci', 'Soni']
students.sort()

for student in students:
    print(student)


students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

# grade = lambda grades : grades[1]
age = lambda ages : ages[2]
# students.sort(key=age)                     # sorts current list
sorted_students = sorted(students,key=age) # sorts and creates a new list
# sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)

print("*" * 100)
# ----------- MAP -------------------------------------------------
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0], data[1] * 0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)


print("*" * 100)
# ----------- FILTER -------------------------------------------------
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [
    ("Ceci", 42),
    ("David", 48),
    ("Mónica", 60),
    ("Adrián", 42),
    ("Vicki", 40),
    ("Vane", 37),
]

young = lambda data : data [1] < 42
younger_friends = list(filter(young, friends))

for fr in younger_friends:
    print(fr)

print("*" * 100)
# ----------- REDUCE -------------------------------------------------
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y, letters)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y,:x * y,factorial)
print(result)

print("*" * 100)
# ----------- COMPREHENSION -------------------------------------------------
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1, 11):       # create a for loop
    squares.append(i ** 2)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i ** 2 for i in range(1, 11)]
print(squares)

students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)