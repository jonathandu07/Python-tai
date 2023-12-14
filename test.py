import tkinter as tk



print("Voici une calculatrice avec une interface graphique!")

window = tk.Tk()

e1 = tk.Entry(window)
e2 = tk.Entry(window)
b = tk.Button(window, text="Calculer")
e3 = tk.Message(window)
e4 = tk.Button(window,text="+")
e5 = tk.Button(window,text="-")
e6 = tk.Button(window,text="X")
e7 = tk.Button(window,text="/")

add = False
sous = True
prod = True
div = True

e1.grid(row=0, column=0)
e2.grid(row=1, column=0)
b.grid(row=2, column=0)
e3.grid(row=3, column=0)
e4.grid(row=0, column=10)
e5.grid(row=1, column=10)
e6.grid(row=2, column=10)
e7.grid(row=3, column=10)

def calculer():
    a = int(e1.get())
    b = int(e2.get())
    c = e4["text"]
    d = e5["text"]
    e = e6["text"]

    if c == "+":
        result = a + b
    if d == "-" :
        result = a - b
    if e == "X" :
        result = a * b
    else:
        result = a / b

    e3.config(text=int(result))
    print(result)

def addition():
    add = False
    sous = False
    prod = False
    div = False
    return (add, sous, prod, div)

def soustraction():
    add = False
    sous = True
    prod = False
    div = False
    return (add, sous, prod, div)

b.config(command=calculer)


window.mainloop()