with open('perepis.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

people = []

for line in lines:
    line = line.strip()
    if line:
        parts = line.split()
        if len(parts) >= 4:
            date_parts = parts[3].split('.')
            if len(date_parts) == 3:
                year = int(date_parts[2])

                person = {
                    'фамилия': parts[0],
                    'имя': parts[1],
                    'отчество': parts[2],
                    'год_рождения': year
                }
                people.append(person)

print('а)')

count_old = 0
old_people = []

for person in people:
    if person['год_рождения'] < 1978:
        print(person['фамилия'])
        old_people.append(person)
        count_old += 1

print('')
print('Всего таких людей: ' + str(count_old))
print('')

print('б)')

print('Введите диапазон годов рождения:')
start_year = int(input('От года: '))
end_year = int(input('До года: '))

if start_year > end_year:
    start_year, end_year = end_year, start_year
    print('')
    print('Диапазон скорректирован: ' + str(start_year) + '-' + str(end_year))

print('')
print('Люди, родившиеся в ' + str(start_year) + '-' + str(end_year) + ' годах:')

found_count = 0

for person in people:
    if start_year <= person['год_рождения'] <= end_year:
        print(person['фамилия'] + ' ' + person['имя'] + ' ' + person['отчество'] + ' - ' + str(person['год_рождения']) + ' г.р.')
        found_count += 1

if found_count == 0:
    print('Людей не найдено.')
else:
    print('')
    print('Найдено: ' + str(found_count) + ' человек')