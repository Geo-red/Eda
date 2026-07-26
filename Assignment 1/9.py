class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.salary)

    def increase_salary(self,p):
        self.salary=self.salary+(self.salary*p/100)

emp=Employee(101,"John",50000)
emp.display()
emp.increase_salary(10)
emp.display()
