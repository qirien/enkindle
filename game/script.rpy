# Enkindle is (c) 2021 by Metasepia Games, http://www.metasepiagames.com
# This software is distributed under the GPL v3.0 license
# (see LICENSE)

# The script of the game goes in this file.
define language_name_map = {
    None:"English", 
    "esperanto":"Esperanto", 
    "francais":"Français",
    "nihongo":"{font=[japanese_font]}日本語{/font}",
    #"deutsch":"Deutsch",
    "espanol":"Español",
    "nederlands":"Nederlands",
    "hangul":"{font=[korean_font]}한국어{/font}",
    "shakespearean":"Early Modern English",    
    # some other language?
    "thai":"{font=[thai_font]}ภาษาไทย{/font}"
    # emoji language?
    }

define EPILOGUE_TIME = 7

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0
default in_room = False
default inventory = Inventory()
define items = {
    "axe":_("Our axe. Mom and dad used to have contests to see who could chop wood faster. We'd keep score, counting in a different language every time."), 
    "kindling":_("I might need this kindling. Normal books catch fire easily, but these books might have tricks up their sleeves."),
    "flashlight":_("My flashlight. I grabbed it when I ran from the cabin last night. I dropped it when I tripped. It doesn't work anymore."),
    "wood": _("Wood for the fire. Wood. Holz. Hout. Madera. Lignum. A lot of good that does me now. How do you say “Go away” to a…whatever that was?"),
    "blanket":_("We usually snuggle up with this blanket on the couch. Could the blast have thrown it this far?"),
    "doll":_("My parents made this for me when I was little. It was on a shelf in my room, but now it's way out here..."),
    "flint":_("These rocks were from the ritual. They said they were just studying it; they never meant to actually perform the rite!")
}

# Define which ending image goes with which language
define ending_image_map = {
        None:"images/ending_neutral.png",
        "esperanto":"images/ending_dark.png",
        "francais":"images/ending_neutral.png",
        "nihongo":"images/ending_warm.png",
        "deutsch":"images/ending_neutral.png",
        "espanol":"images/ending_dark.png",
        "nederlands":"images/ending_warm.png",
        "hangul":"images/ending_dark.png",
        "shakespearean":"images/ending_warm.png",
        "thai":"images/ending_blaze.png"
}
default end_image = "images/ending_neutral.png"
image white = Solid("#fff")
define wolf_description = _("I wonder if wolves have a language? Probably not. If they did, my parents would have known it.")
define cantlight_msg = _("It looks like nothing happened, like there was no blast. I need to get a fire going in here if I want to destroy those books.")

define snow_enabled = True #False #for web build

init -10 python:
    import collections
    if (not persistent.endings):
        persistent.endings = collections.OrderedDict()    
    if (not persistent.languages):
        persistent.languages = set()
    if (not persistent.times_played):
        persistent.times_played = 0
    renpy.save_persistent()


label start:
    scene cabininterior with fade
    $ _game_menu_screen = "preferences"
    $_confirm_quit = False
    image snow = SnowBlossom("images/snowflake.png", 50, 20, (50,300), fast=True)
    image heavy_snow = SnowBlossom("images/snowflake.png", 200, 20, (100,250), (100, 200), fast=True)
    image ending_image = DynamicImage("[end_image]")

    $ current_room = "CabinInterior"
    $ previous_room = "CabinInterior"

    call choose_language from _call_choose_language
    
    $ renpy.show_screen(current_room + "Screen")
    "...They're gone. Everyone's gone. My body aches, but I'm still alive." id start01
    "The books! They're still here. I should burn them, to make sure those words are never read again. I never thought I'd be one to start burning books, but after what happened..." id start02

    window auto hide

    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")

    return

label lit_fire:
    "My fingers are numb from the cold. I need this fire. I need to feel warm again." id light01
    play sound "<loop 3.0>sfx/light-fire.ogg" loop
    $ end_image = ending_image_map[_preferences.language]
    scene ending_image at zoomoutfromcabin
    "My parents were trying to work out how the ancient words might be pronounced. I never thought they would get it right. We never imagined those words could have...power." id light02
    "When that creature came out, I lost everything. All because of these stupid books. Now my family is lost, and the creature is missing too. What am I supposed to do now?" id light03
    window auto hide
    $ renpy.notify("Saving Progress...")
    if (_preferences.language == None):
        $ persistent.languages.add("english")
    else:
        $ persistent.languages.add(_preferences.language)
    $ persistent.times_played += 1
    $ renpy.save_persistent()    
    $ renpy.pause()

    #if ((persistent.times_played >= 5) and (len(persistent.languages) >= 5)):
    #    call postlude

    $ renpy.full_restart()
    return

screen snowfall():
    zorder 150
    showif (snow_enabled):
        showif (current_room != "CabinInterior"):
            # if (has_fire_items()):
            #     add "heavy_snow"
            # else:
            add "snow"

# this doesn't seem to work?? $ config.overlay_screens.append("snowfall")

label choose_language:
    call screen choose_language_screen()

    return

screen choose_language_screen():
    style_prefix "choice"
    $ book_split = len(renpy.known_languages()) // 2
    $ languages_available = renpy.known_languages()    
    hbox:
        yalign 0.5
        xalign 0.5
        vbox:
            yalign 0.5
            xalign 0.5
            spacing 0
            $ button_name = "images/book_english.png"
            if ("english" in persistent.languages): 
                $ book_image = im.Grayscale(button_name)
            else:
                $ book_image = Image(button_name)
            imagebutton:
                idle book_image
                action [Language(None), Return()]
                at highlight_imagebutton
            for i in range(0,book_split):
                $ lang = list(languages_available)[i]
                $ button_name = "images/book_" + lang + ".png"
                if (lang in persistent.languages): 
                    $ book_image = im.Grayscale(button_name)
                else:
                    $ book_image = Image(button_name)
                imagebutton:
                    idle book_image
                    action [Language(lang), Return()]
                    at highlight_imagebutton
        vbox:
            yalign 0.5
            xalign 0.5
            spacing 0
            for i in range(book_split,len(languages_available)):
                $ lang = list(languages_available)[i]
                $ button_name = "images/book_" + lang + ".png"
                if (lang in persistent.languages): 
                    $ book_image = im.Grayscale(button_name)
                else:
                    $ book_image = Image(button_name)
                imagebutton:
                    idle book_image
                    action [Language(lang), Return()]
                    at highlight_imagebutton           
            if (len(persistent.languages) >= EPILOGUE_TIME):
                if (len(persistent.endings) >= 3):
                    $ book_image = im.Grayscale("images/book_epilogue.png")
                else:
                    $ book_image = "images/book_epilogue.png"
                imagebutton:
                    idle book_image
                    action [Language(None), Call("epilogue")]
                    at highlight_imagebutton 