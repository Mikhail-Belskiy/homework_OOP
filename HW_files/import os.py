import os

dict_= {}

for filename in os.listdir():
    if filename.endswith(".txt"):
        with open(os.path.join(filename), 'r', encoding='utf-8') as f:
            text = f.readlines()
            len_line = len(text)
            dict_.update({len_line: [filename, text]})
#dict_2 = dict.fromkeys(dict_)
dict_sorted = dict(sorted(dict_.items()))
#print(dict_sorted)
with open('/home/mikl/Рабочий стол/homework/answer.txt', 'a+', encoding = 'utf-8') as f4:
    for key, value in dict_sorted.items(): 
        f4.write(f'Длина строки: {key}\n')
        f4.write(f'Имя файла: {"".join(value[0])}\n')
        f4.write(f'{"".join(value[1])} \n')
                    





                    #for i in dict_sorted:
                    #f4.write(f'{i[0]} {i[1][0]}')
                    #for j in i[1][1]:
                        #f4.write(j)