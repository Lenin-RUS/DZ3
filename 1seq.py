all_strings=int(input('Введите количество строк: '))
str_val=[]
for string in range(all_strings):
  str_val.append(int(input(f'Введите {string+1} элемент: ')))
str_val.sort()
print(str_val)