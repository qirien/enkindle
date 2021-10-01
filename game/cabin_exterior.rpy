# Cabin Exterior

label EnterCabinExterior:
    "As the door latches shut behind me, a cold wind brushes against me and slips under my jacket right next to my skin."
    "We can have more text."
    "And even more."
    return

screen CabinExteriorScreen():
    frame:
        xfill True
        yfill True
        vbox:
            textbutton "Go Inside" action [SensitiveIf(in_room), SetVariable("current_room", "CabinInterior"), Jump("ChangeRoom")]