from tkinter import *

window = Tk() # Instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='data/logo2.png')
window.iconphoto(True, icon)
window.config(background = "#5cfcff")

window.mainloop() # Place window on computer screen, listen for event