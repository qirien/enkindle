# This room code is based off of West of Entropy's 
# Point and Click game structure,
#  https://westofentropy.wordpress.com/2020/10/29/renpy-point-and-click-tutorial-1-structure/

# CHANGE ROOM
# Whenever you transition to a new screen, it calls this label. 
# This allows you to add something when you enter a room
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
    window auto hide
    $ renpy.call_screen(current_room + "Screen")
    return

# Python Code for Rooms
init python:
    def update_gamestate():
        global move_count
        newcount = move_count + 1
        SetVariable("move_count", newcount)()
        return
             
    def check_intro_reactions(room):
        enter_room_label = "Enter" + room
        has_intro = renpy.has_label(enter_room_label)
        if has_intro:
            renpy.call(enter_room_label)
        return