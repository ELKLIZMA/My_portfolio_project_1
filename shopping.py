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
