import unittest

# from InventoryManagerPython.Inventory import Inventory
# from InventoryManagerPython.Item import Item
from Inventory import Inventory
from Item import Item

class MyTestCase(unittest.TestCase):
    def test_GiftCardUpdates(self):
        item = Item("GiftCard", 20)
        inventory = Inventory()
        inventory.add(item)

        inventory.updateInventory()

        self.assertEqual(0, item.daysInStore)
        self.assertEqual(20, item.price)

    def test_DairyUpdates(self):
        item = Item("Dairy", 50)
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

    def test_FruitUpdates(self):
        item = Item("Fruit", 30)
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

    def testBreadUpdates(self):
        item = Item("Bread", 100)
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
