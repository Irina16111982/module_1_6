# Работа со словарем
from time import process_time

my_dict = {'Ирина': 1982, 'Надя': 1975, 'Андрей': 1985}
print(my_dict)
print(my_dict['Ирина'])
print(my_dict.get('Сергей'))
my_dict.update({"Ксения": 1990,
                "Иван": 1980})
print(my_dict)
q = my_dict.pop('Надя')
print(q)
print(my_dict)

# Работа с множеством

my_set = {1, 5, 5, 5, 9, 8, 15, 2}
print(my_set)
my_set = {1, 5, 5, 5, 9, 8, 15, 2, False, (1, 2, 5), 'set'}
print(my_set)
print(my_set.remove(1)) # Удаляю число 1 из множества
print(my_set)
