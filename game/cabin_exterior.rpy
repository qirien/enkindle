# Cabin Exterior

label EnterCabinExterior:
    "As the door latches shut behind me, a cold wind brushes against me and slips under my jacket right next to my skin."
    "We can have more text."
    "And even more."
    return

screen CabinExteriorScreen():
    frame:
        background "cabinexterior"
        xfill True
        yfill True
        vbox:
            textbutton "Go Inside" sensitive in_room action [SetVariable("current_room", "CabinInterior"), Jump("ChangeRoom")]