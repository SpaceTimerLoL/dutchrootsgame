##--Game Intro--##
label intro:
    "[mainname], my dearest nephew,"
    "I have been in Amsterdam for a week now, still in pursuit of the secret artifact."
    "The myths are real; The Dutch built a pure diamond artifact for every major city they lived in or colonised."
    "However, I still could not locate the one in Amsterdam."
    "The good news is there is another one hidden in Malacca."
    "Before they left Malacca, they tasked a high ranking V.O.C administrator to keep it out of sight."
    "Many had tried to uncover the treasure, but they didn't know the key to finding it."
    "It turns out that J.B. Westerhout was the administrator who hid the treasure."
    "And from the secret archives I've found here, he had placed clues in his own plaque in Christchurch at the left of the altar."
    'The search in Amsterdam has seem to reach a dead end.'
    "The treasure must be found by us or else my life might be in danger."
    "My boss may not tolerate my failure and get rid of me."
    "I must stay in Amsterdam at the moment to avoid suspicion."
    "So, I'm writing to you to find the treasure in Malacca."
    "Starting from Christchurch, I'm sure you can piece the puzzle together with all the detective skills I taught you."
    "The treasure is crucial to my survival and perhaps yours too, as your livelihood depends on my allowance."
    "Our fate in your hands. Love, Uncle Tom."
    "P.S. I pieced together an exposition of the Old Dutch Fort of Malacca to guide you in your treasure hunt."
    "However high the stakes are, enjoy the adventure. These experiences will be the memories you cherish."
    p "The exposition seems important. Best to look through it."
    call fort_history
    return

##--Old Dutch Malacca fort history--##
label fort_history:
    "Insert exposition here."
    call christchurch
    $ renpy.pause(hard=True)
    return

##--Game Tutorial--##
label tutorial:
    return

##--Player now in Christchurch-##
label christchurch:
    scene christchurch_bg
    p "Uncle Tom told me to look at the left of the altar..."
    $ renpy.pause(hard=True)
    return

label plaque:
    p "There seem to be a note within this plaque..."
    p "This note is for their descendants; I'm not supposed to read this. But for my uncle...,I had to."
    return

label the_last_supper:
    return

label the_last_supper_riddle:
    p "Clever mechanism to hide the codex!"
    p "Now I need to turn map the Westerhouts' route to Malacca."
    call codex_stadthuys
    return

label codex_stadthuys:
    return

label stadthuys_guards:
    return

label shopping:
    return

label cooking:
    return

label jail:
    return

label st_paul:
    return

label naning:
    return

label side_quest:
    return

label cake:
    return

label spirit:
    return

label boss_fight:
    return




