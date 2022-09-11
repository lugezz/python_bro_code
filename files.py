import os
import shutil


path = "data/"
# path = "data/little_prince.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")

# -- WRITE AND APPEND -----------------------------------------------------------------
text = "Yooooooooo\nThis is some text\nHave a good one!\n"

with open('data/test.txt','w') as file:
    file.write(text)

with open('data/test.txt','a') as file:
    file.write('Text append')

# ---- MOVE  ---------------------------------------------------------------------
source = "data/test.txt"
destination = "data/destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

except Exception as err:
    print(err)
    print('Something went wrong')

# ---- DELETE  -------------------------------------------------------------------
path = 'data/TBDel.txt'

with open(path,'w') as file:
    file.write("To be deleted")

try:
    os.remove(path)    # delete a file
    # os.rmdir(path)     # delete an empty directory
    # shutil.rmtree(path)# delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")