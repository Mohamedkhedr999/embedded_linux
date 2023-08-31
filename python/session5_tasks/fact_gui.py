import tkinter as tk
import math
def fact():
    global txt,e1
    input_value = e1.get()
    if input_value.isdigit():
        n = int(input_value)
        f = math.factorial(n)
        txt.configure(text="Factorial of {} is {}".format(n, f))
    else:
        txt.configure(text="Invalid input. Please enter an integer.")
    



window = tk.Tk()
window.geometry("400x120+1000+400")

lbl = tk.Label(window, text="Enter value of integer N: ")
e1 = tk.Entry(window,width=20)

bt = tk.Button(window,text="Validate", width=20,height=1,command= fact)
txt = tk.Label(window, text="")

lbl.grid(row=0,column=0)
e1.grid(row=0,column=1)
txt.grid(row=2,column=0)
bt.grid(row=3,column=1)
tk.mainloop()
