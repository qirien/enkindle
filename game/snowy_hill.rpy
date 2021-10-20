# Snowy Hill

label EnterSnowyHill:
    return

screen SnowyHillScreen():
    frame:
        background "snowyhill"
        xfill True
        yfill True
        vbox:
            textbutton "Go West"  yalign 0.5 xalign 0.0 sensitive in_room action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
            textbutton "Go East"  yalign 0.5 xalign 1.0 sensitive in_room action [SetVariable("current_room", "SnowyWoods"), Jump ("ChangeRoom")]
            hbox:
                if (not inventory.hasItem("blanket")):
                    imagebutton idle "images/blanket_cover.png" action AddItem("blanket") at highlight_imagebutton
                if (not inventory.hasItem("flashlight")):
                    imagebutton idle "images/flashlight_cover.png" action AddItem("flashlight") at highlight_imagebutton
                if (not inventory.hasItem("kindling")):
                    imagebutton idle "images/kindling_cover.png" action AddItem("kindling") at highlight_imagebutton
        use inventory_screen