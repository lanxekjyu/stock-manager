#======== Imported libraries ==========
from tabulate import tabulate

#======== The beginning of the class ==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.code

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'''Country :   {self.country}
Code    :   {self.code}
Product :   {self.product}
Cost    :   {self.cost}
Quantity:   {self.quantity}'''

#============= Shoe list ===========
shoe_list = []

#========== Functions outside the class ==============
def read_shoes_data():
    
    # Open 'inventory.txt' file and print error if there is no such file
    try:
        with open('inventory.txt') as f:
            # Skip first line
            next(f)

            # For every line in file 'inventory.txt', create a Shoe object using this data, then append the created object to 'shoe_list'
            for line in f:
                country, code, product, cost, quantity = map(str,line.strip().split(','))
                cost = int(cost)
                quantity = int(quantity)
                shoe_list.append(Shoe(country, code, product, cost, quantity))

    except IOError as e:
        print(e)
        

def capture_shoes():

    # Get all necessary data from user in order to create new Shoe object
    country = input('Enter Country: ')
    code = input('Enter Code: ')
    product = input('Enter Product: ')
    cost = int(input('Enter Cost: '))
    quantity = int(input('Enter Quantity: '))

    # Create new Shoe object and append it to shoe_list
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    print(' ► This item has been logged into the system.')

    # The task did not specify this, but I think it's appropriate to update the 'inventory.txt' file with the captured shoe data
    with open ('inventory.txt', 'w+') as f:
        f.write('Country,Code,Product,Cost,Quantity\n')
        for item in shoe_list:
            f.write(f'{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n')


def view_all():

    # Print all items in 'shoe_list' in tabular format
    table = [[item.country, item.code, item.product, item.cost, item.quantity] for item in shoe_list]
    print(tabulate(table,headers=['Country', 'Code', 'Product', 'Cost', 'Quantity']))


def re_stock():

    # Create list to store shoe objects that equally have the lowest quantity attribute
    min_quantity_list = []
    
    # Find the first shoe object with the minimum quantity and store it in 'min_quantity_item'
    min_quantity_item = min(shoe_list, key = lambda s: s.quantity)

    # Compare all shoe objects in 'shoe_list' to the object in 'min_quantity_item', 
    # then append all objects that match in quantity attribute to the 'min_quantity_list'
    for item in shoe_list:
        if item.quantity == min_quantity_item.quantity:
            min_quantity_list.append(item)

    # For every item in 'min_quantity_list', ask the user for restock values
    for item in min_quantity_list:
        print(item)
        add_stock = int(input('How much quantity would you like to add to this item? '))
        item.quantity += add_stock
        
    # Write the updated 'shoe_list' to the 'inventory.txt' file
    with open ('inventory copy.txt', 'w+') as f:
        f.write('Country,Code,Product,Cost,Quantity\n')
        for item in shoe_list:
            f.write(f'{item.country},{item.code},{item.product},{item.cost},{item.quantity}\n')
        
    print('\n ► These items have been restocked.\n')


def search_shoe():

    # Get code from user then lookup this value among the '.code' properties of the objects in 'shoe_list'
    code = input('Enter the code for the item you want to view: ')
    item = next((item for item in shoe_list if item.code == code), ' ► That code does not match any items in our inventory.')
    print(item)


def value_per_item():

    # Print all items in 'shoe_list' in tabular format but add a 'Total Value' column
    table = [[item.country, item.code, item.product, item.cost, item.quantity, (item.cost * item.quantity)] for item in shoe_list]
    print(tabulate(table,headers=['Country', 'Code', 'Product', 'Cost', 'Quantity', 'Total Value']))


def highest_qty():

    # Create list to store shoe objects that equally have the highest quantity attribute
    max_quantity_list = []
    
    # Find the first shoe object with the maximum quantity and store it in 'max_quantity_item'
    max_quantity_item = max(shoe_list, key = lambda s: s.quantity)

    # Compare all shoe objects in 'shoe_list' to the object in 'max_quantity_item', 
    # then append all objects that match in quantity attribute to the 'max_quantity_list'
    for item in shoe_list:
        if item.quantity == max_quantity_item.quantity:
            max_quantity_list.append(item)
    
    # Print all items in the 'max_quantity_list'
    for item in max_quantity_list:
        print(' ► This item is on sale!')
        print(item)


#========== Banner ==========
print('''
┌─────────────────────────────────────────────────────┐
│                                                     │
│         Welcome to NIKE Stock Manager v1.0!         │
│                                                     │
└─────────────────────────────────────────────────────┘
''')

#========== Main Menu =============
while True:
    menu = input('''
 ► Select option:

v   -   View all items in inventory
a   -   Add an item
r   -   Restock lowest quantity item/s
s   -   Search for an item using its code
tv  -   Total value per item
h   -   Highest stock item/s
q   -   Quit
: ''')
    print()

    if menu.lower() == 'v':
        read_shoes_data()
        view_all()
        shoe_list = []

    elif menu.lower() == 'a':
        read_shoes_data()
        capture_shoes()
        shoe_list = []

    elif menu.lower() == 'r':
        read_shoes_data()
        re_stock()
        shoe_list = []

    elif menu.lower() == 's':
        read_shoes_data()
        search_shoe()
        shoe_list = []

    elif menu.lower() == 'tv':
        read_shoes_data()
        value_per_item()
        shoe_list = []
    
    elif menu.lower() == 'h':
        read_shoes_data()
        highest_qty()
        shoe_list = []

    elif menu.lower() == 'q':
        quit()
        
    else:
        print(' ► Invalid input. Please try again.')
