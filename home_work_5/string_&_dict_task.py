name1 = "кузнецов Rлексей DdD"
name2 = "салютин Rаксим DdD"
name1 = name1.replace("R", "А", 1,).replace("DdD", "Сергеевич", 1).title()
name2 = name2.replace("R", "М", 1,).replace("DdD", "Петрович", 1).title()

name_list_1 = list(name1)

for index, element in enumerate(name_list_1):
    if element == 'а':
        name_list_1[index] = 'А'

name_list_1 = list(set(name_list_1))
name_list_1.sort()
print('Список ключей первого ФИО:', name_list_1)
print('Длина списка ключей первого ФИО:', len(name_list_1))


name_list_2 = list(name2)

for index, element in enumerate(name_list_2):
    if element == 'а':
        name_list_2[index] = 'А'

name_list_2 = list(set(name_list_2))
name_list_2.sort()
print('Список ключей второго ФИО:', name_list_2)
print('Длина списка ключей второго ФИО:', len(name_list_2))


value_list_1 = []
for value in name_list_1:
    value = ord(value)
    value_list_1.append(value)
print('Список значений словаря для первого ФИО:', value_list_1)


value_list_2 = []
for value in name_list_2:
    value = ord(value)
    value_list_2.append(value)
print('Список значений словаря для второго ФИО:', value_list_2)


name_dict_1 = {}
for i in name_list_1:
    name_dict_1[i] = ord(i)
print('Вывод словаря первого ФИО: ', name_dict_1)


name_dict_2 = {}
for i in name_list_2:
    name_dict_2[i] = ord(i)
print('Вывод словаря второго ФИО: ', name_dict_2)


print('Вывод значения по ключу А: ', name_dict_1['А'])


merged_dict = {**name_dict_1, **name_dict_2}
print('Вывод объединенного словаря: ', merged_dict)


a = set(name_dict_1.keys())
b = set(name_dict_2.keys())
print('Вывод множества из ключей словаря первого ФИО: ', a)
print('Вывод множества из ключей словаря второго ФИО: ', b)


merged_a_b = set.union(a, b)
print('Вывод объединенного множества: ', merged_a_b)


dict_list = list(merged_dict)
set_list = list(merged_a_b)
if dict_list == set_list:
    print('True')
print(dict_list, set_list)