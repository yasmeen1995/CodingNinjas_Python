
# parent class
class Person():
    # write your code logic !!
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display(self):
        print(self.name, " ", self.age)


# child class
class Student(Person):
    # write your code logic !!
    def __init__(self, name, age, dob) -> None:
        super().__init__(name, age)
        self.dob = dob

    def displayInfo(self):
        print(self.name, " ", self.age, " ", self.dob)


    
obj = Student("Rahul", 23, "16-03-2000")
obj.display()
obj.displayInfo()



# Problem statement
# Write the Python code that defines a parent class Person and a child class Student. The Person class has attributes for a person's name and age, and a display method to print these attributes. The Student class inherits from the Person class and adds a new attribute for the student's date of birth (dob) and a displayInfo method to print all three attributes (name, age, and date of birth).

# Output :
# Rahul 23
# Rahul 23 16-03-2000

