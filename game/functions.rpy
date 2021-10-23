# Utility functions and variables used elsewhere
init -100:
    # TODO: this doesn't work for inventory items.
    transform highlight_imagebutton():
        on default:
            additive 0.0
        on hover:
            additive 0.2
        on idle:
            additive 0.0 

    transform alpha_imagebutton():
        on start:
            alpha 0.6
        on idle:
            alpha 0.6      
        on hover:
            alpha 1.0
    
    transform icon_size:
        xsize 100
        ysize 100

    define light_gray = "#aaaaaa"
    define japanese_font = "fonts/NotoSerifJP-Regular.otf"
    define korean_font = "fonts/NotoSerifKR-Regular.otf"
    define thai_font = "fonts/NotoSerifThai-Regular.ttf"

init python:
    def has_fire_items():
        global inventory
        return (inventory.hasItem("kindling") and inventory.hasItem("flint") and inventory.hasItem("axe") and inventory.hasItem("wood"))
    
    # Start the fire if we have what we need, otherwise say something.
    def start_fire():
        global inventory
        if has_fire_items():
            renpy.jump("lit_fire")
        else:
            renpy.call("narrate",cantlight_msg)
        return

    StartFire = renpy.curry(start_fire)