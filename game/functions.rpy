init -100:
    transform highlight_imagebutton():
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

init python:
    def start_fire():
        global inventory
        if (inventory.hasItem("kindling") and inventory.hasItem("flint") and inventory.hasItem("axe") and inventory.hasItem("wood")):
            renpy.jump("lit_fire")
        else:
            renpy.call("narrate",cantlight_msg)
        return

    StartFire = renpy.curry(start_fire)