import os
shop_list = []
folder_path = "Databases"
original = "Databases/Spisok.txt"

def check_and_create_file():
    if os.path.exists(original):
        with open(original, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    name, count = line.split(': ')
                    shop_list.append((name, int(count)))
    else:
        with open(original, 'w', encoding="utf-8") as file:
            file.write("")
            print("Создан новый файл")
def add(tovar:str, kolvo:int):
    pozicia = (tovar, kolvo)
    for i in range(len(shop_list)):
        if shop_list[i][0].lower() == tovar.lower():
            shop_list[i]=(shop_list[i][0], shop_list[i][1]+kolvo)
            break
    else:
        shop_list.append(pozicia)
    upload(shop_list)

def remove(tovar:str):
    for i in range(len(shop_list)):
        if shop_list[i][0].lower() == tovar.lower():
            shop_list.pop(i)
            break
    else:
        return None
    upload(shop_list)
    return True
def change(tovar:str, kolvo:int):
    for i in range(len(shop_list)):
        if shop_list[i][0].lower() == tovar.lower():
            shop_list[i]=(shop_list[i][0], kolvo)
            break
    else:
        return None
    upload(shop_list)
    return True

def upload(shop_list):
    with open(original, 'w', encoding="utf-8") as file:
        for name, count in shop_list:
            file.write(f"{name}: {count}\n")
def popitka():
    while True:
        pos = input().split()
        if len(pos) == 2:
            try:
                pos[1] = int(pos[1])
            except ValueError:
                print("Вы ввели некорректные данные, попробуйте ещё раз, тут нужно вводить числа")
            else:
                if pos[1] > 0:
                    break
                else:
                    print("Вы не можете добавить отрицательное кол-во товаров")

        else:
            print("Неверный формат. Введите товар и количество через пробел.")
    return (pos[0], pos[1])
if os.path.exists(folder_path):
    check_and_create_file()
else:
    os.mkdir(folder_path)
    print("Папка создана")
    check_and_create_file()
print("Приветствую в меню")
print("Здесь вы моженте смотреть и менять ваш список покупок")
while True:
    a = input("Выберите действие: 'Добавить', 'Удалить', 'Изменить количесвто', 'Показать списпок': ").lower().strip()
    if a == "добавить":
        print("Напишите наименование товара и его количество, через пробел")
        position, count = popitka()
        add(position.capitalize(), count)
        print(f"Вы успешно добавили позицию: {position}, в количестве {count} шт.")
    elif a == "удалить":
        print(shop_list)
        while True:
            pos = input()
            prov = remove(pos)
            if prov:
                print(f"Успех\nВы удалили товар: {pos}")
                break
            else:
                print("Товар не найден, попробуй те ещё раз")
    elif a== "изменить количество":
        print("Напишите наименование товара и его количество, через пробел")
        position, count = popitka()
        prov = change(position, count)
        if prov:
            print(f"Успех\nВы изменили количество товара:{position}, на {count}")
        else:
            print("Товар не найден, попробуй те ещё раз")
    elif a == "показать список":
        print(shop_list)
    elif a == "закрыть":
        break
    else:
        print("Такой команды нет")
print("До новых покупок. Досвидания!!!")
exit(0)


