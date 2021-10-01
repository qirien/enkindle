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