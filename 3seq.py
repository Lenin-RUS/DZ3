first_set=set(input('Введите элементы первого списка через запятую: ').split(','))
second_set=set(input('Введите элементы второго списка через запятую: ').split(','))
print('Список 1 без элементов списка 2: ', first_set.difference(second_set))