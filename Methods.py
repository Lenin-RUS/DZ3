a='List (список), tuple (кортеж), set (множество) - это встроенные структуры данных языка python. Каждая из них имеет свои возможности и ограничения. Это позволяет выбрать наиболее подходящий способ хранения информации в программе.'
b=a.split(' ')

#1. Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего. 2. Написать их через запятую с параметрами
b_list=b
print(len(b_list))
print(b_list[9].index('у'))
print(b_list[2:7])
print(b_list[5]+b_list[7])
print(b_list[0].lower())
print(b_list[9].replace('у','.'))

#Повторить процедуру для словарей (dict),
b_dict = {b[i] : i for i in range(len(b))}
print(b_dict.keys())
print(b_dict.values())
print(b_dict.items())
print(b_dict['это'])
print(b_dict.clear())

#3.  кортежей (tuple)
b_tuple=tuple(b)
print(len(b_tuple))
print(b_tuple[9].index('у'))
print(b_tuple[2:7])
print(b_tuple[5]+b_tuple[7])
print(b_tuple[0].lower())
print(b_tuple[9].replace('у','.'))

#строк (str)
b_str='Поиск подстроки в строке. Возвращает номер первого вхождения или -1'
print(len(b_str))
print(b_str.index('о'))
print(b_str[2:7])
print(b_str[5]+b_str[7])
print(b_str[0].lower())
print(b_str[9].replace('у','.'))

#множеств (set)
b_set=set(b)
b.sort()
a_set=set(b[:10])
print(len(b_set))
print('это' in b_set)
print(b_set.issubset(a_set))
print(b_set.issuperset(a_set))
print(b_set.difference(a_set))