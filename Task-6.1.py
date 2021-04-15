from pprint import pprint
class Employee:
    def __init__(self, name, birth_year, post):
        self.name, self.birth_year, self.post = name, birth_year, post
        self.key = (name, birth_year)
    def __repr__(self):
        return "Employee('%s',%s,'%s')" % (self.name, self.birth_year, self.post)

Ivan = Employee("Ivan", 1975, "project manager")
Olga = Employee("Olga", 1986, "analyst")
Aleksandr = Employee("Aleksandr", 1988, "programmer")
Vladimir = Employee("Vladimir", 1987, "designer")
Anna = Employee("Anna", 1990, "tester")

Team = {
    Ivan.key: Ivan,
    Olga.key: Olga,
    Aleksandr.key: Aleksandr,
    Vladimir.key: Vladimir,
    Anna.key: Anna
}

pprint(Team)
pprint(Team[Olga.key])