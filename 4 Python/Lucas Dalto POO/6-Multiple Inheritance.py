class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Employee:
    def __init__(self, company, salary):
        self.company = company
        self.salary = salary

    def introduce(self):
        print(f"I work at {self.company}, and my salary is ${self.salary}.")


class Student:
    def __init__(self, school, grade):
        self.school = school
        self.grade = grade

    def study(self):
        print(f"I study at {self.school}, and I'm in grade {self.grade}.")


class WorkingStudent(Person, Employee, Student):
    def __init__(self, name, age, company, salary, school, grade):
        Person.__init__(self, name, age)
        Employee.__init__(self, company, salary)
        Student.__init__(self, school, grade)


# Create an instance of the WorkingStudent class
working_student1 = WorkingStudent("John", 25, "ABC Company", 5000, "XYZ School", "12th")

# Call the methods from the parent classes
working_student1.greet()
working_student1.introduce()
working_student1.study()




print("################################")


class Student:
    def __init__(self, name, age, school, grade):
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

    def study(self):
        print(f"I study at {self.school}, and I'm in grade {self.grade}.")


class Artist:
    def __init__(self, name, age, art_style):
        self.name = name
        self.age = age
        self.art_style = art_style

    def create_art(self):
        print(f"I'm an artist, and I create art in {self.art_style} style.")


class Employee:
    def __init__(self, name, age, company, salary):
        self.name = name
        self.age = age
        self.company = company
        self.salary = salary

    def introduce(self):
        print(f"I work at {self.company}, and my salary is ${self.salary}.")


class Manager(Employee):
    def __init__(self, name, age, company, salary, department):
        super().__init__(name, age, company, salary)
        self.department = department

    def introduce(self):
        super().introduce()
        print(f"I'm a manager, and I oversee the {self.department} department.")


class WorkingArtist(Student, Artist, Employee):
    def __init__(self, name, age, school, grade, art_style, company, salary):
        super().__init__(name, age, school, grade)
        Artist.__init__(self, name, age, art_style)
        Employee.__init__(self, name, age, company, salary)


# Create an instance of the WorkingArtist class
working_artist1 = WorkingArtist("Alice", 22, "XYZ School", "12th", "Abstract", "ABC Company", 4000)

# Call the methods from the parent classes
working_artist1.study()
working_artist1.create_art()
working_artist1.introduce()





print("################################")

#Third Example
#saber si es una subclase
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# Comprobar si Dog es una subclase de Animal y almacenar el resultado en una variable
is_dog_subclass = issubclass(Dog, Animal)

# Comprobar si Cat es una subclase de Animal y almacenar el resultado en una variable
is_cat_subclass = issubclass(Animal, Cat)

# Imprimir el resultado
print("Dog is a subclass of Animal:", is_dog_subclass)
print("Cat is a subclass of Animal:", is_cat_subclass)



print("################################")

#Fourth Example
#Saber si es una instancia

class Animal:
    pass

class Dog(Animal):
    pass

# Crear una instancia de Dog
dog_instance = Dog()

# Verificar si dog_instance es una instancia de Dog o Animal
print(isinstance(dog_instance, Dog))  # True
print(isinstance(dog_instance, Animal))  # True


