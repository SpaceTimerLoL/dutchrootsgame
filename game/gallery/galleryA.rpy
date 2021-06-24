init python:
    ## This will create our gallery. ONLY DO THIS ONCE.
    ## Doing this more than once will erase, the created buttons.
    g = Gallery()

    ## Created a button named red
    g.button("redA")
    ## The CGs are locked by adding the g.condition("flagName")
    g.condition("persistent.redA")
    ## Then in your script.rpy or any label, you can code "$ flagName = True" to unlock the image with that condition
    ## To reset your data, you have to click "Delete Persistent" from the Ren'Py Launcher

    ## if the CG is unlocked, and the user clicks the red button, the red.jpg will show.
    g.image("CGs/red.jpg")
   

    ## Created a button named blue (same as red)
    g.button("blueA")
    g.condition("persistent.blueA")
    g.image("CGs/blue.jpg")


    ## Created a button named purple (same as red)
    g.button("purpleA")
    g.condition("persistent.purpleA")
    g.image("CGs/purple.jpg")


    ## Created a button named green_and_orange
    g.button("green_and_orangeA")
    g.condition("persistent.green_orangeA")
    ## This will show two images, green and orange.
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")

    
    ## The transition used when switching images.
    g.transition = dissolve

    # This is used for row 2, 3 and 4 of gallery A,B,C,D and E.
    g.button("placeholder")
    g.condition("persistent.placeholder")
    g.image("CGs/red.jpg")
    g.image("CGs/blue.jpg")
    g.image("CGs/purple.jpg")
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")


screen galleryA:
    tag menu
    # This is the background image
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        #This will show the screen gallery_navigation from gallery_navigation.rpy
        use gallery_navigation

        
        # This is a grid containing 2 columns and 2 rows.
        grid 4 4:
            spacing 25 # This is the same as using "xspacing 25 yspacing 25"

            ## Row 1
            ## This will add a button that you made.
            ## "redA" is the button name.
            ## "CGs/small/red_smallA.jpg" is the preview image that will show on the button.
            ## "CGs/small/locked.jpg" is the preview image that will show when the button is locked.
            add g.make_button("redA","CGs/small/red_smallA.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("blueA", "CGs/small/blue_smallA.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("purpleA", "CGs/small/purple_smallA.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("green_and_orangeA", "CGs/small/green_smallA.jpg", locked = "CGs/small/locked.jpg")


            ## Row 2: Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")

            
            ## Row 3: Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")

            
            ## Row 4: Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")