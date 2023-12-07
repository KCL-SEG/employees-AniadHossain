class Employee:
    def __init__(self, name):
        self.name = name
        self.contract_type = None
        self.salary = 0
        self.hourly_wage = 0
        self.hours_worked = 0
        self.bonus = 0
        self.commission_per_contract = 0
        self.contracts_landed = 0

    def set_monthly_salary(self, salary):
        self.contract_type = 'salary'
        self.salary = salary

    def set_hourly_rate(self, hourly_wage, hours_worked):
        self.contract_type = 'hourly'
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def set_bonus(self, bonus):
        self.bonus = bonus

    def set_contract_commission(self, commission_per_contract, contracts_landed):
        self.commission_per_contract = commission_per_contract
        self.contracts_landed = contracts_landed

    def get_contract_pay(self):
        if self.contract_type == 'salary':
            return self.salary
        elif self.contract_type == 'hourly':
            return self.hourly_wage * self.hours_worked
        else:
            return 0

    def get_commission(self):
        if self.commission_per_contract and self.contracts_landed:
            return self.commission_per_contract * self.contracts_landed
        else:
            return 0

    def get_pay(self):
        return self.get_contract_pay() + self.get_commission() + self.bonus  # Include bonus in total pay calculation

    def __str__(self):
        explanation = f"{self.name} works "
        
        if self.contract_type == 'salary':
            explanation += f"on a monthly salary of {self.salary}"
        elif self.contract_type == 'hourly':
            explanation += f"on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour"
        
        if self.bonus:
            explanation += f" and receives a bonus commission of {self.bonus}"
        
        if self.commission_per_contract and self.contracts_landed:
            explanation += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"
        
        explanation += f". Their total pay is {self.get_pay()}."
        return explanation


# Creating Employee objects
billie = Employee("Billie")
billie.set_monthly_salary(4000)

charlie = Employee("Charlie")
charlie.set_hourly_rate(25, 100)

renee = Employee("Renee")
renee.set_monthly_salary(3000)
renee.set_contract_commission(200, 4)

jan = Employee("Jan")
jan.set_hourly_rate(25, 150)
jan.set_contract_commission(220, 3)

robbie = Employee("Robbie")
robbie.set_monthly_salary(2000)
robbie.set_bonus(1500)

ariel = Employee("Ariel")
ariel.set_hourly_rate(30, 120)
ariel.set_bonus(600)
