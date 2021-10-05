# Snowy Hill

label EnterSnowyHill:
    "I trudge uphill through the snow. I can't even see the trail anymore because the snow is covering everything. Everything."
    return

screen SnowyHillScreen():
    frame:
        background "snowyhill"
        xfill True
        yfill True
        vbox:
            textbutton "Go West" sensitive in_room action [SetVariable("current_room", "SnowyWoods"), Jump("ChangeRoom")]