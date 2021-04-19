Team = [
    ['Ivan', 1975, 'project manager'],
    ['Olga', 1986, 'analyst'],
    ['Aleksandr', 1988, 'programmer'],
    ['Vladimir', 1987, 'designer'],
    ['Anna', 1990, 'tester']
]
#найдем самого молодого сотрудника:
years = ([item[1] for item in Team])
x = years[0]
for i in years:
    if x < i:
        x = i
for i in range(len(Team)):
    for j in range(len(Team[i])):
        if Team[i][j]==x:
            print(Team[i])

Team = {
    'Ivan': {'Дата рождения':1975, 'Должность':'project manager'}, 
    'Olga': {'Дата рождения':1986, 'Должность':'analyst'},
    'Aleksandr': {'Дата рождения':1988, 'Должность':'programmer'},
    'Vladimir': {'Дата рождения':1987, 'Должность':'designer'},
    'Anna': {'Дата рождения':1990, 'Должность':'tester'}
}
#найдем самого старого сотрудника:
for a, b in Team.items():
    for a0, b0 in b.items():
        if a0=='Дата рождения' and b0==1975:
            print(a,b)
