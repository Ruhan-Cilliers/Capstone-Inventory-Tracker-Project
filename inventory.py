
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self, index):
        
        # Opening the textfile.
        with open("inventory.txt", "r") as inventory:
            
            # Skipping the first line.
            next(inventory)
            
            
            # Creating a readable list of the products at the specified index.
            inventory_list = inventory.readline(index)
 
            individual_inventory_item = inventory_list.split(",")

            # Setting a variable that can be returned
            cost = individual_inventory_item[3]
        
        return int(cost)
        

    def get_quantity(self, index):
        
        # Same logic as the " get_cost " function.
        with open("inventory.txt", "r") as inventory:
            
            next(inventory)
            
            inventory_list = inventory.readline(index)
 
            individual_inventory_item = inventory_list.split(",")

            quantity = individual_inventory_item[4]
        
        return int(quantity)


    def __str__(self):
        
         return f'''
________________________________________________

Product name: {self.product}
Product cost: R{self.cost}
Product code: {self.code}
Product location: {self.country}
Quantity of product available: {self.quantity}

________________________________________________'''


#=============Shoe list===========

shoe_list = []


#==========Functions outside the class==============
def read_shoes_data():
    
    # Defining the shoe list as empty so that it is constantly updating 
    # Whenever the data needs to be read.
    global shoe_list

    try:
        with open("inventory.txt", "r") as inventory:

            # Next funtion was obtained from site:
            # https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row
            
            next(inventory)

            
            inventory_list = inventory.readlines()

            
            # Looping through the inventory and creating an object using that data.
            # The object is then added to the list.
            for inventory_items in inventory_list:

                individual_item = inventory_items.split(",")

                shoe_list.append(Shoe(individual_item[0], individual_item[1], individual_item[2], individual_item[3], individual_item[4]))

    
    except FileNotFoundError:
        print("Please ensure that the file is open or in the correct location and try the program again.")


def capture_shoes():
    
    
    # Recieving input from the user.
    print("___________________________________________________________\n")
    country = input("Please enter the country where the product is available: ")
    code = input("Please enter the code of the product: ")
    product = input("Please enter the product name: ")
    cost = input("Please enter the cost of the product: ")
    quantity = input("Please enter the quantity of the product: ")
    print("____________________________________________________________")
    
    
    # Adding the data to the shoe list.
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    
    # Creating a string with the input data.
    new_item = ",".join((country, code, product, cost, quantity)) + "\n"

    # Adding the data to the text file.
    with open("inventory.txt", "a") as inventory:
        
        inventory.write(new_item)

    print(f'''
____________________________________________
          
The following product has been added:
Country: {country}
Code: {code}
Name of Product: {product}
Cost: {cost}
Quantity: {quantity}

____________________________________________''')

def view_all():
    

    # Read updated data.
    read_shoes_data()
    
    # Set counter so that the iteration goes over the whole list.
    for shoe in shoe_list:

        # Calling the str function to print each item.
        print(shoe)


def re_stock():

    print("entering restock")
    
    # Open text file.
    with open("inventory.txt", "r+") as inventory:

        print("file opened successfully")
        next(inventory)
        inventory_list = inventory.readlines()
        

        # Setting the initial value to infinity thus any quanitity value will be lower.
        min_quantity = float('inf')
        
        for item_index, individual_item in enumerate(inventory_list):

            individual_item = individual_item.split(",")

            # Check quantity of current item
            if int(individual_item[4]) < min_quantity:

                # Set variables to specific data to be used later in function
                item_number = item_index
                code = individual_item[1]
                product = individual_item[2]
                min_quantity = int(individual_item[4])


        print(f'''
The product with the lowest quantity is:
Product: {product}
Code: {code}
Quantity: {min_quantity}

Please enter either Yes or No''')
        
        
        change_quantity_decision = input("Would you like to restock this product?: ")

        # Using a while statement so that program continues until user chooses to exit.
        while True:
        
            if change_quantity_decision.lower() == "yes":

            
                # Using while statement to prevent program from crashing.
                while change_quantity_decision == "yes":
                
                
                    # Using try statement to ensure valid response.
                    try:
                        change_quantity = int(input("By how much would you like to restock this product: "))

                        # Creating new restock value.
                        restock = change_quantity + int(min_quantity)

                        # Creating list at the specific index
                        change = inventory_list[item_number].split(",")

                        # Changing quantity value.
                        change[4] = str(restock)

                        # Adding change value back to a string
                        inventory_list[item_number] = ",".join(change) + "\n"
            
                        # Using the seek funtion to return to the start of the list.
                        inventory.seek(0)

                        # We clear the entire contents of the inventory using the truncate function as
                        # it alters the list to be the same size as where the pointer is
                        # which is at the start of the text file after using the seek function.

                        inventory.truncate()
                        
                        # Writing the new data in the text file
                        inventory.writelines(inventory_list)

                        print(f'''
_____________________________________________

The following product quantity data has been updated:
Product: {product}
Code: {code}
Quantity: {restock}

_____________________________________________''')
                        
                        change_quantity_decision = "no"
                        break


                    except ValueError:

                        print("Please enter a number.\n")

        
            elif change_quantity_decision.lower() == "no":
                break


            else:
                print("Please enter a appropriate input")
                change_quantity_decision = input("Would you like to restock this product?: ")


