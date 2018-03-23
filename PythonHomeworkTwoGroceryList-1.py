## Python Homework One: Grocery List
# John M. Avent 
# ENG 101-06 
# 4/18/2017 
# 
# Setup 
#
from grocery import stock                           # Imports dictionary stock from file grocery. 
from grocery import grocery_cost                    # Imports function grocery_cost from file grocery. 
from grocery import stock_check                     # Imports funcion stock_check from file grocery. 
StockItems = stock.keys()                           # Makes a list of the keys in the stock dictionary. 
StockList = list()                                  # Makes a blank list. 
for StockItem in StockItems:                        # For each item in the list of keys... 
    StockList.append(StockItem)                     # Adds the item to the list of items the store sells. 
ListRun = 1                                         # Sets up a variable for the 'while' loop to run off. 
ItemList = []                                       # Sets up a blank list for items to be bought. 
CountList = []                                      # Sets up a blank list for number ofeach item to be bought. 
Numbers = "0123456789"                              # } Sets up a list of numbers. 
NumbersList = list(Numbers)                         # } 
while ListRun == 1:                                 # 'while' loop for purchasing items. 
    Item = input ("Enter the item you would like to purchase or type 'quit' when finished building list: ") # Queries the user for the item they want. 
    ItemLower = Item.lower()                        # Makes the item lowercase. 
    ItemCheck = 0                                   # Sets the item check to false. 
    if ItemLower == 'quit':                         # If the user is finished. 
        break                                       # Breaks the 'while' loop. 
    else:                                           # Else... 
        for Thing in StockList:                     # For each item in stock. 
            if ItemLower == Thing:                  # If the item the user wants is sold by the store... 
                ItemCheck = 1                       # Item check is true. 
                ItemCountRun = 1                    # Sets up the 'while' loop for the number of each item the user wants. 
    if ItemCheck == 1:                              # If item check is true... 
        while ItemCountRun == 1:                    # 'while' loop for the number of each item the user wants. 
            ItemCount = input ("Enter the quantity of " + ItemLower + " you would like to purchase: ")      # Queries the user for the number of the item they want. 
            ItemCountList = list(ItemCount)         # Turns the user's input into a list of its characters. 
            NumberCheck = 0                         # Sets the number check to false. 
            if ItemCount == 'quit' or ItemCount == 'Quit':                                                  # If they user wants to quit... 
                break                               # Breaks the 'while' loop. 
            else:                                   # Else... 
                for Character in ItemCountList:     # Goes through the user's input one character at a time. 
                    for Number in NumbersList:      # Goes the number one at a time. 
                        if Character == Number:     # If the user input is a number... 
                            NumberCheck = 1         # Number check is true.
            if NumberCheck == 1:                    # If number check is true... 
                ItemList.append(ItemLower)          # Adds the item to the list of items to be bought. 
                CountList.append(ItemCount)         # Adds the number of items the user wants to the number of items to be bought. 
                ItemCountRun = 0                    # Sets up to end the number 'while' loop. 
                break                               # Breaks the number 'while' loop. 
            elif NumberCheck == 0:                  # If number check is false... 
                print ("Please type the quantity as a number (i.e. 1, 12, 5967).")                          # Asks the user to input a number. 
    elif ItemCheck == 0:                            # If item check is false...
        print ("That item in not on the sales list.")                                                       # Tells the user that the item they entered isn't sold. 
grocery_cost(ItemList,CountList)                    # Runs the function grocery_cost. 
stock_check(StockList)                              # Runs the function stock_check.  

