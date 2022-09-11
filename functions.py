#function = a block of code which is executed only when it is called.

def hello(first_name, last_name, age):
    print(f'hello {first_name} {last_name}')
    print(f'You are {age} years old')
    print("Have a nice day!")

hello("Artime", "Vázquez", 42)

#return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1,number2):
    return number1 * number2

x = multiply(6, 8)

print(x)

# keyword arguments =   arguments preceded by an identifier when we pass #                                           them to a function
#                                           The order of the arguments doesn't matter, unlike  #                                           positional arguments
#                                           Python knows the names of the arguments that     #                                           a function receives

def hello2(first, middle, last):
    print(f'Hello {first} {middle} {last}')


hello2(last="Vázquez", middle="Axl", first="Artime")


# ------- NESTED FUNCTIONS ----------------------
# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

print(round(abs(float(input(" ")))))
