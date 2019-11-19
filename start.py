from tkinter import *
from tkinter import messagebox, IntVar
import pymysql
import json



root = Tk()
def close_root():
    root.withdraw()


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
        # Se il login la pass e l-altra pass sono inserite
        if entry_new_login.get() and entry_new_pass.get() and entry_new_pass2.get():
            # Se le password coincidono
            if entry_new_pass.get() == entry_new_pass2.get():
                # Se l-utente ha accettao le condizioni !!!!! Qui ho l-errore che non funziona un cazzo
                if accept.get() == 0:

                    # Apro il file per leggerlo ed estrarre tutti i dati
                    filename = 'accounts.txt'
                    with open(filename, 'r+', encoding='Latin-1') as file:
                        users = json.load(file)
                    # Ricavo tutti i dizionari dalla lista
                    for user in users:
                        # Per ora non so come cavolo evitare il print, altrimenti non salva nulla
                        print('')
                    # Qui controllo se il nuovo login e gia registrato o meno, in caso di si, continuamo
                    if not entry_new_login.get() in user:
                        # Apriamo di nuovo il file, ma stavolta per sovrasscriverlo, utilizzando la vecchia lista users e il vecchio dizionario
                        with open(filename, 'w', encoding='Latin-1') as file:

                            user[entry_new_login.get()] = entry_new_pass2.get()

                            # Aggiungo il log e file nel grande dizionario

                            json.dump(users, file)
                    if registration:
                        root.deiconify()
                        root1.destroy()

                    else:
                        messagebox.showerror("Errore", 'Sei gia registrato, cavolo!')
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
    # Quando premo il tasto di registrazione la finestra di entrata si chiude
    if btn_registration:
        root.withdraw()
        close_root()

    btn_registration.grid(columnspan=4, sticky=E)




# Условие входа
def def_login():
    # Apriamo il file per estrarre le info
    with open('accounts.txt', 'r', encoding='Latin-1') as file:
        users = json.load(file)
        for user in users:
            print('')

    # Se login e pass inseriti
    if entry_login.get() and entry_pass.get():
        # Se il login e nella lista dei dizionari
        if entry_login.get() in user:
            # Se la pass inserito coincide al key nel dizionario
            if entry_pass.get() == user[entry_login.get()]:
                system()
                root.withdraw()
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

# Finestra principale di lavoro
def system():

    def exit_win():
        root2.destroy()
    def profile():
        login = Label(root2, text='Il mio login: ' + str(entry_login.get()))
        login.grid(column=1, row=2)
    root2 = Tk()
    root2.title('DroN - Управление')
    root2.geometry('750x850')

    main_menu = Menu(root2)
    root2.configure(menu=main_menu)
    file = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="File", menu=file)
    file.add_command(label="Профиль", command=profile)
    file.add_command(label="Настройки")
    file.add_separator()
    file.add_command(label="Выйти из программы", command=exit_win)

    crm = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="CRM", menu=crm)
    crm.add_command(label="Новая сделка")
    crm.add_command(label="Список сделок")

    to_do = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Задачи", menu=to_do)
    to_do.add_command(label="Новая задача")
    to_do.add_command(label="Все задачи")

    kompanii = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Компании", menu=kompanii)
    kompanii.add_command(label="Добавить компанию")
    kompanii.add_command(label="Список компаний")

    finansy = Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Финансы", menu=finansy)
    finansy.add_command(label="Поступление д/с")
    finansy.add_command(label="Все поступления")




root.mainloop()