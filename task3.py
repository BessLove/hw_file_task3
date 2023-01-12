import os

def count_strings(file_p):
    '''Узнаем количество строк в файле'''
    with open(file_p, encoding='utf-8') as file_object:
        lenth = len(file_object.readlines())
        return lenth

def print_lines(file_p):
    '''Считываем строки из файла в список'''
    with open(file_p, encoding='utf-8') as file_object:
        lines = file_object.readlines()
        return lines

def count_files():
    '''Формируем список кортежей (имя файла, количество строк)'''
    with os.scandir('.') as entries:
        len_name = []
        for entry in entries:
            if entry.name != 'task3.py' and entry.name != 'my_file.txt':
               len_name.append((entry.name,count_strings(entry)))
        return len_name


my_list = sorted(count_files(), key = lambda x: x[1])
#Записываем отсортированные данные в файл
with open('my_file.txt','w', encoding='utf-8') as my_file:
    for item in my_list:
        for string in item:
            my_file.write(f'{string}\n')
        for i in print_lines(item[0]):
            my_file.write(i)
        my_file.write('\n')
