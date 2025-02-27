# Base class for all beverages
class SweetGuessSo:
    def __init__(self):
        pass

    def addons(self, sugar=0, milk=0):
        self.sugar = sugar
        self.milk = milk

        # Check if condiments exceed the limit
        if sugar > 3 or milk > 3:
            raise TypeError("Too much, put it back!")

    def get_price(self):
        return self.base_price + (self.sugar * 0.10) + (self.milk * 0.15)

    # Method to return the name of the drink and its price
    def __str__(self):
        return f"{self.name} - ${self.get_price():.2f}"


# Subclass for Regular Coffee
class RegularCoffee(SweetGuessSo):
    def __init__(self, sugar=0, milk=0):
        self.name = "Regular Coffee"
        self.base_price = 1.10
        self.addons(sugar, milk)


# Subclass for Espresso
class Espresso(SweetGuessSo):
    def __init__(self, sugar=0, milk=0):
        self.name = "Espresso"
        self.base_price = 2.00
        self.addons(sugar, milk)


# Subclass for Cappuccino (no milk allowed as an extra)
class Cappuccino(SweetGuessSo):
    def __init__(self, sugar=0):
        self.name = "Cappuccino"
        self.base_price = 3.15
        self.addons(sugar, 0)  # No milk option for cap


class Farbucks:
    def __init__(self):
        self.start()

    def start(self):
        while True:
            print("Welcome! What would you like to drink?")
            print("")
            print("1. Regular Coffee ($1.10)")
            print("")
            print("2. Espresso ($2.00)")
            print("")
            print("3. Cappuccino ($3.15)")
            print("")


            while True:
                try:
                    choice = int(input("Choose a beverage by number (1-3): "))
                    print("")
                    if choice < 1 or choice > 3:
                        print("Invalid input. Please choose a beverage by number (1-3).")
                        print("")
                    else:
                        break  # Valid choice, exit loop
                except ValueError:
                    choice = input("Invalid input. Please enter a number: ")  # Re-asks immediately
                    print("")



                       
            # Condiments
            
            while True:
               try:
                  sugar = int(input("How many units of sugar would you like? "))
                  print("")

                  if sugar < 0 or sugar > 3:
                      print("Make sure you get no more than 3!")
                      print("")
                  else:
                      break
               except ValueError:
                    sugar = input("Invalid input. Please enter a number: ")  # Re-asks immediately
                    print("")
                
                
                   
            milk = 0  # Cappuccino can't have milk

            if choice == 1 or choice == 2:  # Only Regular Coffee and Espresso can have milk
                while True:
                    try:
                        milk = int(input("How many units of milk would you like? (0-3): "))
                        if 0 < milk <= 3:
                            break  # Valid input, exit loop
                        else:
                            print("\nYou must choose a milk amount, no more than 3 though!\n")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            

                    
        
            # Process the choice and brew the beverage
            if choice == 1 :
               beverage = RegularCoffee(sugar, milk)
            elif choice == 2:
               beverage = Espresso(sugar, milk)
            elif choice == 3:
               beverage = Cappuccino(sugar)
            else:
                print("Invalid choice. Please choose a valid beverage.")

            # Display final drink details & price
            print(f"\nAwesome! Your drink selection is a : {beverage.name}\n")
            if choice == 1 or choice == 2:
                print(f"Total Price: ${beverage.name} - ${beverage.get_price():.2f}")  # ✅ Ensures price calculation

            # Machine resets after each order
            print("\nThank you! Next customer...\n")



# Main function to run the vending machine
if __name__ == "__main__":
    Farbucks()
