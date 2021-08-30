class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, age):
      self.name = name
      self.salary = salary
      self.age = age # Add an 'age' attribute.
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, ",age: ", self.age)
 
#"This would create first object of Employee class"
emp1 = Employee("Zara", 2000,10)
#"This would create second object of Employee class"
emp2 = Employee("Manni", 5000,12)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)
 
