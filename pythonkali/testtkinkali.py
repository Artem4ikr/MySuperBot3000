from tkinter import  *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os, random


root = Tk()



def main():
    global logiN, passW
    logiN = 'Artem'
    passW = 'Artem123'
    log_pass(root)
    root.title('login')
    root.geometry('400x200')
    root.mainloop()



def log_pass(window):
    login = Entry(window, bg='grey')
    login.place(x=120, y=90, width=100, height=30)



    password = Entry(window, bg='grey', show='*')
    password.place(x=120, y=115, width=100, height=30)

    button_login = Button(window, text='Log in', bg='yellow', command=lambda: get_key(login.get(), password.get()))
    button_login.place(x=120, y=150, width=100, height=30)

    button_forg = Button(window, text='forgot password', bg='yellow', command=lambda:  forget_pass())
    button_forg.place(x=20, y=150, width=80, height=30)

    num1 = Label(root, text='Login:')
    num1.place(x=20, y=90, width=100, height=30)

    num1 = Label(root, text='Password:')
    num1.place(x=20, y=120, width=100, height=30)

def forget_pass():
    forget_sc = Toplevel()

    secret_question = ttk.Combobox(forget_sc, values=['Your first best friend', 'How old is your best friend'])
    secret_question.grid(row=0, column=0)

    secret_answer = Entry(forget_sc)
    secret_answer.grid(row=1, column=0)

    check_btn = Button(forget_sc, text='check', command=lambda: answer(forget_sc, secret_question.get(), secret_answer.get()))
    check_btn.grid(row=2, column=0)

    forget_sc.mainloop()

def answer(window, quest, ans):
    dict_quest = {
        'Your first best friend': 'Olya',
        'How old is your best friend': '14'
    }

    if dict_quest[quest] == ans:
        window.destroy()
        new_log_pass_window = Tk()

        new_log = Entry(new_log_pass_window)
        new_log.grid(row=0, column=0)

        new_pass = Entry(new_log_pass_window)
        new_pass.grid(row=1, column=0)

        new_btn = Button(new_log_pass_window, text='New login and password', command= lambda: new_acc(new_log_pass_window, new_log.get(), new_pass.get()))
        new_btn.grid(row=3, column=0)

        new_log_pass_window.mainloop()

def get_key(login, password):
    if login == logiN and password == passW:
        print('you are in')
        mem_window()
    else:
        print('ERROR')

def new_acc(window, login, password):
    window.destroy()
    global  logiN, passW
    logiN = login
    passW = password

def mem_window():
    mem_sc = Toplevel()
    directory = os.listdir('img')
    rand_img = random.choice(directory)
    img = Image.open('img/' + rand_img)
    img = ImageTk.PhotoImage(img)

    picture = Label(mem_sc, image=img)
    picture.image = img
    picture.grid(row=0, column=0)





if __name__== '__main__':
    main()






































































































































