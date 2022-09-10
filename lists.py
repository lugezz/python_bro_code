# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()

for x in food:
    print(x)

print ("*" * 100)
# food.clear() # Delete everything
del_elem = food.pop(2) # Delete item 2
print(del_elem)
food.append(del_elem) # Added again

for x in food:
    print(x)

print ("*" * 100)
# 2D LISTS ------------------------------------------------
drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[2][0])
