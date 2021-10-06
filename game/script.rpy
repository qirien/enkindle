# The script of the game goes in this file.

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0
default in_room = False
default inventory = Inventory()

# TODO: Inventory

label start:
    #call choose_language

    $ current_room = "CabinInterior"
    "It’s really cold today. I need to start a fire."
    "I need to go outside to collect wood."

    window auto hide

    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")

    return

label choose_language:
    menu:
        "What language would you like?"
        "English":
            $ config.language = None
        "Español":
            $ config.language = "es"
        "Esperanto":
            $ config.language = "eo"
        "Français":
            $ config.language = "fr"
        "Deutsch":
            $ config.language = "de"

    return