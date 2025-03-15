import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")


screenWidget = tk.Frame(window,
                        background="red", 
                        height=100, 
                        width=300)
screenWidget.pack(fill="both")
screenWidget.pack_propagate(False)

number = tk.StringVar()
prevNumber = tk.StringVar()

screen = tk.Label(screenWidget, 
                  textvariable=number,
                  font=("Arial", 20),
                  fg="white",
                  bg="black",
                  anchor=tk.SW
                  )
screen.pack(expand=True, fill="both")

inputWidget = tk.Frame(window,
                       background="green",
                       height=300,
                       width=300
                       )
inputWidget.pack(expand=True, fill="both")
inputWidget.pack_propagate(False)


def addNumber(n):
    number.set(number.get()+n)


lastOper = ""
def operation(n):
    prevNumber.set(number.get())
    global lastOper
    lastOper = n
    number.set("")


def calculate():
    if lastOper == "+":
        number.set(int(prevNumber.get()) + int(number.get()))
    elif lastOper == "-":
        number.set(int(prevNumber.get()) - int(number.get()))
    elif lastOper == "x":
        number.set(int(prevNumber.get()) * int(number.get()))
    elif lastOper == "/":
        if (int(number.get()) == 0):
            number.set("UNDEFINED")
            return
        number.set(int(prevNumber.get())/int(number.get()))


def buttons():
    for i in range(4):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(i, weight=1)
        inputWidget.grid_rowconfigure(i, weight=1)
        inputWidget.grid_columnconfigure(i, weight=1)

    button_0 = tk.Button(inputWidget, text="7", command=lambda: addNumber("7"))
    button_0.grid(row=0, column=0, sticky="nsew")

    button_1 = tk.Button(inputWidget, text="8", command=lambda: addNumber("8"))
    button_1.grid(row=0, column=1, sticky="nsew")

    button_2 = tk.Button(inputWidget, text="9", command=lambda: addNumber("9"))
    button_2.grid(row=0, column=2, sticky="nsew")

    button_4 = tk.Button(inputWidget, text="4", command=lambda: addNumber("4"))
    button_4.grid(row=1, column=0, sticky="nsew")

    button_5 = tk.Button(inputWidget, text="5", command=lambda: addNumber("5"))
    button_5.grid(row=1, column=1, sticky="nsew")

    button_6 = tk.Button(inputWidget, text="6", command=lambda: addNumber("6"))
    button_6.grid(row=1, column=2, sticky="nsew")

    button_8 = tk.Button(inputWidget, text="1", command=lambda: addNumber("1"))
    button_8.grid(row=2, column=0, sticky="nsew")

    button_9 = tk.Button(inputWidget, text="2", command=lambda: addNumber("2"))
    button_9.grid(row=2, column=1, sticky="nsew")

    button_10 = tk.Button(inputWidget, text="3", command=lambda: addNumber("3"))
    button_10.grid(row=2, column=2, sticky="nsew")

    button_13 = tk.Button(inputWidget, text="0", command=lambda: addNumber("0"))
    button_13.grid(row=3, column=1, sticky="nsew")


    button_3 = tk.Button(inputWidget, text="/", command=lambda: operation("/"))
    button_3.grid(row=0, column=3, sticky="nsew")

    button_7 = tk.Button(inputWidget, text="x", command=lambda: operation("x"))
    button_7.grid(row=1, column=3, sticky="nsew")

    button_12 = tk.Button(inputWidget, text=",", command=lambda: operation(",")) # TO BE DONE
    button_12.grid(row=3, column=0, sticky="nsew")

    button_15 = tk.Button(inputWidget, text="+", command=lambda: operation("+"))
    button_15.grid(row=3, column=3, sticky="nsew")

    button_11 = tk.Button(inputWidget, text="-", command=lambda: operation("-"))
    button_11.grid(row=2, column=3, sticky="nsew")

    button_14 = tk.Button(inputWidget, text="=", command=lambda: calculate())
    button_14.grid(row=3, column=2, sticky="nsew")


buttons()

window.mainloop()