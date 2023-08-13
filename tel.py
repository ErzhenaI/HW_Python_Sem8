def initial_notes ():
    with open ('HW_Python_Sem8\phonebook.txt', 'w', encoding='utf-8') as data:
        data.write ('Иванов Иван Иванович 11111\n')
        data.write ('Петров Петр Петрович 22222\n')
        data.write ('Александров Александр Александрович 33333\n')
#initial_notes ()
    

def add_note ():
    surname = input ('Введите фамилию: ')
    name = input ('Введите имя: ')
    patronimic = input ('Введите отчетсво: ')
    phonenumber = input ('Введите номер телефона: ')
    while not phonenumber. isdigit():
        phonenumber = input ('Введите номер телефона: ')
    str = f'{surname} {name} {patronimic} {phonenumber}\n'
    with open ('HW_Python_Sem8\phonebook.txt', 'a', encoding='utf-8') as data:
        data.write (str)

def find_note (str):
    with open ('HW_Python_Sem8\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if str.lower () in line.lower(). split ():
                print (line, end = '')

def delete_note (str):
    lst = []
    with open ('HW_Python_Sem8\phonebook.txt', 'r', encoding='utf-8') as data:
        lst = data.readlines()
        for line in range (len(lst)):
            if str.lower () in lst[line].lower(). split ():
                lst [line] = ''
    with open ('HW_Python_Sem8\phonebook.txt', 'w', encoding='utf-8') as data:
        for i in lst:
            data. write(i)

def edit_note (str):
    delete_note (str)
    add_note ()

def full_note ():
    with open ('HW_Python_Sem8\phonebook.txt', 'r', encoding='utf-8') as data:
        data = data.readlines ()
        data = list (map (lambda x: x.strip (), data))
        print (data)
   
while True:
    com = input ('Выберите команду для работы со справочником (add, all, find, del, ed, stop): ')
    if com.lower () == 'stop':
        break
    if com.lower () == 'add':
        add_note ()
    if com.lower () == 'find':
        str = input ('Что ищете? ')
        find_note (str)
    if com.lower () == 'all':
        full_note ()
    if com.lower () == 'del':
        str = input ('Что ищете? ')
        delete_note (str)
    if com.lower () == 'ed':
        str = input ('Что ищете? ')
        edit_note (str)
