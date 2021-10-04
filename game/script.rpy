# The script of the game goes in this file.

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0
default in_room = False

# TODO: Inventory

label start:

    $ current_room = "CabinInterior"
    "Every time I come to the cabin, it brings back memories..."
    window auto hide

    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")

    return
