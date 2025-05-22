# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class Manager(Employee):
#
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
# class Developer(Employee):
#
#     def __init__(self, name, salary, programing_language):
#         super().__init__(name, salary)
#         self.programing_language = programing_language
#
# class TeamLead(Manager, Developer):
#
#     def __init__(self, name, salary, department, programing_language, team_size):
#         Employee.__init__(self, name, salary)
#         self.department = department
#         self.programing_language = programing_language
#         self.team_size = team_size
#
#
# Den = TeamLead(name="Den", salary=1000, department="AI", programing_language="C++", team_size=12)


class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary
        super().__init__(**kwargs)

class Manager(Employee):
    def __init__(self, department, **kwargs):
        self.department = department
        super().__init__(**kwargs)

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        self.programming_language = programming_language
        super().__init__(**kwargs)

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        self.team_size = team_size
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )


d = {"one": 1, "two": 2, "three": 3}
