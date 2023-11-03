"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self,name,salary,contract,hourly, hours,fixed,comissions,bonus):
        self.name = name
        self.salary = salary
        self.contract = contract
        self.hourly = hourly
        self.hours = hours
        self.fixed = fixed
        self.comissions = comissions
        self.bonus = bonus


    def get_pay(self):
        if(self.contract == False):
            if(self.fixed == True):
                return self.salary + self.bonus
            else:
                return (self.salary + (self.comissions * self.bonus))
        else:
            if(self.hourly == False):
                return self.salary
            else:
                return (self.salary * self.hours)

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,True,False,0,False,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',25,True,True,100,False,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,True,False,0,False,4,200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
