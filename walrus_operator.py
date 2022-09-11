#python #walrus operator

# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)
print(happy := True)

foods = list()
while True:
  food = input("What food do you like?: ")
  if food == "quit":
      break
  foods.append(food)

print(foods)
print("*" * 100)
foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)

print(foods)