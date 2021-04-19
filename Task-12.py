class Person: # Класс "Человек"
    def __init__(self, name, surname, patronymic, gender, birth_year):
        self.name, self.surname, self.patronymic = name, surname, patronymic
        self.gender, self.birth_year = gender, birth_year
        self.key = (name, surname, patronymic, birth_year)
    def __repr__(self):
        return "Person('%s','%s','%s','%s',%s)" % (self.name, self.surname, self.patronymic, self.gender, self.birth_year)
    def post_resume: # разместить резюме
        pass
    def go_to_interview: # пойти на собеседование
        pass
    def get_job: #устроиться на работу
        pass
    
class Employee(Person): # Класс "Сотрудник" - наследник класса "Человек"
    def __init__(self, ID_number, date_of_employment, position, department):
        super().__init__(name, surname, patronymic, gender, birth_year)
        self.ID_number, self.date_of_employment = ID_number, date_of_employment 
        self.position, self.department = position, department
        self.key = ID_number
    def __repr__(self):
        return "Employee(%s,'%s','%s','%s')" % (self.ID_number, self.date_of_employment, self.position, self.department)
    def to_work: # работать
        pass
    def get_salary: # получить зарплату
        pass
    def to_quit: # уволиться
        pass
