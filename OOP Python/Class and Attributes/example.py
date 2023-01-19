class Student():

    planet = "Earth" #CLASS OBJECT ATTRIBUTE

    def __init__(self, name, gpa):
        self.name = name #ATTRIBUTES
        self.gpa = gpa
    

stu1 = Student("Jose", 3.5)
stu2 = Student(name="Mimi", gpa=4.0)

print(stu1.name)
print(stu1.planet)
print(stu2)