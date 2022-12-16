import tkinter as tk


window=tk.Tk()
window.geometry("800x600+50+50")
window.title("Calculate Total of 2 numbers!")

var1=tk.StringVar() # declare variables
var2=tk.StringVar()
var3=tk.StringVar()

def add_numbers():
    try:
        value1=int(var1.get())+int(var2.get())
    except ValueError as msg:
        label_error_msg=tk.Label(text="Please enter numbers only")
        label_error_msg.place(x=50,y=300)
    else:
        var3.set(value1)

def clear_text():
    var1.set("")
    var2.set("")
    var3.set("")

Label1=tk.Label(text="Enter first Number ")
Label2=tk.Label(text="Enter Second Number ")
Label3=tk.Label(text="Result is ")
Label1.place(x=50,y=60)
Label2.place(x=50,y=120)
Label3.place(x=50,y=180)

textbox1=tk.Entry(textvariable=var1)
textbox2=tk.Entry(textvariable=var2)
textbox3=tk.Entry(textvariable=var3)
textbox1.place(x=200,y=60)
textbox2.place(x=200,y=120)
textbox3.place(x=200,y=180)

button1=tk.Button(text="ADD",fg="black",bg="light blue",width=30,command=add_numbers)
button2=tk.Button(text="CLEAR",fg="black",bg="light pink",width=30,command=clear_text)
button3=tk.Button(text="QUIT",fg="black",bg="yellow",width=30,command=window.destroy)
button1.place(x=500,y=60)
button2.place(x=500,y=120)
button3.place(x=500,y=180)


window.mainloop()



