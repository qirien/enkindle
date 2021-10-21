# Cabin Interior

label EnterCabinInterior:
    return

screen CabinInteriorScreen():
    frame:
        background "cabininterior"
        xfill True
        yfill True
        imagebutton:
            idle "images/fireplace.png"
            sensitive in_room 
            action StartFire()
            xpos 780 ypos 525  
            at highlight_imagebutton
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room 
            action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
            xalign 1.0
            yalign 0.5
            at alpha_imagebutton

        use inventory_screen
