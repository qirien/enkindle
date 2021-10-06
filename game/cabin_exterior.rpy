# Cabin Exterior

label EnterCabinExterior:
    "As the door latches shut behind me, a cold wind brushes against me and slips under my jacket right next to my skin."
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
                textbutton "Axe" action inventory.addItem("axe")
            