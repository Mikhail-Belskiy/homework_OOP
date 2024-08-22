
from pprint import pprint
import os

cook_book = {}
with open('/home/mikl/Рабочий стол/homework/recipes.txt', 'rt', encoding = "utf-8") as file:
    for l in file:
        dish_name = l.strip()
        new_list = []
        count = file.readline()
        for i in range(int(count)):
            dish_ing = file.readline()
            ingredient_name, quantity, measure  = dish_ing.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity,'measure': measure})
            dep = {dish_name: new_list}
        separate = file.readline()
        cook_book.update(dep)

#pprint(f'cook_book = {cook_book}')



def get_shop_list_by_dishes (dishes:list, person_count: int):
    ingridients = {}
    for dish in dishes: # dish = омлет
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                if ingridient ['ingredient_name'] in ingridients:
                    ingridients [ingridient['ingredient_name']]['quantity'] += int(ingridient['quantity']) * person_count
                else:
                    ingridients [ingridient['ingredient_name']]: ingridients[ingridient['ingredient_name']] ={'measure':ingridient['measure'],'quantity':int(ingridient['quantity']) * person_count} 
        else:    
            print(f'Блюда "{dish}" нет в книге рецептов')
    return ingridients

#pprint (get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




with open('/home/mikl/Рабочий стол/homework/HW_files/1.txt', 'rt', encoding = "utf-8") as f1, open('/home/mikl/Рабочий стол/homework/HW_files/2.txt', 'rt', encoding = "utf-8") as f2, open('/home/mikl/Рабочий стол/homework/HW_files/3.txt', 'rt', encoding = "utf-8") as f3, open('/home/mikl/Рабочий стол/homework/HW_files/answer.txt', 'a+', encoding = "utf-8") as f4:

    line1 = f1.readlines()
    len_line_1 = len(line1)
    file_path_1 = '/home/mikl/Рабочий стол/homework/HW_files/1.txt'
    file_name_1 = os.path.basename(file_path_1)

    line2 = f2.readlines()
    len_line_2 = len(line2)
    file_path_2 = '/home/mikl/Рабочий стол/homework/HW_files/2.txt'
    file_name_2 = os.path.basename(file_path_2)

    line3 = f3.readlines()
    len_line_3 = len(line3)
    file_path_3 = '/home/mikl/Рабочий стол/homework/HW_files/3.txt'
    file_name_3 = os.path.basename(file_path_3)

    dict_ = {len_line_1: [line1, file_name_1], len_line_2:[line2, file_name_2], len_line_3: [line3, file_name_3]}
    sort_list = dict(sorted(dict_.items()))


    for key, value in sort_list.items():  #хочу яерез цикл из словаря записать в файл решение, добавив через basename() 
        f4.write(f'\n{key}\n')
        f4.write(f'{value[1]} \n')
        f4.write(f'{"".join(value[0])}')
#print(sort_list)
print(f4)







