
"""
Product Inventory Project:

Create an application which manages an inventory of products. Create a product 
class which has a price, id, and quantity on hand. Then create an inventory 
class which keeps track of various products and can sum up the inventory value.
"""

class Product:
    id_num = 1
    
    def __init__(self, name, price=None, *args, **kwargs):
        self.name = name
        self.price = price
        self.id_num = Product.id_num
        
        
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        Product.id_num += 1
            
    def __str__(self):
        return self.name.title()
    
    def __repr__(self):
        return self.name.title()
    

class Inventory(list):
    id_num = 1
        
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.id_num = Inventory.id_num
        Inventory.id_num += 1

    def add_item(self, item):
        if isinstance(item, Product):
            self.append(item) 
        else:
            raise ValueError("must be of type Product")
           
    
class Inventory_Actions():

    def value_dollars(self,inventory):
        total_value = 0
        for product in inventory:
            try:
                total_value += float(product.price)
            except TypeError:
                continue      
        return total_value
    
    def no_price(self, inventory):
        no_price = []
        no_price.extend([prod for prod in inventory if not prod.price])
#        for product in inventory:
#            if not product.price:
#                no_price.append((product, product.id_num))
        if not no_price:
            return "All products priced"
        return no_price
    
    def price_adjust(self, id_num, new):
        for prod in self:
            if prod.id_num == id_num:
                prod.price = new
    
        
    def summary(self, inventory):
        print("\n")
        print("Inventory: {}".format(inventory.name.title()))
        print("Inventory value: " + "{}".format(self.value_dollars(inventory))) 
        print("Missing price(Product,Id#): " + str(self.no_price(inventory))) 
        return ''


#shirt = Product('shirt', price = 3.25)
#pants = Product('pants')
#
#clothing = Inventory('clothing')
#clothing.extend([shirt, pants])
#
#invrep = Inventory_Actions()
#invrep.summary(clothing)
