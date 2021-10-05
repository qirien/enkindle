# Snowy Woods

label EnterSnowyWoods:
    "Farther from the cabin, the trees get thicker. Thick enough to hide just about anything."
    return

screen SnowyWoodsScreen():
    frame:
        background "snowywoods"
        xfill True
        yfill True
        vbox:
            textbutton "Go West" sensitive in_room action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]
            textbutton "Go East" sensitive in_room action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]