# The script of the game goes in this file.

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0
default in_room = False
default inventory = Inventory()
define items = {
    "axe":_("This is Dad’s axe. It will help chop down wood."), 
    "kindling":_("I could use this as kindling for the fire. That’ll come in handy!"),
    "flashlight":_("Isn’t this my brother’s flashlight? Why is it out here?"),
    "wood":_("Wood for the fire. Perfect."),
    "blanket":_("This was mom’s favorite blanket. She used to curl up by the fire under this thing. Perfect for snuggling. Too bad it’s all yucky now."),
    "doll":_("My sister’s favorite doll. She must have tried to hide it out here where it would be safe."),
    "flint":_("This flint will help start the fire. It looks so pretty when struck. I can use this and the axe head as a firestarter.")
}
define wolf_description = _("The wolves must be hunting. How cute! They know better than to come near us, I’m sure.")
define cantlight_msg = _("I don't have everything yet.")

label start:
    if (not persistent.languages):
        $ persistent.languages = []
    if (not persistent.times_played):
        $ persistent.times_played = 0
    $ renpy.save_persistent()
    call choose_language

    #play music "music/Unsolved.mp3" loop
    $ current_room = "CabinInterior"
    $ renpy.show_screen(current_room + "Screen")
    "It’s really cold today. I need to start a fire."
    "I need to go outside to collect what I need."


    window auto hide

    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")

    return

label lit_fire:
    "It's time."
    # TODO: cozy fire image here
    "Ahh, this is perfect. Thanks to the fire I’m nice and warm. Nothing like a good, cozy fire to lift your spirits!"
    $ persistent.languages.append(config.language)
    $ persistent.times_played += 1
    $ renpy.save_persistent()
    $ renpy.full_restart()
    return

label choose_language:
    menu:
        "Which language?"
        "English":
            $ renpy.change_language(None)
        "Esperanto":
            $ renpy.change_language("esperanto")
        # "Español":
        #     $ renpy.change_language("espanol")            
        # "Français":
        #     $ renpy.change_language("francais")
        # "Deutsch":
        #     $ renpy.change_language("deutsch")
        # "{font=fonts/unifont.ttf}日本語{/font}":
        #     $ renpy.change_language("japanese")
        

    return