init python:
    def start_fire():
        global inventory
        if (not inventory.hasItem("kindling")):
            renpy.call("narrate", _("I need kindling."))
        elif (not inventory.hasItem("flint")):
            renpy.call("narrate",_("I need something to make sparks."))
        elif (not inventory.hasItem("axe")):
            renpy.call("narrate",_("I need something steel to strike sparks."))
        elif (not inventory.hasItem("wood")):
            renpy.call("narrate", _("I need wood to burn."))
        else:
            renpy.jump("lit_fire")
        return

    StartFire = renpy.curry(start_fire)