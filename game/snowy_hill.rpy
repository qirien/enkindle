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
            hbox:
                if (not inventory.hasItem("flint")):
                    textbutton "Flint" action AddItem("flint")
                if (not inventory.hasItem("doll")):
                    textbutton "Doll" action AddItem("doll")
                if (not inventory.hasItem("kindling")):
                    textbutton "Kindling" action AddItem("kindling")
        use inventory_screen