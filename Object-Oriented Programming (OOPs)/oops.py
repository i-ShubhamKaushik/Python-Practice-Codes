# 1. Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class programmer:

    company = "MicroSoft"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

employee1= programmer("Shubham", 123456789, "CEO")
print(employee1.company, employee1.name, employee1.salary, employee1.position)

employee2= programmer("Rohan", 12345678, "MD")     
print(employee2.company, employee2.name, employee2.salary, employee2.position)



# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 

class calculator:
    def __init__(self, number):
        self.number= number

    def square(self):
            print(f"Square of {self.number} is : {self.number**2}")

    def cube(self):
            print(f"Cube of {self.number} is : {self.number**3}")

    def sqroot(self):
            print(f"Sq. root of {self.number} is : {self.number**0.5}")

calc1= calculator(12)
calc1.square()
calc1.cube()
calc1.sqroot()



# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

class testing_a:
    a = 1

object= testing_a()
object.a= 0

print(object.a)
print(testing_a.a)           #No, it will only overwrite the class attribute because instance attritute is present!



# 4. Add a static method in problem 2, to greet the user with hello. 

class calculator2:
    def __init__(self, number):
        self.number= number
    
    def square(self):
        print(f"Square of {self.number} is : {self.number**2}")

    def cube(self):
        print(f"Cube of {self.number} is : {self.number**3}")
    
    def sqroot(self):
        print(f"Sq. root of {self.number} is : {self.number**0.5}")

    @staticmethod
    def greet():
        print("Hello")

calc2= calculator2(34)
calc2.greet()
calc2.square()
calc2.cube()
calc2.sqroot()



# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo= trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}.")

    def getStatus(self):
        print(f"Train number: {self.trainNo} has {randint(1,99)} available seats.")

    def fare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(111,999)}rs.")


myTrain= train(12345)
myTrain.book("Delhi", "Shimla")
myTrain.getStatus()
myTrain.fare("Delhi", "Shimla")



# 6. Can you change the self-parameter inside a class to something else (say “Naruto”). 
# Try changing self to “slf” or “Naruto” and see the effects.

class check:
    def __init__(slf, name):
        slf.name= name

person1= check("Shubham")
print(person1.name)

class check:
    def __init__(naruto, name):
        naruto.name= name

person1= check("Naruto")
print(person1.name)                    #Nothing will happen! Code will still run the same way.