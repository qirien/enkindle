screen inventory_screen():
    vbox:            
        yalign 1.0
        xfill True
        $ tooltip = GetTooltip()
        if tooltip:
            text "[tooltip]"
        else:
            text " "    
        hbox:        
            spacing 10
            label "Inventory"
            for i in inventory:
                    textbutton i tooltip items[i] action NullAction()
                    # TODO: when you click/mouseover, display description
