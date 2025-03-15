import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.geometry("300x400")

        #SHOWS NUMBER
        self.screenFrame = tk.Frame(self.master,
                          height=100,
                          width=300,
                          bg="green")
        self.screenFrame.pack()
        self.screenFrame.pack_propagate(False)

        self.numScreen = tk.Entry(self.screenFrame,
                          width=280,
                          bd=5,
                          font=("Arial", 20))
        self.numScreen.pack()

        ##ALL INPUT BUTTON
        buttonFrame = tk.Frame(self.master,
                          height=300,
                          width=300,
                          bg="black")
        buttonFrame.pack()
        buttonFrame.pack_propagate(False)

        buttonLayout = [
            ("*", 0, 0), ("*", 0, 1), ("*", 0, 2), ("C", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            (",", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for text, rows, cols in buttonLayout:
            butt = tk.Button(buttonFrame,
                      font=("Arial",8),
                      text=text,
                      padx=1,
                      pady=1,
                      width=11,
                      height=4,
                      command=lambda t=text: self.on_click(t))
            butt.grid(row=rows, column=cols,sticky="nsew")

    def on_click(self, n):
        if (n == "C"):
            self.clear()
        elif (n == "="):
            res = eval(self.numScreen.get())
            self.clear()
            self.numScreen.insert(tk.END, str(res))
        else:
            self.numScreen.insert(tk.END, n)
        
    def clear(self):
        self.numScreen.delete(0, tk.END)


win = tk.Tk()
calculator = Calculator(win)
win.mainloop()

