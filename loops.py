
# ---- WHILE ---------------------------------------------------------
# while loop =  a statement that will execute it's block of code,
#               as long as it's condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print(f"Hello {name}")

# ---- FOR ---------------------------------------------------------

# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#               while loop = unlimited
#               for loop = limited

import time

for i in range(10):
    print(i + 1)


# ---- NESTED ---------------------------------------------------------
# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

for i in range(50,100+1,2):
    print(i)

for i in "Bro Code":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("Happy New Year!")

# ---- BREAK CONTINUE ---------------------------------------------------------

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)