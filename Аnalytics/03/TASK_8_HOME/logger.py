from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    """ Функция меню выбора """
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 Вариант: \n\n"
                    f"{surname}\n"
                    f"{name}\n"
                    f"{phone}\n"
                    f"{address}\n\n"
                    f"2 Вариант: \n\n"
                    f"{surname};{name};{phone};{address}\n\n"
                    f"Выберете вариант: "))

    while var != 1 and var != 2:
        print('Неправильный ввод!')
        var = int(input("Введите число: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n\n')


def print_data():
    """ Функция вывода """
    print('Вывожу данные из 1 файла: \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i + 1]))
                j = i
        print(''.join(data_first_list))
    print('Вывожу данные из 2 файла: \n')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = list(f.readlines())
        print(*data_second)
    return data_first, data_second


def put_data():
    """ Функция изменения """
    print('Данные какого файла вы хотите изменить?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неправильный ввод ')
        number_file = int(input('Введите число '))

    if number_file == 1:
        print("Какой контакт поменять?")
        number_journal = int(input('Введите номер контакта:'))
        number_journal -= 1

        print(f'Изменить контакт\n{data_first[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_first = data_first[:number_journal] + [f'{name}\n{surname}\n{phone}\n{address}\n'] + \
                     data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_first))
        print('Изменения сохранены!')
    else:
        print("Какой контакт изменить?")
        number_journal = int(input('Введите номер контакта: '))
        number_journal -= 1

        print(f'Изменить контакт\n{data_second[number_journal]}')
        name = name_data()
        surname = surname_data()
        phone = phone_data()
        address = address_data()
        data_second = data_second[:number_journal] + [f'{name};{surname};{phone};{address}\n'] + \
                      data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_second))
        print('Изменения сохранены!')


def delete_data():
    """Функция удаления"""
    print('Данные какого файла вы хотите удалить?')
    data_first, data_second = print_data()
    number_file = int(input('Введите номер файла: '))

    while number_file != 1 and number_file != 2:
        print('Неправильный ввод ')
        number_file = int(input('Введите номер файла: '))

    if number_file == 1:
        print("Какой контакт вы хотите удалить?")
        number_journal = int(input('Введите номер контакта: '))

        print(f'Удалить контакт\n{data_first[number_journal - 1]}')
        data_first = data_first[:number_journal] + data_first[number_journal + 1:]
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_first))
        print('Контакт удален!')
    else:
        print("Какой контакт вы хотите удалить?")
        number_journal = int(input('Введите номер контакта: '))

        print(f'Удалить контакт\n{data_second[number_journal - 1]}')
        data_second = data_second[:number_journal] + data_second[number_journal + 1:]
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            f.write(''.join(data_second))
        print('Контакт удален!')
