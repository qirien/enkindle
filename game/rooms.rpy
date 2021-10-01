screen CabinInteriorScreen():
    frame:
        xfill True
        yfill True
        vbox:
            textbutton "Go Outside" action [SetVariable("current_room", "CabinExterior"), Jump("ChangeRoom")]


screen CabinExteriorScreen():
    frame:
        xfill True
        yfill True
        vbox:
            textbutton "Go Inside" action [SetVariable("current_room", "CabinInterior"), Jump("ChangeRoom")]