class My_class:
    def __init__(self, f_name, s_name, sir_name):
        self.f_name = f_name
        self.s_name = s_name
        self.sir_name = sir_name

    def helo(self):
        print("helo world")


person = My_class("bill", "clinton", "ogot")
print(person.f_name)
print(person.helo())

class Employee:
   'Common base class for all employees'
   empCount = 0
   # this varriable can not be assesed outide the class
   __total_number = 20

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print( "Total Employee %d" % Employee.empCount)
