# The script of the game goes in this file.

# Variables that should be saved
default current_room = "CabinInterior"
default previous_room = ""
default move_count = 0

# TODO: Inventory

label start:

    $ current_room = "CabinInterior"
    "Every time I come to the cabin, it brings back memories..."

    $ renpy.call_screen(current_room + "Screen")

    return

label ChangeRoom:
    #Update values behind the scenes
    $ update_gamestate()
 
    #Enter the scene
    $ in_room = False
    $ renpy.show_screen(current_room + "Screen")
 
    #React to entrance
    if current_room != previous_room:
        $ check_intro_reactions(current_room)
    $ previous_room = current_room
 
    #Enable scene interactivity
    $ in_room = True
    $ renpy.call_screen(current_room + "Screen")
    return