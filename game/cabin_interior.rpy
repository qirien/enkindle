# Cabin Interior

label EnterCabinInterior:
    "I close the door behind me, but it won't stay latched. I have to slam it into place, and by that time, the wind has made the room even colder."
    return

screen CabinInteriorScreen():
    frame:
        background "cabininterior"
        xfill True
        yfill True
        vbox:
            textbutton "Go Outside" sensitive in_room action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]

