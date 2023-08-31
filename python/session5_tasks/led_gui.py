import tkinter as tk
def led_on() :
    global cnvs,led,text_id 
    cnvs.itemconfig(led,fill = "red")
    cnvs.itemconfig(text_id,text = "led is on", font=("Arial", 12))

def led_off():
    global cnvs, led,text_id
    cnvs.itemconfig(led,fill = "black")
    cnvs.itemconfig(text_id,text = "led is off", font=("Arial", 12))



window = tk.Tk()
window.geometry("400x400+1000+250")
window.resizable(False,False)

cnvs = tk.Canvas(window, width= 400, height=400)
led= cnvs.create_oval(50, 50, 200, 150, fill='black', outline='black')
text_id = cnvs.create_text(130, 170, text="led is off", font=("Arial", 12))
bt1 = tk.Button(window,text="led on" ,width = 10 ,height =1 ,command= led_on)
bt2 = tk.Button(window,text="led off",width = 10 ,height =1 ,command= led_off)

cnvs.place(x=0,y=0)
bt1.place(x=150,y=300)
bt2.place(x=150,y=330)


tk.mainloop()