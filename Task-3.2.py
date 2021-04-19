Team = {
    'Ivan': {'Дата рождения':1975, 'Должность':'project manager'}, 
    'Olga': {'Дата рождения':1986, 'Должность':'analyst'},
    'Aleksandr': {'Дата рождения':1988, 'Должность':'programmer'},
    'Vladimir': {'Дата рождения':1987, 'Должность':'designer'},
    'Anna': {'Дата рождения':1990, 'Должность':'tester'}
}
print('Введите должность сотрудника:')
d = input()
for a, b in Team.items():
    for a1, b1 in b.items():
        if a1=='Должность' and b1==d:
            print('Сотрудник:',a,b)
