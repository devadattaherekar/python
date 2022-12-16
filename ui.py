import tkinter as tk

#tk._test()

window=tk.Tk()
window.geometry("800x600+50+50")
window.title("First UI Application using tkinter")
#label1=tk.Label(text="Hello World",fg="light blue",bg="red",font="Ariel",width=30)
#label2=tk.Label(text="Good Bye world!",fg="purple",bg="yellow",font="TimesnewRoman",height=10)
def greet_user_function():
    label1=tk.Label(text="Hello World",fg="light blue",bg="red")
    label1.place(x=50,y=60)

def good_bye_user_function():
    label2=tk.Label(text="Good Bye world!",fg="purple",bg="yellow")
    label2.place(x=50, y=120)

# There are 3 widget managers
# 1.pack() 2.grid() 3.place()
#label1.pack(side="right")
#label1.grid(row=0,column=0)
#label2.grid(row=1,column=20)


button1=tk.Button(text="Greet User",width=30,fg="yellow",bg="purple",command=greet_user_function)
button2=tk.Button(text="Farewell User",width=30,fg="black",bg="pink",command=good_bye_user_function)
button1.place(x=200,y=60)
button2.place(x=200,y=120)


window.mainloop()
#print("hello world")


