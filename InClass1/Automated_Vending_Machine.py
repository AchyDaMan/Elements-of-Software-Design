"""
Achintya Yedavalli
CS 313E
In-Class Assignment 1: Automated Coffee vending machine
"""
class Coffee:
    def __init__(self, price, milk, sugar):
        self.price = price
        self.milk = milk
        self.sugar = sugar
    def __str__(self):
        return f"Coffee. Contains {self.milk.get_units()} milk, {self.sugar.get_units()} sugar, and costs ${self.get_price():.2f}"
    def get_price(self):
        return self.price + self.milk.get_price() + self.sugar.get_price()
    
class Espresso(Coffee):
    def __init__(self, price, milk, sugar):
        super().__init__(price * 1.2, milk, sugar)
    def __str__(self):
        return f"Espresso. Contains {self.milk.get_units()} milk, {self.sugar.get_units()} sugar, and costs ${self.get_price():.2f}"
    def get_price(self):
        return super().get_price()

class Cappuccino(Espresso):
    def __init__(self, price, sugar):
        super().__init__(price * 1.15, 0, sugar)

    def __str__(self):
        return f"Cappuccino. Contains {self.sugar.get_units()} sugar, and costs ${self.get_price():.2f}"
    
    def get_price(self):
        return self.price + self.sugar.get_price()
    
class Milk:
    def __init__(self, units, unit_price=.15):
        self.units = units
        self.unit_price = unit_price
    def get_price(self):
        return self.unit_price * self.units
    def get_units(self):
        return self.units
    
class Sugar:
    def __init__(self, units, unit_price=.10):
        self.units = units
        self.unit_price = unit_price
    def get_price(self):
        return self.unit_price * self.units
    def get_units(self):
        return self.units
    
class VendingMachine:
    def run_program(self):
        coffee_cost = 1.10
        print('Hello and Welcome to the Automated Coffee Vending Machine (ACVM)! Let\'s get started.')
        print('######################################################################################')
        while(True):
            print('What type of coffee do you want? Coffee (1), Espresso (2), or Cappuccino (3)?')
            choice = -1
            while choice > 3 or choice <= 0:
                choice = int(input())
                if choice > 3 or choice <= 0:
                    print('Invalid. Try again.')

            total_units = 4
            while total_units > 3:
                total_units = 0
                milk_units = 0
                if choice != 3:
                    print('How much milk do you want? Between 0 and 3. Note that you share between milk and sugar.')
                    milk_units = int(input())
                
                print('How much sugar do you want? Between 0 and 3.')
                sugar_units = int(input())
                total_units = sugar_units + milk_units
                if total_units > 3:
                    print('Invalid, Choose only 3 units of condiments')
            
            if choice == 1:
                beverage = Coffee(coffee_cost, Milk(milk_units), Sugar(sugar_units))
            elif choice == 2:
                beverage = Espresso(coffee_cost, Milk(milk_units), Sugar(sugar_units))
            else:
                beverage = Cappuccino(coffee_cost, Sugar(sugar_units))

            print('Got it! Now dispensing', beverage, '\n\n')

def main():
    VendingMachine().run_program()
    
main()