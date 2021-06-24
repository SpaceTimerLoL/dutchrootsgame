## This is galleryD for our LoveInterestD.
## Difference with galleryA:
## screen name, button name, condition and preview images ends in "D" instead of "A"
## (You can name it anyway you want just not the same name as other galleries)

init python:
    g.button("redD")
    g.condition("persistent.redD")
    g.image("CGs/red.jpg")
   
    g.button("blueD")
    g.condition("persistent.blueD")
    g.image("CGs/blue.jpg")

    g.button("purpleD")
    g.condition("persistent.purpleD")
    g.image("CGs/purple.jpg")

    g.button("green_and_orangeD")
    g.condition("persistent.green_orangeD")
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")

    g.transition = dissolve

## This is gallery D
screen galleryD:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation
        grid 4 4:
            spacing 25 

            add g.make_button("redD","CGs/small/red_smallD.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("blueD", "CGs/small/blue_smallD.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("purpleD", "CGs/small/purple_smallD.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("green_and_orangeD", "CGs/small/green_smallD.jpg", locked = "CGs/small/locked.jpg")


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