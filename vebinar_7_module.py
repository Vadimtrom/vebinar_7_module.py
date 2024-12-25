import re

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'ФИО: {self.name}, Должность: {self.position}, Оклад: {self.salary}'

class Manager(Employee):
    def __init__(self, name, position, salary, team_size):
        super().__init__(name, position, salary)
        self.team_size = team_size

    def __str__(self):
        return f'{super().__str__()}, Размер команды: {self_team_size}'

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employee = employee
        pattern = re.compile(re.escape(employee))
        with open('emp_list', 'r+', encoding='utf-8') as name:
            lines = name.readlines()
            name.seek(0)
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    name.write(line)
                name.truncate()

    def list_employees(self):
        with open('emp_list', 'r', encoding='utf-8') as file:
            for line in file:
                print(line)

        for emp in self.employees:
            print(emp)

    def save_to_file(self, filename):
        with open(filename, 'a', encoding='utf-8') as file:
            for emp in self.employees:
                if isinstance(emp, Manager):
                    file.write(f'ФИО: {emp.name}, Должность: {emp.position}, Оклад: {emp.salary}, Размер команды: {emp.team_size}\n')
                else:
                    file.write(f'ФИО: {emp.name}, Должность: {emp.position}, Оклад: {emp.salary}\n')


company = Company()

while True:
    print('Добро пожаловать в программу Сотрудник 2.1')
    print('В этой программе доступны команды: \n'
          'add - добавление сотрудников\n'
          'list - вывод списка всех сотрудников\n'
          'save - сохранение списка сотрудников в отдельный файл\n'
          'exit - выход из программы')

    action = input('Выберите действие (add/list/save/exit/remove): ')
    if action == 'add':
        emp_type = input('Введите тип сотрудника (разработчик / тимлид): ')
        name = input('Введите ФИО сотрудника: ')
        position = input('Введите должность сотрудника: ')
        salary = input('Укажите оклад сотрудника: ')


        if emp_type == 'тимлид':
            team_size = int(input('Введите кол-во человек в команде: '))
            company.add_employee(Manager(name, position, salary, team_size))
            print('Сотрудник внесен в список')
        else:
            company.add_employee(Employee(name, position, salary))
            print('Сотрудник внесен в список')

    elif action == 'list':
        check_list = company.list_employees()
        if check_list == None:
            print('Список сотрудников пуст')
        else:
            company.list_employees()



    elif action == 'save':
        filename = input('Введите имя файла для сохранения: ')
        company.save_to_file(filename)
        print(f'Файл {filename} сохранен')

    elif action == 'exit':
        print('Cеанс завершен')
        break

    elif action == 'remove':
        company.remove_employee(employee=input('Введите имя удаляемого сотрудника: '))

    else:
        print('Некорректный ввод, попробуйте ещё раз')

