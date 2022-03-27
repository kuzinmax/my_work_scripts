""" 
    Проверка количества вхождений наименований в файле regions.txt 
    Файл должен содержать один столбец со значениями. Скрипт очищает список от пустых значений и выводит количество упоминаний каждого значения. 
""" 
 
 
# Чтение файла и очищение его от пустых значений 
file_for_check = input('Введите название файла без указания разрешения (файл должен быть в txt формате): ') 
 
file_for_check_txt_format = file_for_check + '.txt' 
 
with open(file_for_check_txt_format, encoding='utf-8') as input_file: 
    regions = [val.strip() for val in input_file.readlines()] 
clear_regions = [] 
 
# выделение уникальных значений из первоначального списка 
for i in range(len(regions)): 
    if regions[i] != '': 
        clear_regions.append(regions[i]) 
set_region = {val for val in clear_regions}    
dict_region = {} 
 
# наполнение ключом и значений. Значение - это количество вхождений 
for val in set_region: 
    dict_region[val] = clear_regions.count(val) 
 
sorted_dict = sorted(dict_region, key=lambda pair: pair[1]) 
 
output_file_csv = 'output', file_for_check, '.csv' 
 
# запись значений в файл 
with open(output_file_csv, 'w') as output_file: 
    for x in sorted_dict: 
        print(x, sorted_dict[x], sep=';', file=output_file) 
 
print('загрузка произошла успешно в файл, проверяйте') 
input()