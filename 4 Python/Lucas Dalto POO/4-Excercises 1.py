class Student:
    def __init__(self, name, age, grade, high_school):
        self.Name = name
        self.Age = age
        self.Grade = grade
        self.High_school = high_school
        
    def study(self):
        print("Estudiando...")
        

Name = input("What is your name: ")
Age = input("What is your age: ")
Grade = input("What is your grade: ")
High_school = input("What is your high school: ")

student = Student(Name, Age, Grade, High_school)

print(f"""
      Student's information \n \n
      
      Nombre: {student.Name} \n
      Edad: {student.Age} \n
      Grado: {student.Grade} \n
      Colegio: {student.High_school} \n
      """)

while True:
    Estudiar = input("Type 'estudiar' to study: ")
    if Estudiar.lower() == "estudiar":
        student.study()
        break