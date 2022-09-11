# ---- FUNCTION TO VARIABLES -----------------------------

def hello():
    print("Hello")


hi = hello
hi()

say = print
say("Whoa! I can't believe this works! :O")
print("*" * 100)

# ---- HIGHER ORDER -----------------------------
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument ----- 
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)

# ------------ 2. returns a function ------------- 
def divisor(x):
   def dividend(y):
       return y / x
   return dividend


divide = divisor(2)
print(divide(10))

print("*" * 100)
# ---- LAMBDA -----------------------------
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
print(double(1))

multiply = lambda x, y: x * y
print(multiply(1,2))

add = lambda x, y, z: x + y + z
print(add(1, 2, 3))

full_name = lambda first_name, last_name: f'{last_name}, {first_name}'
print(full_name("Artime","Vázquez"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18), age_check(17)) 

print("*" * 100)
