class Student:
    def __init__(self, name, age, grade, high_school):
        self.Name = name
        self.Age = age
        self.Grade = grade
        self.High_school = high_school
        
student1 = Student("Jose", 17, "Undecimo", "C.T.P ATENAS")

print(f"El es {student1.Name}, tiene {student1.Age} y esta en {student1.Grade} en el colegio del {student1.High_school}")