# Inventory System
# written by Andrea Landaker, Metasepia Games <http://metasepiagames.com>
# This code is in the public domain.
# 

init -100 python:  
    # Ordered dictionary storing name and quantity
    # {name: {quantity:, order:}}
    class Inventory(dict):
        def __missing__(self, key):
            return 0
        
        def _ensure_item_exists(self, name):
            # Initialize the next_order the first time this function is called.
            # Normally we'd handle this in __init__, but in Python 2, you can't override __init__ when inheriting from dict.
            try:
                self.next_order
            except:
                self.next_order = 0
            self.setdefault(name, {"name": name, "quantity": 0, "order": self.next_order})
            self.next_order += 1

        def addItem(self, name, quantity=1):
            assert quantity >= 0
            self._ensure_item_exists(name)
            self[name]["quantity"] = self[name]["quantity"] + quantity
            return self[name]["quantity"]

        def removeItem(self, name, quantity=1):
            assert quantity >= 0
            self._ensure_item_exists(name)
            item_quantity = self[name]["quantity"]
            item_quantity = max(0, item_quantity - quantity)
            if item_quantity == 0: del self[name]
            else: self[name]["quantity"] == item_quantity
            return item_quantity

        def toList(self):
            return sorted(
                list(self.values()),
                key=lambda item: item["order"]
            )

        def hasItem(self, name):
            if (self[name]):
                return (self[name]["quantity"] > 0)
            return False

init python:
    def add_item(name, quantity=1):
        global inventory
        renpy.play("sfx/snow-grab.ogg", "sound")        
        inventory.addItem(name, quantity)
        if (items[name]):
            renpy.call("narrate", items[name])
        renpy.restart_interaction()
        return

    AddItem = renpy.curry(add_item)