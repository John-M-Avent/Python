## Python Assignment Five: Updated for Homework 2
# John M. Avent 
# ENG 101-06 
# 4/18/2017 
# 
# Dictionary Setup
#
stock = {                   # Sets up a dictionary for the items and the amount in stock of each.
    "tomato soup": 20,
    "cheese": 10,
    "bread": 3,
    "milk": 1,
    "butter": 7,
    "coffee": 8,
    "ice cream": 5,
    "orange juice":  12,
    "bacon": 2,
    "tortilla chips":  4,
    "ramen":  20
    }
prices = {                  # Sets up a dictionary for the items and their costs. 
    "tomato soup": 1.85,
    "cheese": 3.99,
    "bread": 2.50,
    "milk": 3.59,
    "butter": 1.99,
    "coffee": 5.99,
    "ice cream": 2.99,
    "orange juice":  2.50,
    "bacon": 5.49,
    "tortilla chips":  3.99,
    "ramen":  0.99
    }
# 
# Sets Up The grocery_cost Function 
# 
def grocery_cost(food,count):                                       # Defines function for grocery_cost. 
    """Finds the cost of each grocery item in the list entered"""   # Describes the function. 
    Cost = 0                                                        # Sets up cost.
    for item, number in zip(food, count):                           # For item in the list food and number in the list count...
        price = prices[item]                                        # Price equals price of that item listed in dictinary prices.
        Amount = number                                             # Amount equals the number desired for purchase. 
        if stock[item] >= int(Amount):                              # If there are those items in stock...
            Cost = Cost + (price * int(Amount) )                    # Adds the sold items from stock.
            stock[item] -= int (Amount)
        else:                                                       # Else...
            print ("There is not that many of item " + item + " in stock.") # Informs the user that there aren't as many of the item as they want. 
            Answer = input ("There is a quantity of " + str(stock[item]) + " in stock. Would you like to buy that many instead? Type 'yes' or 'no': ")  # Queries the user to see if they'd like to buy how many there are in stock. 
            Answer = Answer.lower()                                 # Makes the answer lowercase. 
            if Answer == 'yes':                                     # If the answer is yes...
                Cost = Cost + (price * stock[item] )                # Adds the cost. 
                stock[item] = 0                                     # Removes sold items from stock dictionary. 
    print("The cost is $" + str(Cost) + ".")                        # Prints the overall price. 
# 
# Sets Up the stock_check Function 
# 
def stock_check(stock_list):                                        # Defines function for stock_check. 
    """Find the amount in stock for each item in the list entered"""# Describes the function. 
    for item in stock_list:                                         # For item in list stock_list...
        if stock[item] < 5:                                         # If there is less than 5 of that item in stock...
            print(item.title() + " is running low.")                # Prints that the item is running out. 
# 

