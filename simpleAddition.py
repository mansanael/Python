from tkinter import *

root = Tk()
root.title("Simple Addition")
root.geometry("300x200")

def calculatef():
    try:
       value1 = int(myValue1.get())
       value2 = int(myValue2.get())
       sumofvalue = value1+value2
       result.config(text=sumofvalue)
    except ValueError:
        result.config(text="Please enter a number")

myLabel1 = Label(root, text="Please Enter first number")
myLabel1.pack(pady=3)

myValue1 = Entry(root)
myValue1.pack(pady=2)

myLabel2 = Label(root, text="Please Enter second number")
myLabel2.pack(pady=3)

myValue2 = Entry(root)
myValue2.pack(pady=2)

myButton = Button(root, text="Calculate", command=calculatef)
myButton.pack(pady=3)

result = Label(root, text='')
result.pack(pady=3)
root.mainloop()