def seach_shoe():
    
    read_shoes_data()
    
    # Asking user for the desired product code.
    code_search = input("Please enter the code of the shoe you are searching for: ")

    # Looping through the list and attempting to find a matching value.
    for shoe in shoe_list:

        if code_search == shoe.code:

            # Displaying shoes data
            print(shoe)
            break


def value_per_item():
    

    # Updating the list so that it is always using the most current data
    read_shoes_data()
    
    # Looping through shoelist
    for shoe in shoe_list:

        # Using class functions to get the cost and quantity of the items.
        total_value = int(shoe.cost) * int(shoe.quantity)
        
        # Displaying data.
        print(f'''
________________________________________________________________________________________

{shoe.product} has a individual cost of R{shoe.cost} and quantity of {shoe.quantity}.
The total value has been calculated to be: R{total_value}
________________________________________________________________________________________''')
    


def highest_qty():
    
    # Uses similar logic as the restock function, excluding the option to restock.
    with open("inventory.txt", "r") as inventory:

        next(inventory)
        inventory_list = inventory.readlines()
        

        max_quantity = 0

        for individual_item in inventory_list:

            individual_item = individual_item.split(",")

            if int(individual_item[4]) > max_quantity:

                code = individual_item[1]
                product = individual_item[2]
                max_quantity = int(individual_item[4])

        
        print(f'''
The product with the highest quantity is:
Product: {product}
Code: {code}
Quantity: {max_quantity}

This product is now on sale!
''')


#==========Main Menu=============
user = True

while user == True:

    menu = int(input('''
___________________________________________________
                     
Hello world! 
                     
Please pick the option you wish to access:
                     
1) Access the inventory data
2) Add item to inventory
3) Restock a item
4) Find a specific item
5) Determine the value per item
6) Item currently for sale
7) Exit menu
                     
___________________________________________________
                     
Menu option: '''))
    
    # Using try-except statement to ensure a appropriate response.
    try:

        if menu == 1:

            view_all()

        elif menu == 2:

            capture_shoes()

        elif menu == 3:
            
            re_stock()

        elif menu == 4:

            seach_shoe()

        elif menu == 5:

            value_per_item()

        elif menu == 6:
            
            highest_qty()

        elif menu == 7:
            
            print("\n Goodbye!!!\nEnjoy the rest of your day!")
            exit()

        else:

            print("Please enter a valid response\n")
            menu = int(input('''
___________________________________________________
                     
Hello world! 
                     
Please pick the option you wish to access:
                     
1) Access the inventory data
2) Add item to inventory
3) Restock a item
4) Find a specific item
5) Determine the value per item
6) Item currently for sale
                     
___________________________________________________'''))

    except ValueError:
        print("Please enter a valid response from the menu provided.\n")
        menu = int(input('''
___________________________________________________
                     
Hello world! 
                     
Please pick the option you wish to access:
                     
1) Access the inventory data
2) Add item to inventory
3) Restock a item
4) Find a specific item
5) Determine the value per item
6) Item currently for sale
7) Exit menu
                     
___________________________________________________
                     
Menu option: '''))
