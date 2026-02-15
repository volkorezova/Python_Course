class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary,departament):
        Employee.__init__(name, salary)
        self.departament = departament

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(name, salary)
        self.programming_language = programming_language

class TeamLead (Manager, Developer):
    def __init__(self, name, salary, departament, programming_language, team_size):
        Employee.__init__(self, name, salary)
        self.departament = departament
        self.programming_language = programming_language
        self.team_size = team_size
