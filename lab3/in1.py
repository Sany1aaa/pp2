class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("Saniya", "Mashrap")
x.printname()

#student class inherits person class
class Student(Person):
  pass #pass to change nothing 

x = Student("Mike", "Olsen")
x.printname()