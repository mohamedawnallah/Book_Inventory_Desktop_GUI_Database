from select import select
from tkinter import *
from turtle import back
from tkinter import messagebox
from matplotlib.pyplot import title
from backend import Database

database = Database('books.db')


class Window(object):
    def __init__(self,window):

        self.window = window

        self.window.wm_title("Bookstore")

        l1 = Label(window,text="Title")
        l1.grid(row=0,column=0)

        l2 = Label(window,text="Author")
        l2.grid(row=0,column=2)

        l3 = Label(window,text="Year")
        l3.grid(row=1,column=0)

        l4 = Label(window,text="ISBN")
        l4.grid(row=1,column=2)

        self.title_text = StringVar()
        self.e1 = Entry(window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(window,textvariable=self.isbn_text)
        self.e4.grid(row=1,column=3)

        self.list1 = Listbox(window, height=6,width=35)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=2)


        sb1 = Scrollbar(window)
        sb1.grid(row=2,column=2,rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)


        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)

        b1 = Button(window,text="View All",width=12,command=self.view_command)
        b1.grid(row=2,column=3)

        b2 = Button(window,text="Search entry",width=12,command=self.search_command)
        b2.grid(row=3,column=3)

        b3 = Button(window,text="Add entry",width=12,command=self.add_command)
        b3.grid(row=4,column=3)

        b4 = Button(window,text="Update selected",width=12,command=self.update_command)
        b4.grid(row=5,column=3)

        b5 = Button(window,text="Delete selected",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)

        b6 = Button(window,text="Close",width=12,command=self.close_command)
        b6.grid(row=7,column=3)
        
        self.view_command()

    def get_selected_row(self,event):
            try: 
                index = self.list1.curselection()[0]
                self.selected_tuple = self.list1.get(index)
                self.fill_entries()
            except IndexError:
                pass


    def fill_entries(self):
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])

        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])

        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])

        self.e4.delete(0,END)
        self.e4.insert(END,self.selected_tuple[4])

    def popup_warning(self,message): 
        messagebox.showwarning(title="Inputs Warning", message=message)

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        
        search_results = database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        print(search_results)
        if   search_results:
            self.list1.delete(0,END)
            for row in search_results:
                self.list1.insert(END,row)
        else:
            self.popup_warning("Please provide AT LEAST one parameter so we can search")

    def add_command(self):
        val = database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        if val:
            self.list1.delete(0,END)
            self.list1.insert(END,self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
        else:
            self.popup_warning("Please provide ALL parameters for book details")

    def delete_command(self):
        try:
            database.delete(self.selected_tuple[0])
            self.view_command() 
        except NameError:
            self.popup_warning("Please SELECT the book you wanna delete first")

    def update_command(self):
        try:
            val = database.update(self.selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            if val:
                    self.list1.delete(0,END)
                    self.list1.insert(END,self.title_text.get(),self.author_text.get(),self.year_text.get(),self.isbn_text.get())
            else:
                    self.popup_warning("Please DON'T let one of parameters empty")
        except NameError:
            self.popup_warning("Please SELECT the book you wanna update first")


    def close_command():
        response = messagebox.askyesno("Exit Warning",message="Do you want to close the application?")
        if response == 1: window.destroy()

    def __del__(self):
        self.window.destroy()
    
    



window = Tk()

Window(window)

window.mainloop()