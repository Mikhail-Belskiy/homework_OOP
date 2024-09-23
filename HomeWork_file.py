
from pprint import pprint
import os


with open('/home/mikl/Рабочий стол/homework/recipes.txt', 'rt', encoding = "utf-8") as file:
    cook_book = {}
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




import os

dict_= {}

for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(os.path.join(filename), 'r', encoding='utf-8') as f:
            text = f.readlines()
            len_line = len(text)
            dict_.update({len_line: [filename, text]})
dict_sorted = dict(sorted(dict_.items()))
#print(dict_sorted)
with open('/home/mikl/Рабочий стол/homework/answer.txt', 'a+', encoding = 'utf-8') as f4:
    for key, value in dict_sorted.items(): 
        f4.write(f'Длина строки: {key}\n')
        f4.write(f'Имя файла: {"".join(value[0])}\n')
        f4.write(f'{"".join(value[1])} \n')







