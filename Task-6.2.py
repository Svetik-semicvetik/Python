from pprint import pprint
class Employee:
    def __init__(self, name, birth_year, post):
        self.name, self.birth_year, self.post = name, birth_year, post
        self.key = (name, birth_year)
    def __repr__(self):
        return "Employee('%s',%s,'%s')" % (self.name, self.birth_year, self.post)
    def get_name(self):
        return self.name
    def get_birth_year(self):
        return self.birth_year
    def get_post(self):
        return self.post

Ivan = Employee("Ivan", 1975, "project manager")
Olga = Employee("Olga", 1986, "analyst")
Aleksandr = Employee("Aleksandr", 1988, "programmer")
Vladimir = Employee("Vladimir", 1987, "designer")
Anna = Employee("Anna", 1990, "tester")

Team = [Ivan, Olga, Aleksandr, Vladimir, Anna]

print('Введите имя сотрудника:')
n = str(input())
print('Введите минимальный год рождения сотрудника:')
y = int(input())
for item in Team:
    if item.name == n and item.birth_year > y:
        print(item.__repr__())
