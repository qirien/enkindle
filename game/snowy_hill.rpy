# Snowy Hill

label EnterSnowyHill:
    return

screen SnowyHillScreen():
    frame:
        background "snowyhill"
        xfill True
        yfill True
        vbox:
            textbutton "Go West" sensitive in_room action [SetVariable("current_room", "SnowyWoods"), Jump("ChangeRoom")]
        use inventory_screen