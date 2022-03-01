from enum import Enum, unique

# created class for specific shipment days
@unique
class Shipment(Enum):
    # shipment 1
    Wednesday = 1
    # shipment 2
    Saturday = 2

class Item:
    def __init__(self, name, price, shipment):
        
        # renamed to daysInStore because timeInStore was a little
        # too general
        self.shipment = shipment
        self.daysInStore = 0
        self.price = price
        self.name = name
