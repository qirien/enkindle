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
                textbutton "Wolves" action Call("narrate", "The wolves must be hunting. How cute! They know better than to come near us, I’m sure.")
                textbutton "Flint" action AddItem("flint")
                textbutton "Doll" action AddItem("doll")
                textbutton "Kindling" action AddItem("kindling")
        use inventory_screen