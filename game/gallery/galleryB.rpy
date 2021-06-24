## This is galleryB for our LoveInterestB.
## Difference with galleryA:
## screen name, button name, condition and preview images ends in "B" instead of "A"
## (You can name it anyway you want just not the same name as other galleries)

init python:
    g.button("redB")
    g.condition("persistent.redB")
    g.image("CGs/red.jpg")
   
    g.button("blueB")
    g.condition("persistent.blueB")
    g.image("CGs/blue.jpg")

    g.button("purpleB")
    g.condition("persistent.purpleB")
    g.image("CGs/purple.jpg")

    g.button("green_and_orangeB")
    g.condition("persistent.green_orangeB")
    g.image("CGs/green.jpg")
    g.image("CGs/orange.jpg")

    g.transition = dissolve

## This is gallery B
screen galleryB:
    tag menu
    add "customUI/bg_gallery.jpg"
    hbox:
        yalign 0.5
        xalign 0.5
        
        use gallery_navigation
        grid 4 4:
            spacing 25 

            add g.make_button("redB","CGs/small/red_smallB.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("blueB", "CGs/small/blue_smallB.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("purpleB", "CGs/small/purple_smallB.jpg", locked = "CGs/small/locked.jpg")
            add g.make_button("green_and_orangeB", "CGs/small/green_smallB.jpg", locked = "CGs/small/locked.jpg")


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