class JobException(Exception):
    pass

class TooManyEmployeeException(Exception):
    pass

class Person: # Класс "Человек"
    def __init__(self, a_name, a_surname, patronymic, gender, birth_year):
        self.a_name, self.a_surname, self.patronymic = a_name, a_surname, patronymic
        self.gender, self.birth_year = gender, birth_year
        self.key = (a_name, a_surname, patronymic, birth_year)
        self._has_job = 0
    def __repr__(self):
        return "Person('%s','%s','%s','%s',%s)" % (self.a_name, self.a_surname, self.patronymic, self.gender, self.birth_year)
    def post_resume(self): # разместить резюме
        pass
    def go_to_interview(self): # пойти на собеседование
        pass
    def get_job(self, company): #устроиться на работу
        if not self._has_job:
            company.to_hire_employee(self)
            self._has_job = 1
        else:
            raise JobException('у человека уже есть работа!')

class Employee(Person): # Класс "Сотрудник" - наследник класса "Человек"
    def __init__(self, ID_number, date_of_employment, position, department, a_name, a_surname, patronymic, gender, birth_year):
        super().__init__(a_name, a_surname, patronymic, gender, birth_year)
        self.ID_number, self.date_of_employment = ID_number, date_of_employment 
        self.position, self.department = position, department
        self.key = ID_number
    def __repr__(self):
        return "Employee(%s,'%s','%s','%s','%s')" % (self.ID_number, self.position, self.a_name, self.a_surname, self.patronymic)
    def to_work(self): # работать
        pass
    def get_salary(self): # получить зарплату
        pass
    def to_quit(self): # уволиться
        pass

class Company: # Класс "Фирма"
    def __init__(self, titel, field_of_activity):
        self.titel, self.field_of_activity = titel, field_of_activity
        self.key = titel
        self.__team = []
    def __repr__(self):
        return "Company('%s','%s')" % (self.titel, self.field_of_activity)
    def to_hire_employee(self, person): # нанять сотрудника
        if len(self.__team) < 1:
            self.__team += [person]
        else:
            raise TooManyEmployeeException('на вакантную позицию сотрудник уже принят!')
    def to_fire_employee(self): # уволить сотрудника
        pass
    def position_is_occupied(self): # на вакантную позицию принят сотрудник
        return len(self.__team) > 0
    def staff(self):
        return self.__team
        
Ivan = Employee(111, '01.03.2020', "project manager", 'IT-department','Ivan', 'Ivanov', 'Ivanovich', 'male', 1975)
Olga = Employee(222, '01.04.2020', "analyst", 'IT-department','Olga', 'Petrova', 'Nikolaevna', 'female', 1986)
Aleksandr = Employee(333, '01.05.2020', "programmer", 'IT-department','Aleksandr', 'Aleksandrov', 'Aleksandrovich', 'male', 1988)
Vladimir = Employee(444, '01.06.2020', "designer", 'IT-department','Vladimir', 'Vladimirov', 'Vladimirovich', 'male', 1987)
Anna = Employee(555, '01.07.2020', "tester", 'IT-department','Anna', 'Smirnova', 'Petrovna', 'female', 1990)

a_company = Company('IBS', 'IT')
b_company = Company('Apple', 'IT')

Team = [Ivan, Olga, Aleksandr, Vladimir, Anna]

print('Введите имя сотрудника:')
n = str(input())
print('Введите минимальный год рождения сотрудника:')
y = int(input())
for item in Team:
    if item.a_name == n and item.birth_year > y:
        x = item.__repr__()
        print(x)

import unittest
class TestPerson(unittest.TestCase):
    def test_reserch(self):
        self.assertEqual(item.__repr__(), x)

if __name__ == '__main__':
    unittest.main()
