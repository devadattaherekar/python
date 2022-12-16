import tkinter as tk

#tk._test()

window=tk.Tk()
window.geometry("800x600+50+50")
window.title("Use Text boxes")

var1=tk.StringVar() # declare variables
var2=tk.StringVar()

def copy_function():
    value1=var1.get()
    var2.set(value1)

textbox1=tk.Entry(textvariable=var1)
textbox2=tk.Entry(textvariable=var2)
textbox1.place(x=50,y=60)
textbox2.place(x=50,y=120)

button1=tk.Button(text="COPY",width=30,fg="black",bg="white",command=copy_function)
button1.place(x=200,y=60)

window.mainloop()



