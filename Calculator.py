from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title("Calculator")
root.iconbitmap('cal_logo.ico')
string = ''
image1 = ImageTk.PhotoImage(Image.open("sirjan.png"))
frame=LabelFrame(root, text="I am here",padx=5,pady=5).grid(row=0,column=0)


def button_click(number):
    global string
    current = e.get()
    string += str(number)
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    global num1
    global symbol
    global string
    string = str(eval(string))
    num1 = e.get()
    e.delete(0, END)
    symbol = "+"
    string += symbol


def button_subtract():
    global num1
    global symbol
    global string
    string = str(eval(string))
    num1 = e.get()
    e.delete(0, END)
    symbol = "-"
    string += symbol


def button_multiply():
    global num1
    global symbol
    global string
    string = str(eval(string))
    num1 = e.get()
    e.delete(0, END)
    symbol = "*"
    string += symbol


def button_divide():
    global num1
    global symbol
    global string
    string = str(eval(string))
    num1 = e.get()
    e.delete(0, END)
    symbol = "/"
    string += symbol


def button_equal():
    global string
    global num2
    num2=e.get()
    e.delete(0, END)
    e.insert(0, eval(string))
    string = str(eval(string))


def button_root():
    global string
    string = str(eval(string))
    string = str(eval(str(int(string) ** 0.5)))


def button_clear():
    global string
    e.delete(0, END)
    string = ""


def button_back():
    global string
    global num2
    num2=e.get()
    e.delete(len(num2)-1,END)
    string2 = ""
    for i in range(len(string) - 1):
        string2 += string[i]
    string = string2



e = Entry(root, width=60, bg="black", fg="green", borderwidth=10)
e.grid(row=0, column=0, rowspan=2, columnspan=5, padx=10, pady=10)

button_1 = Button(frame, text="1", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(1)).grid(row=4,
                                                                                                                  columnspan=1,
                                                                                                                  column=0)
button_2 = Button(frame, text="2", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(2)).grid(row=4,
                                                                                                                  columnspan=1,
                                                                                                                  column=1)
button_3 = Button(frame, text="3", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(3)).grid(row=4,
                                                                                                                  columnspan=1,
                                                                                                                  column=2)
button_4 = Button(frame, text="4", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(4)).grid(row=3,
                                                                                                                  columnspan=1,
                                                                                                                  column=0)
button_5 = Button(frame, text="5", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(5)).grid(row=3,
                                                                                                                  columnspan=1,
                                                                                                                  column=1)
button_6 = Button(frame, text="6", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(6)).grid(row=3,
                                                                                                                  columnspan=1,
                                                                                                                  column=2)
button_7 = Button(frame, text="7", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(7)).grid(row=2,
                                                                                                                  columnspan=1,
                                                                                                                  column=0)
button_8 = Button(frame, text="8", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(8)).grid(row=2,
                                                                                                                  columnspan=1,
                                                                                                                  column=1)
button_9 = Button(frame, text="9", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(9)).grid(row=2,
                                                                                                                  columnspan=1,
                                                                                                                  column=2)
button_0 = Button(frame, text="0", padx=40, pady=20, fg="white", bg="black", command=lambda: button_click(0)).grid(row=5,
                                                                                                                  columnspan=1,
                                                                                                                  column=1)
button_dot = Button(frame, text=".", padx=41, pady=20, fg="white", bg="black", command=lambda: button_click(".")).grid(
    row=5, columnspan=1,
    column=0)

button_cl = Button(frame, text="clear", padx=30, pady=20, fg="white", bg="black", command=lambda: button_clear()).grid(
    row=5, column=2, columnspan=1)
button_bk = Button(frame, text="<--", padx=33, pady=20, fg="white", bg="black", command=lambda: button_back()).grid(
    row=2, column=4, columnspan=1)
button_ad = Button(frame, text="+", padx=38, pady=20, fg="white", bg="black", command=lambda: button_add()).grid(row=6,
                                                                                                                columnspan=1,
                                                                                                                column=4)
button_eq = Button(frame, text="=", padx=88, pady=20, fg="white", bg="black", command=lambda: button_equal()).grid(row=6,
                                                                                                                  column=1,
                                                                                                                  columnspan=2)
button_sub = Button(frame, text="-", padx=40, pady=20, fg="white", bg="black", command=lambda: button_subtract()).grid(
    columnspan=1,
    row=3, column=4)
button_mul = Button(frame, text="*", padx=40, pady=20, fg="white", bg="black", command=lambda: button_multiply()).grid(
    columnspan=1,
    row=4, column=4)
button_div = Button(frame, text="/", padx=40, pady=20, fg="white", bg="black", command=lambda: button_divide()).grid(
    columnspan=1,
    row=5, column=4)
button_sqqroot = Button(frame, text="√x", padx=35, pady=20, fg="white", bg="black", command=lambda: button_root()).grid(
    columnspan=1,
    row=6, column=0)

root.mainloop()
