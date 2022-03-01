import unittest

# from InventoryManagerPython.Inventory import Inventory
# from InventoryManagerPython.Item import Item
# from InventoryManagerPython.Item import Shipment
from Inventory import Inventory
from Item import Item
from Item import Shipment

class MyTestCase(unittest.TestCase):
    # tests for gift card updates on Wednesday
    def test_GiftCardUpdates_Wednesday(self):
        item = Item("GiftCard", 20, Shipment.Wednesday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()

        self.assertEqual(0, item.daysInStore)
        self.assertEqual(20, item.price)

    # tests for gift card updates on Saturday
    def test_GiftCardUpdates_Saturday(self):
        item = Item("GiftCard", 20, Shipment.Saturday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()

        self.assertEqual(0, item.daysInStore)
        self.assertEqual(20, item.price)

    # tests for dairy updates on Wednesday
    def test_DairyUpdates_Wednesday(self):
        item = Item("Dairy", 50, Shipment.Wednesday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(6, item.daysInStore)
        self.assertEqual(45, item.price)
        inventory.updateInventory()
        self.assertEqual(7, item.daysInStore)
        self.assertEqual(37.5, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))

    # tests for dairy updates on Saturday
    def test_DairyUpdates_Saturday(self):
        item = Item("Dairy", 50, Shipment.Saturday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(45, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(6, item.daysInStore)
        self.assertEqual(50, item.price)
        inventory.updateInventory()
        self.assertEqual(7, item.daysInStore)
        self.assertEqual(37.5, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))
        
    # tests for fruit updates on Wednesday
    def test_FruitUpdates_Wednesday(self):
        item = Item("Fruit", 30, Shipment.Wednesday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(22.5, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))
        
    # tests for fruit updates on Saturday
    def test_FruitUpdates_Saturday(self):
        item = Item("Fruit", 30, Shipment.Saturday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(27, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(30, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(22.5, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))

    # tests for bread updates on Wednesday
    def testBreadUpdates_Wednesday(self):
        item = Item("Bread", 100, Shipment.Wednesday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(6, item.daysInStore)
        self.assertEqual(90, item.price)
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        self.assertEqual(13, item.daysInStore)
        self.assertEqual(90, item.price)
        inventory.updateInventory()
        self.assertEqual(14, item.daysInStore)
        self.assertEqual(75, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))
    
    # tests for bread updates on Saturday
    def testBreadUpdates_Saturday(self):
        item = Item("Bread", 100, Shipment.Saturday)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()
        self.assertEqual(1, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(2, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(3, item.daysInStore)
        self.assertEqual(90, item.price)
        inventory.updateInventory()
        self.assertEqual(4, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        self.assertEqual(5, item.daysInStore)
        self.assertEqual(100, item.price)
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        inventory.updateInventory()
        self.assertEqual(14, item.daysInStore)
        self.assertEqual(75, item.price)
        inventory.updateInventory()
        self.assertEqual(0, len(inventory.items))


if __name__ == '__main__':
    unittest.main()
