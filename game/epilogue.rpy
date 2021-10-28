label epilogue:
    scene cabininterior with fade
    "I read through the books they left behind. The stories they contained were strange, but mundane."
    "Still, as I read them I could feel my mind opening. Something was forming there. Like a thought I couldn’t recall, or a memory full of emotion and blurs."
    "Something was whispering inside my mind. It wanted to be let out. It itched and burned under my skull. I had to do something..."
    menu:
        "What should I do?"
        "Burn the books":
            "Whatever is happening, it’s too dangerous. I have to destroy these books and hope it will stop whatever is here. Perhaps now I can leave."
            "As I set the books on fire, I can feel it fading away in my mind. Maybe it’ll stay gone this time."
            "…This fire won’t be enough. I’ll have to make sure it’s gone."
            scene ending_blaze at zoomoutfromcabin with fade 

            "It’s the only way to be sure…"
            $ persistent.endings["burn"] = None
            $ renpy.save_persistent()
        "Speak the words":
            scene title02 with fade
            "Yes, this is good. This is right."
            "I see now that I was the egg. The eggshell. This was my purpose."
            scene title03 with dissolve
            "I can remember what happened when my parents spoke quickly and excitedly. It won’t happen again. I take my time."
            scene title04 with dissolve
            "The words slither out of my mouth, and so does he. My mind feels wet– wet and blank."
            "He is free now. He has arrived."
            scene demon_eyes with dissolve
            "Our era has come to an end."
            "Now it is time for his."
            $ persistent.endings["release"] = None
            $ renpy.save_persistent()
        "Banish the demon" if (len(persistent.languages) >= (len(renpy.known_languages()) + 1)):
            scene title03 with fade
            "???" "Yes, this is good. This is right."
            "???" "You are an egg. An eggshell. Being an eggshell was your purpose in life."
            "???" "Remember the words, speak them slowly."
            "I can feel the voice encouraging me in my mind. I can feel my body compelled to obey."
            scene title04 with dissolve
            "So I speak. The words slither out of my mouth, and along with them drops the body of…"
            "What. Is. That."
            scene demon_eyes with dissolve            
            "A gloopy lump splats onto the ground. A form no larger than my foot with the head and neck of a newborn chicken and the malformed body of a human."
            "Tiny arms and legs end in impossibly small hands with long fragile fingers. The head is easily the size of the rest of the body and the entire form is coated in some black substance–like thick black paint."
            "As this mind demon drops to the floor, my mind is awakened completely. With each book a language. With each language, a new perspective–a new meaning."
            "I can see more clearly than ever before. This pathetic creature on the floor. It whispered into my mind. It pretended it was powerful and tricked me into agreeing."
            "I see it for what it is now. A weak, crawling, grasping whisper that tried to creep into my mind and breed."
            "I know it must be destroyed. I have to tell this foul thing to leave and never come back. I'll choose my words carefully..."
            menu banish_menu:
                "Begone":
                    menu:      
                        "Begone..."                  
                        "{font=[japanese_font]}かわいい{/font}":
                            jump banish_wrong
                        "{font=[japanese_font]}元気{/font}":
                            jump banish_wrong
                        "{font=[japanese_font]}わるい{/font}":
                            menu:
                                "Begone, {font=[japanese_font]}わるい{/font}..."
                                "{font=[thai_font]}ยักษ์{/font}":
                                    menu:
                                        "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! "
                                        "sap":
                                            jump banish_wrong
                                        "nooit":
                                            menu:
                                                "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! Nooit..."
                                                "bonvolu":
                                                    jump banish_wrong
                                                "aŭtuno":
                                                    jump banish_wrong
                                                "hantu":
                                                    menu:
                                                        "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! Nooit hantu..."
                                                        "ce":
                                                            menu:
                                                                "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! Nooit hantu ce..."
                                                                "gato":
                                                                    jump banish_wrong
                                                                "mundo":                                                                   
                                                                    menu:
                                                                        "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! Nooit hantu ce mundo..."
                                                                        "{font=[korean_font]}더 이상{/font}":
                                                                            "Begone, {font=[japanese_font]}わるい{/font} {font=[thai_font]}ยักษ์{/font}! Nooit hantu ce mundo {font=[korean_font]}더 이상{/font}!"
                                                                        "{font=[korean_font]}오후{/font}":
                                                                            jump banish_wrong
                                                                        "{font=[korean_font]}해{/font}":
                                                                            jump banish_wrong

                                                                "lindo":
                                                                    jump banish_wrong
                                                        "nuit":
                                                            jump banish_wrong
                                                        "fromage":
                                                            jump banish_wrong
                                        "hoed":
                                            jump banish_wrong

                                "{font=[thai_font]}สอง{/font}":
                                    jump banish_wrong
                                "{font=[thai_font]}น้ำ{/font}":
                                    jump banish_wrong
                "Congealment":
                    jump banish_wrong                    
                "Mockable":
                    jump banish_wrong
            "These new words pour from my mouth, light and bright, strong and clear."
            scene white with fade
            "With a screech, the dripping creature on the floor flinches, limbs burning to ash as it tries to move away."
            scene cabininterior with fade
            "After just a few seconds, it vanishes completely. I can feel it disappear: not just the body, but the whisper. It’s gone."
            scene ending_warm at zoomoutfromcabin with fade
            "I sigh, the strength leaving my legs causing me to collapse in relief. I wasn’t able to save my family, but I hoped now they could rest in peace."
            $ persistent.endings["banish"] = None
            $ renpy.save_persistent()
    $ renpy.full_restart()
    return

label banish_wrong:
    "That didn't feel right. I have to tell this foul creature to leave and never return. I need to start over."
    jump banish_menu