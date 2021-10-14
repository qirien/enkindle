# The script of the game goes in this file.

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0
default in_room = False
default inventory = Inventory()
define items = {
    "axe":"This is Dad’s axe. It will help chop down wood.", 
    "kindling":"I could use this as kindling for the fire. That’ll come in handy!",
    "flashlight":"Isn’t this my brother’s flashlight? Why is it out here?",
    "wood":"Wood for the fire. Perfect.",
    "blanket": "This was mom’s favorite blanket. She used to curl up by the fire under this thing. Perfect for snuggling. Too bad it’s all yucky now.",
    "doll": "My sister’s favorite doll. She must have tried to hide it out here where it would be safe.",
    "wolves": "The wolves must be hunting. How cute! They know better than to come near us, I’m sure.",
    "flint":"This flint will help start the fire. It looks so pretty when struck. I can use this and the axe head as a firestarter."
}

# TODO: Inventory

label start:
    #call choose_language

    $ current_room = "CabinInterior"
    "It’s really cold today. I need to start a fire."
    "I need to go outside to collect what I need."


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