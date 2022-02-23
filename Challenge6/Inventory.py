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
        # day 3 = tuesday first week
        # day 10 = tuesday second week
        if item.daysInStore == 3 or item.daysInStore == 10:
            if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
                    item.price /= 0.9
                    
        # counter for the days
        if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
            item.daysInStore += 1

        # discount for days 3 and 10
        if item.daysInStore == 3 or item.daysInStore == 10:
            if item.name == "Dairy" or item.name == "Bread" or item.name == "Fruit":
                    item.price *= 0.9
    
    def updateInventory(self):
        for item in self.items:
            self.__checkTuesdayDiscount(item)                
            self.__checkExpired(item)

        
