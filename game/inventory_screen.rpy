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
            #label "Inventory"
            for i in inventory:
                imagebutton:
                    idle im.FactorScale(i+".png", 0.25)
                    tooltip items[i] 
                    action NullAction()