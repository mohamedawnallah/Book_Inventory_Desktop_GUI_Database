from select import select
from tkinter import *
from turtle import back
from tkinter import messagebox
from matplotlib.pyplot import title
import backend

def get_selected_row(event):
        try:
            global selected_tuple
            index = list1.curselection()[0]
            selected_tuple = list1.get(index)
            fill_entries()
        except IndexError:
            pass


def fill_entries():
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])

    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])

    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])

    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])



def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    
    search_results = backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    print(search_results)
    if   search_results:
        list1.delete(0,END)
        for row in search_results:
            list1.insert(END,row)
    else:
        popup_warning("Please provide AT LEAST one parameter so we can search")

def add_command():
    val = backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    if val:
        list1.delete(0,END)
        list1.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    else:
        popup_warning("Please provide ALL parameters for book details")

def delete_command():
    try:
        backend.delete(selected_tuple[0])
        view_command() 
    except NameError:
        popup_warning("Please SELECT the book you wanna delete first")

def update_command():
    try:
       val = backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
       if val:
            list1.delete(0,END)
            list1.insert(END,title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
       else:
            popup_warning("Please DON'T let one of parameters empty")
    except NameError:
        popup_warning("Please SELECT the book you wanna update first")

def close_command():
    response = messagebox.askyesno("Exit Warning",message="Do you want to close the application?")
    if response == 1: window.destroy()
    
def popup_warning(message):
    messagebox.showwarning(title="Inputs Warning", message=message)


window = Tk()
window.wm_title("Bookstore")

l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1 = Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)


sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


list1.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=close_command)
b6.grid(row=7,column=3)

view_command()
window.mainloop()