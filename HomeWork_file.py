
from pprint import pprint

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

pprint (get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
