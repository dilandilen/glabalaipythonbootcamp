import csv
from datetime import datetime
from classes import  TurkPizza,ClassicPizza,Decorator,Corn,Goat_cheese,MargheritaPizza,DominosPizza,Meat,Mushrooms,Olives,Onions
def welcome():
    print("Welcome to Pizza Place!\n")
    print("Menu:")

def goodbye():
   print("Your order has been placed successfully. Thank you for choosing our restaurant!")
def print_menu():
    with open('menu.txt', 'r') as file:
     data = file.read()
     print(data)

def main():
    # Print the menu
    welcome()
    print_menu()
    # Get user's pizza selection
    while True:
        try:
            pizza_choice = int(input("Please enter the number of your pizza selection: "))
            if pizza_choice < 1 or pizza_choice > 4:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # Get user's sauce selection
    while True:
        try:
            sauce_choice = int(input("Please enter the number of your sauce selection: "))
            if sauce_choice < 11 or sauce_choice > 16:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 11 and 16.")

    # Create the pizza object based on user's selection
    if pizza_choice == 1:
        pizza = ClassicPizza()
        pizzaprint = "classic pizza"
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
        pizzaprint= "margherita pizza"
    elif pizza_choice == 3:
        pizza = TurkPizza()
        pizzaprint=" turk pizza"
    else:
        pizza = DominosPizza()
        pizzaprint="dominos pizza"

    # Add sauce to the pizza based on user's selection
    if sauce_choice == 11:
        pizza = Olives(pizza)
        sauceprint="olives"
    elif sauce_choice == 12:
        pizza = Mushrooms(pizza)
        sauceprint= "Mushrooms"
    elif sauce_choice == 13:
        pizza = Goat_cheese(pizza)
        sauceprint="goat cheese"
    elif sauce_choice == 14:
        pizza = Meat(pizza)
        sauceprint=" meat"
    elif sauce_choice == 15:
        pizza = Onions(pizza)
        sauceprint="onions"
    else:
        pizza = Corn(pizza)
        sauceprint="corn"

    # Calculate total price
    total_price = pizza.get_cost()
    print(' The pizza you choose:{} \n The sauce you want to add your pizza:{}\n and total cost is: {}'.format(pizzaprint,sauceprint,total_price))
 
    # Get user information
    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    cc_number = input("Please enter your credit card number: ")
    cc_password = input("Please enter your credit card password: ")

    # Write order information to the database
    with open("Orders_Database.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, id_number, cc_number, cc_password, pizza.get_description(), total_price, datetime.now()])

    goodbye()  

if __name__ == "__main__":
    main()