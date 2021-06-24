## This is galleryC for our LoveInterestC.
## Difference with galleryA:
## screen name, button name, condition and preview images ends in "C" instead of "A"
## (You can name it anyway you want just not the same name as other galleries)

init python:
    g.button("redC")
    g.condition("persistent.redC")
    g.image("CGs/red.jpg")
   
    g.button("blueC")
    g.condition("persistent.blueC")
    g.image("CGs/blue.jpg")

    g.button("purpleC")
    g.condition("persistent.purpleC")
    g.image("CGs/purple.jpg")

    g.button("green_and_orangeC")
    g.condition("persistent.green_orangeC")
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")

    g.transition = dissolve

## This is gallery C
screen galleryC:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation
        grid 4 4:
            spacing 25 

            add g.make_button("redC","CGs/small/red_smallC.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("blueC", "CGs/small/blue_smallC.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("purpleC", "CGs/small/purple_smallC.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("green_and_orangeC", "CGs/small/green_smallC.jpg", locked = "CGs/small/locked.jpg")


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