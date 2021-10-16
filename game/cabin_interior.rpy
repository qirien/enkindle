# Cabin Interior

label EnterCabinInterior:
    return

screen CabinInteriorScreen():
    frame:
        background "cabininterior"
        xfill True
        yfill True
        vbox:
            xfill True
            yfill True
            textbutton "Go Outside":
                sensitive in_room 
                action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
                xalign 1.0
                yalign 0.5
            textbutton "Light a Fire" xalign 0.5 action StartFire() 
        use inventory_screen
