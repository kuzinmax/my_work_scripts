'''
    Цель создания данного скрипта: присвоение определенному адресу в Адресном плане работ (АП) рабочей группы на основании предыдущих присваиваний. Работая группа - это состав работников того или иного района РФ.
    Как работает скрипт: 
    1. Скрипт считывает файл с регионами и районами РФ
    2. Считывает файл с новыми адресами, которым необходимо присвоить рабочую группу
    3. Считывает адреса и рабочие группы, которые уже были отработаны ранее.
    4. Делает сопоставление района и рабочей группы поиском по старому адресному плану (сначала ищет регион, а затем ищет название района в регионе)
    5. Подставляет в новом АП рабочую группу по району (сначала ищет регион, а затем ищет название района в регионе)
    6. Записывает получившиеся значения в файл
'''


def clear_list_from_txt_file(file_title):
    with open(file_title, encoding='utf-8') as input_file:
        output_list = [val.strip().lower() for val in input_file.readlines()]
    return output_list
    
region_and_district = clear_list_from_txt_file('subj_regions.txt')
region_and_district_uniq = []
region_and_district_dict = {}
all_ke_old = clear_list_from_txt_file('adress_ke_wg.txt')
new_ke = clear_list_from_txt_file('new_ke.txt')

#new_ke_13 = clear_list_from_txt_file('new_ke_13.txt')

# добавление уникальных субъектов федерации
for region in region_and_district:
    i = region.index("&")
    if region[:i] in region_and_district_uniq:
        continue
    else:
        region_and_district_uniq.append(region[:i])

# создание словаря    
for elem in region_and_district_uniq:
    region_list = []
   # Ненецкий - дублем добавляет регионы из Ямало-Ненцкого АО. Поэтому занес значения в ручную
    if elem == 'ненецкий':
        region_list.append('заполярный')
    # алтай - дублем добавляет регионы из алтайского. Поэтому занес значения в ручную
    elif elem == 'алтай':
        region_list = ['кош-агачский', 'майминский', 'онгудайский', 'турочакский', 'улаганский', 'усть-канский', 'усть-коксинский', 'чемальский', 'чойский', 'шебалинский']
    else:
        for region in region_and_district:
            i = region.index("&")
            if elem in region:
                if "&" in region:
                    region_list.append(region[i+1:])
    region_and_district_dict[elem] = region_list

print(f'все удачно загрузилось. Длина словаря: {len(region_and_district_dict)}')

"""
# выгрузка в файл ключ: значение словаря region_and_district_dict
with open('final_file.csv', 'w') as output_fin_file:
    for key, value in region_and_district_dict.items():
        print(key, value, sep=': ', file=output_fin_file)
"""


# проверка вхождений значений словаря в КЭ для выделения групп
#checking_region = input('Введите проверяемый субъект федерации: ')
try:
    for checking_region in region_and_district_dict.keys():
        if checking_region not in ['ненецкий', 'алтай']:
            for adress in all_ke_old:
                k = adress.find("&")
                if checking_region in adress:
                    checking_districts_list = region_and_district_dict[checking_region]
                    for i in range(len(checking_districts_list)):
                        if checking_districts_list[i] in adress:
                            checking_districts_list[i] = checking_districts_list[i] + adress[k:]
        else:
            print('не будет проверяться регион: ', checking_region)
            if checking_region == 'ненецкий':
                region_list.append('заполярный')
            if checking_region == 'алтай':
                region_list = ['кош-агачский', 'майминский', 'онгудайский', 'турочакский', 'улаганский', 'усть-канский', 'усть-коксинский', 'чемальский', 'чойский', 'шебалинский']
            region_and_district_dict[checking_region] = region_and_district_dict[checking_region]
except Exception as err:
    print(adress, checking_districts_list[i], type(err), err, sep=': ')

# выгрузка в файл для проверки
with open('logger.csv', 'w') as log_file:
    for key, value in region_and_district_dict.items():
        print(key, value, len(value), sep=';', file=log_file)


# checking_region_2 = 'ямало-ненецкий'
try:
    for checking_region_2 in region_and_district_dict.keys():
        if checking_region_2 not in ['алтай', 'ненецкий']:
            for adress_ind in range(len(new_ke[:50])):
                if checking_region_2 in new_ke[adress_ind]:
                    for district_and_wg in region_and_district_dict[checking_region_2]:
                        k = district_and_wg.find("&")
                        district = district_and_wg[:k]
                        wg = district_and_wg[k:]
                        if district in new_ke[adress_ind]:
                            new_ke[adress_ind] = new_ke[adress_ind] + wg
                            break                   
except Exception as err:
    print(adress, checking_region_2, type(err), err, sep=': ')

# выгрузка в файл для проверки
with open('logger2.csv', 'w') as log_file:
    print(len(value), *new_ke, sep='\n', file=log_file)

print('')
print('-' * 10)
print('Все успешно записалось, проверяйте')
print('-' * 10)
input()