# Snowy Woods

label EnterSnowyWoods:
    return

screen SnowyWoodsScreen():
    frame:
        background "snowywoods"
        hbox:
            xfill True
            yfill True
            textbutton "Go West"  yalign 0.5 xalign 0.0 sensitive in_room action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
            textbutton "Go East"  yalign 0.5 xalign 1.0 sensitive in_room action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
        use inventory_screen