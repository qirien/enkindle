# Cabin Exterior

label EnterCabinExterior:
    #room description goes here
    return

screen CabinExteriorScreen():
    frame:
        background "cabinexterior"
        xfill True
        yfill True
        vbox:
            xfill True
            yfill True
            hbox:
                xalign 0.5               
                textbutton "Go Inside" sensitive in_room action [SetVariable("current_room", "CabinInterior"), Jump("ChangeRoom")]
            hbox:
                xalign 1.0
                yalign 0.5
                textbutton "Head East" sensitive in_room action [SetVariable("current_room", "SnowyWoods"), Jump("ChangeRoom")]
            hbox:
                xalign 0.8
                yalign 0.8
                textbutton "Axe" action AddItem("axe") #TODO: also delete the axe so we can't pickup 1000 of them
        use inventory_screen

init python:
    def add_item(name, quantity=1):
        global inventory
        inventory.addItem(name, quantity)
        renpy.restart_interaction()
        return

    AddItem = renpy.curry(add_item)