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
                textbutton "Go West" sensitive in_room action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
            hbox:
                imagebutton idle "images/wolves.png" action Call("narrate", wolf_description) at highlight_imagebutton
                if (not inventory.hasItem("flint")):
                    imagebutton idle "images/flint.png" action AddItem("flint") at highlight_imagebutton
                if (not inventory.hasItem("doll")):
                    imagebutton idle "images/doll_cover.png" action AddItem("doll") at highlight_imagebutton
                if (not inventory.hasItem("wood")):
                    imagebutton idle "images/wood_cover.png" action AddItem("wood") at highlight_imagebutton

        use inventory_screen