'''
Our business has been flourishing, we need to include a second day to receive shipments
instead of just Saturdays.

The business owner has scheduled deliveries to occur on Saturdays and Wednesdays.
As a results, we need to modify our program to accommodate this new requirement.

You need to write some tests for the new situations, as well as incorporate the new requirement into
your refactored code.

Everything else must remain the same for the program, and the discount days and amounts have not changed.

Notes:
- need to change the naming convention: shipment_num (for Wednesday and Saturdays)
'''

# from InventoryManagerPython.Item import Shipment
from Item import Shipment

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __checkExpired(self, item):
        itemsToRemove = []
        inventory = { "Dairy": 7, "Bread": 14, "Fruit": 5}
        for name, date in inventory.items():
            if item.daysInStore > date - 1:
                if item.name == name:
                    if item.daysInStore > date:
                        itemsToRemove.append(item)
                    item.price *= 0.75
        for item in itemsToRemove:
            self.items.remove(item)        
            
    def __checkTuesdayDiscount(self, item):
        # checks which shipment day it is and how many days the product has
        # been in store
        if (item.shipment == Shipment.Saturday and (item.daysInStore == 3 or item.daysInStore == 10)) or \
            (item.shipment == Shipment.Wednesday and (item.daysInStore == 6 or item.daysInStore == 13)):
            if item.daysInStore == 3 or item.daysInStore == 6 or item.daysInStore == 10 or item.daysInStore == 13:
                if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
                        item.price /= 0.9
                    
        # counter for the days
        if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
            item.daysInStore += 1

        # discount for days 3, 6, 10, and 13 depending on the shipment day
        if (item.shipment == Shipment.Saturday and (item.daysInStore == 3 or item.daysInStore == 10)) or \
            (item.shipment == Shipment.Wednesday and (item.daysInStore == 6 or item.daysInStore == 13)):
            if item.daysInStore == 3 or item.daysInStore == 6 or item.daysInStore == 10 or item.daysInStore == 13:
                if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
                        item.price *= 0.9
    
    def updateInventory(self):
        for item in self.items:
            self.__checkTuesdayDiscount(item)                
            self.__checkExpired(item)

        
