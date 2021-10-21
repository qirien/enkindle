# Snowy Hill

label EnterSnowyHill:
    return

screen SnowyHillScreen():
    frame:
        background "snowyhill"
        xfill True
        yfill True
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]            
            yalign 0.5
            xalign 0.0
            at alpha_imagebutton
        imagebutton:
            idle "gui/right_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "SnowyWoods"), Jump ("ChangeRoom")]
            xalign 1.0
            yalign 0.5
            at alpha_imagebutton
        
        if (not inventory.hasItem("blanket")):
            imagebutton:
                idle "images/blanket_cover.png"
                sensitive in_room
                action AddItem("blanket")
                pos (1400, 750)
                at highlight_imagebutton
        if (not inventory.hasItem("flashlight")):
            imagebutton:
                idle "images/flashlight_cover.png"
                sensitive in_room
                action AddItem("flashlight")
                pos (900, 400)
                at highlight_imagebutton
        if (not inventory.hasItem("kindling")):
            imagebutton:
                idle "images/kindling_cover.png"
                sensitive in_room
                action AddItem("kindling") 
                pos (200, 700)
                at highlight_imagebutton
        use inventory_screen