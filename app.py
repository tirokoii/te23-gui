from tkinter import *
from tkinter import Menu
from random import randint

# How many dices
# History
# Dice kind t4, t6, t8, t10, t12, t16 - doesn't work

number = 6

class Dice:
    def __init__(self, roll, p):
        self.roll = roll
        self.print = p

D4 = Dice(4, "d4")
D6 = Dice(6, "d6")
D8 = Dice(8, "d8")
D10 = Dice(10, "d10")
D12 = Dice(12, "d12")
D20 = Dice(20, "d20")

dices = [D4, D6, D8, D10, D12, D20] 

root = Tk() #Variabel
root.title("Roll the dice")
text_box = Label(root, text="You can roll a dice here") #Write text out
text_box.pack() #Unpacks the text?
text_box_number = Label(root, text="0")
text_box_number.pack()


def diceChoice(newdice):
    for dice in dices:
        if newdice == dice.print:
            global number
            number = dice.roll
            return number

menubar = Menu(root) #Creates the Menubar
dice_menu = Menu(menubar, tearoff=0) #Adds the dice menu
menubar.add_cascade(label = "Dice", menu = dice_menu)
dice_menu.add_command(label = D4.print, command=lambda: diceChoice(D4.print))
dice_menu.add_command(label = D6.print, command=lambda: diceChoice(D6.print))
dice_menu.add_command(label = D8.print, command=lambda: diceChoice(D8.print))
dice_menu.add_command(label = D10.print, command=lambda: diceChoice(D10.print))
dice_menu.add_command(label = D12.print, command=lambda: diceChoice(D12.print))
dice_menu.add_command(label = D20.print, command=lambda: diceChoice(D20.print))
root.config(menu=menubar)

def show():
    roll = randint(1, number) #In terminal
    text_box_number.config(text=roll) #Updated the value in the window

show_button = Button(root, text="Roll the dice", command=show)
show_button.pack()

button = Button(root, text="Quit program", width=45, command=root.destroy)
button.pack()

text_box.configure(background="black", fg="white")
text_box_number.configure(background="black", fg="white")
button.configure(background="darkred", fg="white")
root.configure(background="black")
root.mainloop() #Keeps it updated'''