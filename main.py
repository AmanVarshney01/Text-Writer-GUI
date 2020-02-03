import turtle
import tkinter as tk
from alphabet import alphabet

root = tk.Tk()
root.title('Text Writer')
ccanvas = tk.Canvas(master = root, width = 1000, height = 500)
ccanvas.grid(row=0, column=0, columnspan=3)
canvas = turtle.TurtleScreen(ccanvas)
canvas.bgcolor("black")
myPen = turtle.RawTurtle(canvas)
myPen.hideturtle()
myPen.speed(0)
myPen.pensize(2)

def displayMessage(message, fontSize, color, x, y):
    myPen.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            myPen.penup()
            for dot in letter:
                myPen.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                myPen.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing


fontSize = 30
characterSpacing = 5
fontColor = "#FF00FF"
name = tk.Entry(root)
name.grid(row=1, column=0)
def Button_click():
    shift = 0
    if len(str(name.get())) < 17:
        shift = int(-230)
    elif len(str(name.get())) <= 12:
        shift = int(-210)
    elif len(str(name.get())) > 17:
        shift = int(-290)

    displayMessage(str(name.get()), fontSize, fontColor, shift, 0)

def Button_click_clear():
    myPen.clear()

submit = tk.Button(root, text='Submit', padx=40, pady=20, command=Button_click).grid(row=1, column=1)
clear = tk.Button(root, text='Clear', padx=40, pady=20, command=Button_click_clear).grid(row=1, column=2)

root.mainloop()
