import tkinter as tk

def greeting(l2, t1):
    name = t1.get()
    msg = "Hello "+name+", How are you?"
    l2.config(text = msg)


root = tk.Tk()  # create screen
root.title("My first GUI Application")
root.geometry("500x300")    # set size of screen (width x height)

# visits
l1 = tk.Label(root, text="Enter your name: ")   # print text on screen

"""How to Display content on screen"""
# l1.pack()   # (top -> bottom) formate
l1.grid(row=0, column=0)  # (row and column) formate

""" Text Box """
t1 = tk.Entry(root, width=50)   
t1.grid(row=0, column=1)

l2 = tk.Label(root, text="")
l2.grid(row=2, column=1)

"""-----Botton-----"""
b1 = tk.Button(root, text="Submit", command=lambda:greeting(l2, t1))
b1.grid(row=1, column=1)


root.mainloop()