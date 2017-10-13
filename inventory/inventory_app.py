from inventory import Product, Inventory, Inventory_Actions


def main_menu():
    '''Returns user's choice of new or quit'''
    
    print(
    "Enter 'NEW' for new inventory\n"+\
    "Enter 'QUIT' to quit\n"
    )
    choice = input('> ').lower()
    return choice

def new_inv():
    '''obtains the inventory's name from user and returns an Inventory instance
    '''    
    name = input("Enter inventory name\n> ")
    inv = Inventory(name)
 
    return inv

def inventory_menu():
    '''returns user's choice of add, report, or back'''
    
    print(
    "Enter 'ADD' to add a product to this inventory\n"+\
    "Enter 'REPORT' for report options\n"    
    "Enter 'BACK' to return to main menu\n"       
    )
    choice = input("> ").lower()
    return choice

def create_prod():
    '''obtains Product name and price from user
    creates Product instance'''
    
    name = input("Product name: ").lower()
    price = input("product price: ")
    print('-' *20)
    print('\n')
    item = Product(name=name, price=price) 
    return item       


def add_item_to_inv(item, inv):
    '''adds product to inventory. Performs a check'''
    choice = input("Do you want to add {} to the {} inventory?\nY/n\n>".format(item.name, inv.name)).lower()
    if choice in ['y', 'yes']:
        inv.add_item(item)
        print("{} was added to the {} inventory".format(item.name, inv.name))
        
    else:
        print("{} was NOT added to the {} inventory".format(item.name, inv.name))
        


def inventory_app():
    inventory_dict = {}    
    while True:
        #returns new, select, or quit
        main_choice = main_menu().lower()
        print(main_choice)
        
        if main_choice in ['quit','q']:
            break        

        elif main_choice == 'new':
            #create Inventory obj 
            inv = new_inv()  
            
            #Inventory Loop
            inventory = True
            while inventory:
                # add, report, go-back
                inv_choice = inventory_menu()
                adding = False
                                
                if inv_choice == 'back':
                    break            
                elif inv_choice == 'add':
                    adding = True
                elif inv_choice == 'report':
                    report = Inventory_Actions()
                    print(report.summary(inv))
                #Add items Loop
                while adding:
                    #create a Product obj with name and price
                    item = create_prod()
                    #and append that new product to inv
                    add_item_to_inv(item, inv)
                    print('-' * 20) 
                    print('\n')
                    while True:
                        inv_choice = inventory_menu()
                        if inv_choice == 'add':
                            break
                        elif inv_choice == 'report':
                            print(inv)
                            
                            report = Inventory_Actions()
                            print(report.summary(inv))        
                        elif inv_choice == 'back':
                            #log this inventory
                            inventory_dict[inv.name] = inv
                            #inventory_list.append(inv)
                            #breaks out of 3 loops to return to main menu
                            adding = False
                            inventory = False
                            break
                    
        else:
            print("Please select from the menu\n")
    print("Goodbye")        
    return inventory_dict                
                

#inventory_dict = inventory_app()       

    
    
        







#if __name__=='__main__':
#    inventory_app()
#pants = Product('pants', 1.25)
#shirt = Product('shirt', )
#
#clothing = Inventory('clothing')
#
#clothing.append(shirt)
#clothing.append(pants)
#print("\n")
#print("Inventory: {}".format(clothing.name.title()))
#print("Inventory value: " + "{}".format(clothing.value_dollars())) 
#print("Missing price(Product,Id#): " + str(clothing.no_price()))

