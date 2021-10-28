init python:
    import re

screen inventory_screen():
    vbox:            
        yalign 0.0
        xfill True
        $ tooltip = GetTooltip()

        hbox:        
            spacing 10
            #label "Inventory"
            $ sorted_items = inventory.toList()
            for i in sorted_items:
                if (items[i["name"]]):
                    $ full_desc = items[i["name"]]
                    $ full_desc_translated = renpy.translate_string(full_desc)
                    $ splitted = re.split('(\u\!|\?|\.|。|？|\n)',full_desc_translated)
                    if len(splitted) <= 1:
                        $ desc = splitted[0].strip()
                    else:
                        $ desc = (splitted[0] + splitted[1]).strip()
                    imagebutton:
                        sensitive in_room
                        idle "images/" + i["name"]+".png"
                        tooltip desc
                        action NullAction()
                        at icon_size, highlight_imagebutton

        if tooltip:
            text "[tooltip]" color "FFFFFF"
        else:
            text " "                        