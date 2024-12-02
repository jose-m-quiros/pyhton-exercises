#By simply putting ("the parent class in parentheses"), the child class can access the attributes and methods of the parent class.
#Con solo poner ("La clase padre entre parectecis") la clase hija puede acceder a los atributos y métodos de la clase padre.

#Example

# class ClasePadre:
#      #Definición de atributos y métodos de la clase padre

# class ClaseHija(ClasePadre):
#      #Definición de atributos y métodos adicionales para la clase hija



#First Example
class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, nationality, course):
        # Call the constructor of the parent class (Person)
        super().__init__(name, age, nationality)
        self.course = course

    def introduce(self):
        print(f"Hello, I'm {self.name}, I'm {self.age} years old, I'm from {self.nationality}, and I'm in the {self.course} course.")


# Create an instance of the Student class
student1 = Student("Jose", 17, "CR", "Dalto")

# Call the method of the parent class (Person) from the Student class
student1.greet()

# Call the method of the Student class
student1.introduce()





print("################################")


#Second Example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Employee(Person):
    def __init__(self, name, age, company, salary):
        # Call the constructor of the parent class (Person)
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def introduce(self):
        print(f"I'm {self.name}, I'm {self.age} years old, I work at {self.company}, and my salary is ${self.salary}.")


class Student(Person):
    def __init__(self, name, age, school, grade):
        # Call the constructor of the parent class (Person)
        super().__init__(name, age)
        self.school = school
        self.grade = grade

    def study(self):
        print(f"I'm {self.name}, I'm {self.age} years old, I study at {self.school}, and I'm in grade {self.grade}.")


# Create an instance of the Employee class
employee1 = Employee("John", 30, "ABC Company", 5000)

# Call the method of the parent class (Person) from the Employee class
employee1.greet()

# Call the method of the Employee class
employee1.introduce()

# Create an instance of the Student class
student1 = Student("Alice", 18, "XYZ School", "12th")

# Call the method of the parent class (Person) from the Student class
student1.greet()

# Call the method of the Student class
student1.study()
