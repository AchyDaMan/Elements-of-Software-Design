# Base Employee Class
class Employee:
    # Initialized
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
                setattr(self, key, value)

    # Formatted to do format "attribute: value"
    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)


# An Employee with benefits
class PermanentEmployee(Employee):
    def __init__(self, **kwargs):
        self.benefits = []
        super().__init__(**kwargs)

    def cal_salary(self):
        benefit = getattr(self, 'benefits', None)
        salary = float(getattr(self, 'salary', 0))
        if benefit == ['health_insurance']:
            return salary * 0.9
        elif benefit == ['retirement']:
            return salary * 0.8
        elif benefit == ['retirement', 'health_insurance']:
            return salary * 0.7
        return salary


    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)

############################################################
############################################################
############################################################

class Manager(Employee):
    def __init__(self, **kwargs):
        self.bonus = 0
        super().__init__(**kwargs)
    
    def cal_salary(self):
        bonus = float(getattr(self, 'bonus', 0))
        salary = float(getattr(self, 'salary', 0))
        return salary + bonus

    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)


############################################################
############################################################
############################################################
class TemporaryEmployee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
    def cal_salary(self):
        salary = getattr(self, 'salary', 0)
        hours = getattr(self, 'hours', 0)
        return salary * hours

    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)

    
############################################################
############################################################
############################################################


class Consultant(TemporaryEmployee):
    def __init__(self, **kwargs):
        self.travel = 0
        super().__init__(**kwargs)

    def cal_salary(self):
        travel = getattr(self, 'travel', 0) * 1000
        return super().cal_salary() + travel

    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)
############################################################
############################################################
############################################################


class ConsultantManager(Consultant, Manager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cal_salary(self):
        salary = getattr(self, 'salary', 0)
        hours = getattr(self, 'hours', 0)
        bonus = getattr(self, 'bonus', 0)
        travel = getattr(self, 'travel', 0)
        return salary*hours + travel*1000 + bonus
 
    def __str__(self):
        attributes = [f"{key}: {value}" for key, value in self.__dict__.items()]
        return "\n".join(attributes)


############################################################
############################################################
############################################################





###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    """
    A Main function to create some example objects of our classes. 
    """

    chris = Employee(name="Chris", identifier="UT1")
    print(chris, "\n")

    emma = PermanentEmployee(name="Emma", identifier="UT2",
                              salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = TemporaryEmployee(name="Sam", identifier="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", identifier="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", identifier="UT5",
                        salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = ConsultantManager(name="Matt", identifier="UT6",
                              salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")

if __name__ == "__main__":
  main()



