# Library
from tkinter import ttk, CENTER
import tkinter as tk
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
win = tk.Tk()
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


# Function
def new_news():
    def add():
        title = title_input.get()
        news = news_input.get()
        db.collection('News').add({'Title': title, 'News': news})

    win1 = tk.Toplevel()
    win1.title('Create News')
    win1.iconbitmap('new.ico')
    win1.minsize(300, 300)
    win1.geometry('400x400')
    title_label = tk.Label(master=win1, text='Title')
    title_input = tk.Entry(master=win1)
    news_label = tk.Label(master=win1, text='News')
    news_input = tk.Entry(master=win1)
    upload_button = tk.Button(master=win1, text='Upload', command=add)
    title_label.pack()
    title_input.pack()
    news_label.pack()
    news_input.pack()
    upload_button.pack(pady=10)
    win1.mainloop()


def search():
    win2 = tk.Toplevel()
    win2.title('News')
    win2.iconbitmap('new.ico')
    win2.minsize(450, 300)
    search_var = search_title_input.get()
    if search_var == '':
        docs = db.collection('News').get()
        my_tree = ttk.Treeview(win2)
        # Columns
        my_tree['columns'] = ("Title", "News")
        my_tree.column("Title", anchor=CENTER, width=100)
        my_tree.column("News", anchor=CENTER, width=100)

        # Headings
        my_tree.heading('Title', text="Title", anchor=CENTER)
        my_tree.heading('News', text='News', anchor=CENTER)
        ii = 0
        for doc in docs:
            ii += 1
            my_tree.insert(parent='', index='end', iid=ii, values=(doc.to_dict()['Title'],
                                                                   doc.to_dict()['News']))
            my_tree.pack()
    else:
        docs = db.collection('News').where('Title','==', search_var).get()
        my_tree = ttk.Treeview(win2)
        # Columns
        my_tree['columns'] = ("Title", "News")
        my_tree.column("Title", anchor=CENTER, width=100)
        my_tree.column("News", anchor=CENTER, width=100)

        # Headings
        my_tree.heading('Title', text="Title", anchor=CENTER)
        my_tree.heading('News', text='News', anchor=CENTER)
        ii = 0
        for doc in docs:
            ii += 1
            my_tree.insert(parent='', index='end', iid=ii, values=(doc.to_dict()['Title'],
                                                                   doc.to_dict()['News']))
            my_tree.pack()

    win2.mainloop()


# Code
win.title('KO News')
win.iconbitmap('new.ico')
win.minsize(200, 150)
win.geometry('250x250')
new_news_button = tk.Button(master=win, text='Create News', command=new_news)
search_title_input = tk.Entry(master=win)
search_title_button = tk.Button(master=win, text='Search', command=search)
new_news_button.pack(pady=10)
search_title_input.pack()
search_title_button.pack(pady=10)
win.mainloop()
