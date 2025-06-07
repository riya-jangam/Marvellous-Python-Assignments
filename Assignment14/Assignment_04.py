class Student:
    School_Name = "CISK"

    def __init__(self, A, B):
        self.name = A
        self.roll_no = B

    def display(self):
        print("Name : ",self.name,"Roll No : ",self.roll_no,"School : ", Student.School_Name)


def main():
    obj1 = Student("Riya", 101)
    obj2 = Student("Akhilesh", 102)

    obj1.display()
    obj2.display()

    Student.School_Name = "KHS School"

    print("Change school name")

    obj1.display()
    obj2.display()

if __name__ == "__main__":
    main()
