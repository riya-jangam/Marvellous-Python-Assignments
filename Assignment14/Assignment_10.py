class Employee:
    def __init__(self, name, department, salary):
        self.name = name              # public
        self._department = department  # protected
        self.__salary = salary         # private

    def display_info(self):
        print("Name : "+self.name)
        print("Department : "+self._department)
        print("Salary : ",self.__salary)

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

def main ():
    emp = Employee("Riya", "Marketing", 50000)

    print("Public - Name:", emp.name)

    print("Protected - Department:", emp._department)

    print("Private - Salary:", emp.get_salary())

    emp.set_salary(55000)
    print("Updated Salary:", emp.get_salary())

    emp.display_info()

if __name__ == "__main__":
    main()
