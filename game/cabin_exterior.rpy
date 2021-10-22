# Cabin Exterior

label EnterCabinExterior:
    #Play whichever sound if appropriate
    if (previous_room == "SnowyHill"):
        play sound "sfx/walk-snow-fast.ogg"
    if (previous_room == "CabinInterior"):
        play sound "sfx/close-door.ogg"
    return

screen CabinExteriorScreen():
    frame:
        background "cabinexterior"
        xfill True
        yfill True
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
            xalign 1.0
            yalign 0.5
            at alpha_imagebutton
        imagebutton:                    
            idle "gui/up_arrow.png"          
            sensitive in_room 
            action [SetVariable("current_room", "CabinInterior"), Jump("ChangeRoom")]
            xalign 0.5     
            yalign 0.5
            at alpha_imagebutton

        if (not inventory.hasItem("axe")):
            imagebutton:                
                idle "images/axe_cover.png"
                sensitive in_room
                action AddItem("axe")
                xalign 0.8
                yalign 0.8
                at highlight_imagebutton
        use inventory_screen
