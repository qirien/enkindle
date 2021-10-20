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
                textbutton "Head East" sensitive in_room action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
            hbox:
                xalign 0.8
                yalign 0.8
                if (not inventory.hasItem("axe")):
                    imagebutton idle "images/axe_cover.png" action AddItem("axe") at highlight_imagebutton
        use inventory_screen
