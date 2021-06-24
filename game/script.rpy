define p = Character("mainname", dynamic=True)

label start:
    # scene room
    # with fade
    # $ renpy.music.set_volume(0.1,0,channel="music")
    # play music "audio/wanderlust.ogg"
    # default progress = 0
    $mainname = renpy.input("What's your name?")
    $mainname = mainname.strip()
    call intro
    call christchurch
return