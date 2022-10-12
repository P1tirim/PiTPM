from ast import operator
from tkinter import *

win = Tk() 
win.geometry("312x324")  
win.resizable(0, 0)  
win.title("Calculator")

firstChislo = ""
operand = ""
secondChislo = ""
isFirst = True

def btn_click(item):
    global output
    global isFirst
    output = output + str(item)
    if isFirst:
        global firstChislo
        firstChislo += str(item)
    else: 
        global secondChislo
        secondChislo += str(item)
    input_text.set(output)

def action(item):
    global output
    global operand
    global isFirst
    output = ""
    operand = item
    isFirst = False
    input_text.set(output)

def bt_clear(): 
    global output 
    global firstChislo
    global secondChislo
    global operand
    global isFirst
    output = ""
    firstChislo = ""
    secondChislo = ""
    operand = "" 
    isFirst = True
    input_text.set("")

def bt_backspace():
    global output 
    global firstChislo
    global secondChislo
    global operand
    global isFirst
    if isFirst and firstChislo != "":
        firstChislo = firstChislo[:-1]
        output = firstChislo
    elif isFirst == False and secondChislo != "":
        secondChislo = secondChislo[:-1]
        output = secondChislo
    input_text.set(output)
    


def bt_equal():
    global output
    global firstChislo
    global operand
    global secondChislo
    global isFirst
    try:
        result = str(eval(str(firstChislo) + operand + str(secondChislo)))
        input_text.set(result)
        firstChislo = result
    except:
        if operand == "/" and secondChislo == "0":
            input_text.set("Ошибка! деление на 0")
        firstChislo = ""
        isFirst = True
    
    print(firstChislo)
    print(secondChislo)
    print(operand) 
    
    output = ""  
    secondChislo = ""
 
output = ""
 
 
input_text = StringVar()
 
 
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
 
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) 

btns_frame = Frame(win, width=312, height=272.5, bg="grey")
 
btns_frame.pack()
 
 
clear = Button(btns_frame, text = "C", fg = "black", width = 22, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
 
backspace = Button(btns_frame, text = "⌫", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_backspace()).grid(row = 0, column = 2, padx = 1, pady = 1)

divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: action("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
 
seven = Button(btns_frame, text = "7", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 2, pady = 1)
 
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: action("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
 
four = Button(btns_frame, text = "4", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: action("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
 
one = Button(btns_frame, text = "1", fg = "black", width = 11, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: action("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
 
zero = Button(btns_frame, text = "0", fg = "black", width = 22, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()
