from tkinter import *
from tkinter import messagebox, IntVar
import pymysql
import pickle

root = Tk()
root.title('DroN')
root.geometry('260x120')
# Надписи логин и пароль
label_login = Label(root, text='Login')
label_pass = Label(root, text='Password')

# Ввод логина и пароля
entry_login = Entry(root)
entry_pass = Entry(root, show='*')

check_botton = Checkbutton(root, text='Запомнить пароль и остаться в системе!')

# Надписи логин и пароль в таблицу
label_login.grid(column=0, row=1, sticky=E)
label_pass.grid(column=0, row=2, sticky=E)

# Ввод логина и пароля в таблицу
entry_login.grid(column=1, row=1)
entry_pass.grid(column=1, row=2)

# Галочка остаться в системе
check_botton.grid(columnspan=4, sticky=E)

# Регистрация
accounts = {'arti': 'arti'}
def registration():
    root1=Tk()
    root1.title('DroN - Регистрация')
    root1.geometry('350x120')

    # Testo login e password
    new_login_text = Label(root1, text='Nuovo Login')
    new_pass_text = Label(root1, text='Nuova password')
    new_pass_text2 = Label(root1, text='Nuova password')

    # Inserire testo e password
    entry_new_login = Entry(root1)
    entry_new_pass = Entry(root1, show='*')
    entry_new_pass2 = Entry(root1, show='*')

    # Ввод логина и пароля в таблицу
    new_login_text.grid(column=0, row=1, sticky=E)
    new_pass_text.grid(column=0, row=2, sticky=E)
    new_pass_text2.grid(column=0, row=3, sticky=E)

    entry_new_login.grid(column=1, row=1)
    entry_new_pass.grid(column=1, row=2)
    entry_new_pass2.grid(column=1, row=3)



    # Bottone registrzione
    def save():
        if entry_new_login.get() and entry_new_pass.get() and entry_new_pass2.get():
            if entry_new_pass.get() == entry_new_pass2.get():
                if accept.get() == 0:
                    accounts = {}
                    filename = 'accounts.txt'
                    accounts[str(entry_new_pass.get())] = str(entry_new_pass2.get())
                    file = open(filename, 'ab')
                    pickle.dump(accounts, file)
                    file.close()
                else:
                    messagebox.showerror("Errore", 'Dovete accettare le condizioni')
            else:
                messagebox.showerror("Errore", 'Le password non coincidono')
        else:
            messagebox.showerror("Errore", 'Riempite tutti i campi')

    accept = BooleanVar()

    check_registration = Checkbutton(root1, text='Sono d accordo con tutto', variable=accept, onvalue=1, offvalue=0)
    check_registration.grid(columnspan=4, sticky=E)

    btn_registration = Button(root1, text='Зарегестрироваться', command=save)
    btn_registration.grid(columnspan=4, sticky=E)




# Условие входа

def def_login():

    if entry_login.get() and entry_pass.get():
        if entry_login.get() in accounts:
            if entry_pass.get() == accounts[entry_login.get()]:
                messagebox.showinfo("Successo!", 'Sei nella lista')
            else:
                messagebox.showerror("Errore", 'La pass e errata')
        else:
            messagebox.showerror("Errore", 'NON sei nella lista, registrati!')
    else:
        messagebox.showerror("Ошибка", 'Non hai inserito login o password')


# Кнопки регистрации и входа
registration = Button(root, text='Регистрация', command=registration)
entry_in_system = Button(text='Войти', command=def_login)


# Кнопки регистрации и входа в таблице
registration.grid(column=0, row=5, sticky=E)
entry_in_system.grid(column=1, row=5, sticky=E)



root.mainloop()