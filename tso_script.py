'''
    Скрипт ищет вхождение в строку определенного патерна, почему нахождения присваивает найденное значение ключу в словаре. Записывает словарь в csv файл
'''

import re 
applications = {} 
applications_tso = {} 
# паттерн для нахождения номера tso 
tso_pattern = '9\d{6}' 
 
with open('id_rtits.txt', encoding='utf-8') as output_file_id_rtits: 
    id_rtits_list = [val.strip() for val in output_file_id_rtits.readlines()] 
 
with open('naryad_name.txt', encoding='utf-8') as output_file_naryad_name: 
    naryad_name_list = [val.strip() for val in output_file_naryad_name.readlines()] 
 
for i in range(len(id_rtits_list)): 
    applications[id_rtits_list[i]] = naryad_name_list[i] 
''' 
w = 'W-00079436' 
 
tso_number = re.search(tso_pattern, applications[w]) 
 
print(tso_number.gpoup(0)) 
''' 
try: 
    for key in applications.keys(): 
        tso_number = re.search(tso_pattern, applications[key]) 
        if tso_number != None: 
            applications_tso[key] = 'TSO-' + tso_number.group(0) 
        else: 
            applications_tso[key] = '0' 
 
    with open('output_file.csv', 'w') as output_file: 
        for key, val in applications_tso.items(): 
            print(key, val, sep=';', file=output_file) 
 
except Exception as err: 
    print(type(err), err, key, tso_number)  
 
print('файл записался') 
input()