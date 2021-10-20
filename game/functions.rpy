init -100:
    transform highlight_imagebutton():
        on hover:
            additive 0.2
        on idle:
            additive 0.0 

init python:
    def start_fire():
        global inventory
        if (not inventory.hasItem("kindling")):
            renpy.call("narrate", kindling_msg)
        elif (not inventory.hasItem("flint")):
            renpy.call("narrate",flint_msg)
        elif (not inventory.hasItem("axe")):
            renpy.call("narrate", axe_msg)
        elif (not inventory.hasItem("wood")):
            renpy.call("narrate", wood_msg)
        else:
            renpy.jump("lit_fire")
        return

    StartFire = renpy.curry(start_fire)