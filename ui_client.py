import tkinter as tk
from tkinter import messagebox
import data

window=tk.Tk()
window.geometry("800x600+50+50")
window.title("Cricketers Database Operations!")

var1=tk.StringVar() # declare variables
var2=tk.StringVar()

Label1=tk.Label(text="Enter Cricketer Name ")
Label2=tk.Label(text="Enter Cricketer Country ")

Label1.place(x=50,y=60)
Label2.place(x=50,y=120)


textbox1=tk.Entry(textvariable=var1)
textbox2=tk.Entry(textvariable=var2)

textbox1.place(x=200,y=60)
textbox2.place(x=200,y=120)

def user_add_cricketer():
    data.add_cricketer(var1.get(),var2.get())
    messagebox.showinfo("Add record successful",f"{var1.get()} added successfully!").place(x=500,y=400)

def user_delete_cricketer():
    data.delete_cricketer(var1.get())

def user_search_cricketer():
    all_records=data.display_cricketers()
    name = var1.get()
    count_records=0
    for each_record in all_records:
        if each_record["name"]==name:
            messagebox.showinfo("Record Present",f"{var1.get()} is present in database!").place(x=500, y=400)
            break
        count_records+=1
    if count_records==len(all_records):
        tk.Label(text="Record is not present!").place(x=500,y=330)

def user_display_cricketers():
    all_cricketers=data.display_cricketers()
    for record in all_cricketers:
        tk.Label(text=f'{record["name"]} plays for {record["country"]}').pack()

button1=tk.Button(text="ADD",fg="black",bg="light blue",width=30,command=user_add_cricketer)
button2=tk.Button(text="DELETE",fg="black",bg="light pink",width=30,command=user_delete_cricketer)
button3=tk.Button(text="SEARCH",fg="black",bg="light blue",width=30,command=user_search_cricketer)
button4=tk.Button(text="DISPLAY ALL",fg="black",bg="light pink",width=30,command=user_display_cricketers)
button5=tk.Button(text="QUIT",fg="black",bg="yellow",width=30,command=window.destroy)

button1.place(x=500,y=60)
button2.place(x=500,y=120)
button3.place(x=500,y=180)
button4.place(x=500,y=240)
button5.place(x=500,y=300)

window.mainloop()



