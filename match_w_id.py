'''
    Скрипт ищет вхождение в строку определенного патерна, почему нахождения присваивает найденное значение ключу в словаре. Записывает словарь в файл
'''

import re 
applications = {} 
w_pattern = 'w-\d{8}' 
 
with open('id_application.txt', encoding='utf-8') as inputfile_id_sbs: 
    id_application_sbs_list = [val.strip() for val in inputfile_id_sbs.readlines()] 
 
with open('info_fields_2_dol.txt', encoding='utf-8') as inputfile_infofield_sbs: 
    info_field_list = inputfile_infofield_sbs.read().split('&') 
 
print(len(id_application_sbs_list), type(info_field_list), len(info_field_list), sep='\n') 
 
for i in range(len(id_application_sbs_list)): 
    applications[id_application_sbs_list[i]] = info_field_list[i].lower() 
 
 
with open('output_file_applications_w_number.txt', 'w') as output_file_w_number: 
    print('key', 'w-number', sep=':', file=output_file_w_number) 
    for key in applications.keys(): 
        w_number = re.search(w_pattern, applications[key]) 
        if w_number != None:     
            applications[key] = w_number.group() 
            print(key, applications[key], sep=':', file=output_file_w_number) 
        else: 
            applications[key] = w_number 
            print(key, applications[key], sep=':', file=output_file_w_number) 
 
print('файл успешно записался') 
input()