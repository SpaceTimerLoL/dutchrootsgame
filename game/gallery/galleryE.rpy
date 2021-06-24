## This is galleryE for our LoveInterestE.
## Difference with galleryA:
## screen name, button name, condition and preview images ends in "E" instead of "A"
## (You can name it anyway you want just not the same name as other galleries)

init python:
    g.button("redE")
    g.condition("persistent.redE")
    g.image("CGs/red.jpg")
   
    g.button("blueE")
    g.condition("persistent.blueE")
    g.image("CGs/blue.jpg")

    g.button("purpleE")
    g.condition("persistent.purpleE")
    g.image("CGs/purple.jpg")

    g.button("green_and_orangeE")
    g.condition("persistent.green_orangeE")
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")

    g.transition = dissolve

## This is gallery E
screen galleryE:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation
        grid 4 4:
            spacing 25 

            add g.make_button("redE","CGs/small/red_smallE.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("blueE", "CGs/small/blue_smallE.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("purpleE", "CGs/small/purple_smallE.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("green_and_orangeE", "CGs/small/green_smallE.jpg", locked = "CGs/small/locked.jpg")


            # This is using the placeholder from GalleryA.rpy. Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")

            
            # This is using the placeholder from GalleryA.rpy. Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")

            
            # This is using the placeholder from GalleryA.rpy. Placeholder only
            add g.make_button("placeholder","CGs/small/red_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/blue_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/purple_small.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("placeholder", "CGs/small/green_small.jpg", locked = "CGs/small/locked.jpg")