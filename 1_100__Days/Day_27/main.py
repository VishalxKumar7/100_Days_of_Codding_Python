import tkinter

def button_clicked():
    # print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

# Lable
my_label = tkinter.Label(text = "I'm a Label", font=("Arial", 12, "italic"))
# my_label.pack(side="top")
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = tkinter.Entry(width=10)
input.grid(column=2, row=3)
input.get()




window.mainloop()