def get_Data():
    data = []
    surname = input('Введите фамилию: ')
    data.append(surname)
    name = input('Введите имя: ')
    data.append(name)
    mname = input('Введите отчество: ')
    data.append(mname)
    number = input('Введите номер телефона: ')
    data.append(number)
    return data

def menu():
    print('\nГлавное меню: \n'
          '\n1. Открыть CSV файл\n'
          '2. Добавить контакт в CSV- файл\n'
          '3. Поиск контакта\n'
          '4. Выход')
    return(int(input('->> ')))







