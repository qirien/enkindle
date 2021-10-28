# Snowy Woods

label EnterSnowyWoods:
    play sound "sfx/walk-snow-fast.ogg"    
    return

screen SnowyWoodsScreen():
    frame:
        background "snowywoods"
        xfill True
        yfill True
        imagebutton:
            idle "gui/left_arrow.png"
            sensitive in_room
            action [SetVariable("current_room", "SnowyHill"), Jump("ChangeRoom")]
            xpos 0.0
            ypos 0.4
            at alpha_imagebutton
        imagebutton:
            idle "images/wolves.png"
            sensitive in_room
            action Call("narrate", wolf_description)
            pos (1240, 140)
            at highlight_imagebutton
        if (not inventory.hasItem("flint")):
            imagebutton:
                idle "images/flint.png"
                sensitive in_room
                action AddItem("flint")
                pos (467, 658)
                at highlight_imagebutton
        if (not inventory.hasItem("doll")):
            imagebutton:
                idle "images/doll_cover.png"
                sensitive in_room
                action AddItem("doll")
                pos (1305, 648)
                at highlight_imagebutton
        if (not inventory.hasItem("wood")):
            imagebutton:
                idle "images/wood_cover.png"
                sensitive in_room and inventory.hasItem("axe")
                action AddItem("wood")
                pos (845, 644)
                at highlight_imagebutton
        use inventory_screen