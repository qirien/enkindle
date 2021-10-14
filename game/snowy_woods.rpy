# Snowy Woods

label EnterSnowyWoods:
    return

screen SnowyWoodsScreen():
    frame:
        background "snowywoods"
        vbox:
            xfill True
            yfill True
            hbox:
                xfill True
                textbutton "Go West"  yalign 0.5 xalign 0.0 sensitive in_room action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
                textbutton "Go East"  yalign 0.5 xalign 1.0 sensitive in_room action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
            hbox:
                textbutton "Wood" yalign 1.0 xalign 0.0 action AddItem("wood")
                textbutton "Blanket" yalign 1.0 xalign 0.5 action AddItem("blanket")
                textbutton "Flashlight" yalign 1.0 xalign 1.0 action AddItem("flashlight")
        use inventory_screen