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

print(f'cook_book = {cook_book}')