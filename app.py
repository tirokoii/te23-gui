from tkinter import *
from random import randint

# How many dices
# History
# Dice kind t4, t6, t8, t10, t12, t16

#TypeError: "Menu" object not callable - look into

root = Tk() #Variabel
root.title("Roll the dice")
text_box = Label(root, text="You can roll a dice here") #Write text out
text_box.pack() #Unpacks the text?
text_box_number = Label(root, text="0")
text_box_number.pack()
number = 6

def show():
    roll = randint(1, number) #In terminal
    text_box_number.config(text=roll) #Updated the value in the window

show_button = Button(root, text="Roll the dice", command=show)
show_button.pack()

def dice():
    if dice_menu(label="D4"):
        number = 4
    elif dice_menu(label="D6"):
        number = 6
    return number

menubar = Menu(root)
dice_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Dice", menu = dice_menu)
dice_menu.add_command(label = "D4", command=dice)
dice_menu.add_command(label = "D6", command=dice)
dice_menu.add_command(label = "D8", command=dice)
dice_menu.add_command(label = "D10", command=dice)
dice_menu.add_command(label = "D12", command=dice)
dice_menu.add_command(label = "D20", command=dice)
root.config(menu=menubar)

button = Button(root, text="Quit program", width=50, command=root.destroy)
button.pack()

root.mainloop() #Keeps it updated