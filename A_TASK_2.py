import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#2C3E50")  # Darker background for the window

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation 
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "!!ERROR!!"
            equation = ""
    label_result.config(text=result)

label_result = tk.Label(root, width=25, height=2, text="", font=("arial", 30), bg="#34495E", fg="#ECF0F1")
label_result.pack()

buttons = [
    ('C', 10, 100, clear, "#E74C3C"), ('/', 150, 100, lambda: show("/"), "#2980B9"), ('%', 290, 100, lambda: show("%"), "#2980B9"), ('*', 430, 100, lambda: show("*"), "#2980B9"),
    ('7', 10, 200, lambda: show("7"), "#3498DB"), ('8', 150, 200, lambda: show("8"), "#3498DB"), ('9', 290, 200, lambda: show("9"), "#3498DB"), ('-', 430, 200, lambda: show("-"), "#2980B9"),
    ('4', 10, 300, lambda: show("4"), "#3498DB"), ('5', 150, 300, lambda: show("5"), "#3498DB"), ('6', 290, 300, lambda: show("6"), "#3498DB"), ('+', 430, 300, lambda: show("+"), "#2980B9"),
    ('1', 10, 400, lambda: show("1"), "#3498DB"), ('2', 150, 400, lambda: show("2"), "#3498DB"), ('3', 290, 400, lambda: show("3"), "#3498DB"), ('=', 430, 400, calculate, "#E67E22"),
    ('0', 10, 500, lambda: show("0"), "#3498DB"), ('.', 290, 500, lambda: show("."), "#2980B9")
]

for (text, x, y, command, color) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#ECF0F1", bg=color, command=command).place(x=x, y=y)
    elif text == '0':
        tk.Button(root, text=text, width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#ECF0F1", bg=color, command=command).place(x=x, y=y)
    else:
        tk.Button(root, text=text, width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#ECF0F1", bg=color, command=command).place(x=x, y=y)

root.mainloop()
