import model
import sys

def reg():
    login = (input("Придумайте логин\n")).lower()
    password  = input("Придумайте пароль\n")
    email = (input("Введите емейл\n")).lower()
    model.read_db()
    if model.reg_db(login,password,email) == True:
        print('Регистрация прошла успешно.')
        return reg_or_auth()
    else:
        print('Ошибка при регистрации. Возможно, логин уже занят или одно из полей пустое.')
        return reg()

def auth():
    login = (input("Введите свой логин\n")).lower()
    password = input("Введите пароль\n")
    if model.auth_db(login,password) == True:
        print("Вы успешно авторизовались.")
        return operation_notes(login)
    else:
        print('Данные для входа не верны.')
        return reg_or_auth()

def reg_or_auth():
    while True:
        choose = input("Выберите:\n[1]Авторизация\n[2]Регистрация\n")
        if choose == '1':
            print("Вы выбрали Авторизацию\n")
            return auth()
        if choose == '2':
            print("Вы выбрали Регистрацию\n")
            return reg()
        else:
            print("Повторите выбор(Нужно ввести цифру 1 или 2)")


def show_notes(login):
    notes = model.show_notes(login)
    #prepared_list = [a,b,c for a,b,c in zip(notes[::2], notes[:1:2]['title'],notes[:1:2]['datetime'])]
    if not notes:
        print('У вас нет ни одной заметки.')
        while True:
            choice = input("Хотите создать?\n[1]Да\n[2]Нет\n")
            if choice == '1':
                create_note(login)
            if choice == '2':
                sys.exit('Ну как хотите, больше тут делать нечего.')
            else:
                print('Несуществующтй выбор.  ', choice)


    print('{:<30}{:<30}{:<}'.format("Номер", "Название", "Дата и время"))
    for a,b in zip(notes[::2], notes[1::2]):

        print('{:<30}{:<30}{:<}'.format(a, b['title'], b['datetime']))

def operation_notes(login):
    show_notes(login)

    while True:
        print('\n\nСделайте выбор:')
        choice = input('[1]Создать заметку\n[2]Удалить заметку\n[3]Прочесть заметку\n')
        if choice == "1":
            print('Вы выбрали Создание заметки.')
            create_note(login)
            break
        elif choice == "2":
            print('Вы выбрали Удаление заметки.')
            del_note(login)
            break
        elif choice == "3":
            print('Вы выбрали Чтение заметки.')
            read_note(login)
            break
        else:
            print("Сделавйте существующий выбор")

def create_note(login):
    print("НОВАЯ ЗАМЕТКА")
    title = input('Введите название заметки:\n')
    body = input('Введите текст заметки:\n')
    try:
        model.add_note_db(login, title, body)
        print("Заметка успешно создана")
    except:
        print("Неизветная ошибка при создании заметки")
    finally:
        operation_notes(login)

def del_note(login):
    print("УДАЛЕНИЕ ЗАМЕТКИ")
    while True:
        num = input('Какой номер заметки нужно удалить?\n')
        try:
            model.del_note(login, num)
            print("Заметка успешно удалена")
            operation_notes(login)
            break
        except IndexError:
            print("Такого номера заметки не существует.")
            continue
        except ValueError:
            print("Введите номер(цифру) заметки.")
            continue


def read_note(login):
    print("ЧТЕНИЕ ЗАМЕТКИ")
    while True:
        num = input('Какой номер заметки нужно прочесть?\n')
        try:
            print("Название: ", model.show_note(login, num)['title'])
            print("Текст: ", model.show_note(login, num)['body'])
            print("Дата создания: ", model.show_note(login, num)['datetime'])
            print('\n\n')
            operation_notes(login)
            break
        except IndexError:
            print("Такого номера заметки не существует.")
            continue
        except ValueError:
            print("Введите номер(цифру) заметки.")
            continue




print("Вас приветствует примитивная программа по работе с заметками\"Notes за 10 часов\"!")
try:
    model.read_db()
except FileNotFoundError:
    model.save_db()

reg_or_auth()


