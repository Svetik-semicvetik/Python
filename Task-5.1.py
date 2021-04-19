Team = {
    'Ivan': {'Дата рождения':1975, 'Должность':'project manager'}, 
    'Olga': {'Дата рождения':1986, 'Должность':'analyst'},
    'Aleksandr': {'Дата рождения':1988, 'Должность':'programmer'},
    'Vladimir': {'Дата рождения':1987, 'Должность':'designer'},
    'Anna': {'Дата рождения':1990, 'Должность':'tester'}
}

print('Введите должность сотрудника:')
s = input()
def search(s):
    for a, b in Team.items():
        for a1, b1 in b.items():
            if a1=='Должность' and b1 == s.lower():
                return print('Сотрудник:',a,b)
search(s)

Team = [
    ['Ivan', 1975, 'project manager'],
    ['Olga', 1986, 'analyst'],
    ['Aleksandr', 1988, 'programmer'],
    ['Vladimir', 1987, 'designer'],
    ['Anna', 1990, 'tester']
]
print('Введите имя сотрудника:')
m = input()
def search(m):
    for i in range(len(Team)):
        for j in range(len(Team[i])):
            if Team[i][j]==m:
                return print(Team[i])
search(m)