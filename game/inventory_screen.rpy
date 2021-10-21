screen inventory_screen():
    vbox:            
        yalign 1.0
        xfill True
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]" color "FFFFFF"
        else:
            text " "    
        hbox:        
            spacing 10
            #label "Inventory"
            $ sorted_items = inventory.toList()
            for i in sorted_items:
                imagebutton:
                    sensitive in_room
                    idle "images/" + i["name"]+".png"
                    tooltip items[i["name"]] 
                    action NullAction()
                    at icon_size