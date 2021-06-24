define z = Character("Zeil")
image CG_red = "CGs/red.jpg"

label start:
    z "You've created a new Ren'Py game."

    show CG_red with fade

    ## This is how you unlock the CG.
    ## This "persistent.red1" is the condition used for "red" button.
    $ persistent.red1 = True
    z "Showing red.png as CG. Beautiful isn't it?"

    ## These are the other persistent. Just uncomment if you want to test them~
    # $ persistent.blue1 = True
    # $ persistent.purple1 = True
    # $ persistent.green_orange1 = True

    ## Use this to test the other galleries.
    ## They have different images for the first row.
    ## everything else is a placeholder.
    "Testing: Do you want to unlock any of the images?"
    menu:
        "unlock GalleryA's first row":
            $ persistent.redA = True
            $ persistent.blueA = True
            $ persistent.purpleA = True
            $ persistent.green_orangeA = True
            "Success"
            
        "unlock GalleryB's first row":
            $ persistent.redB = True
            $ persistent.blueB = True
            $ persistent.purpleB = True
            $ persistent.green_orangeB = True
            "Success"

        "unlock GalleryC's first row":
            $ persistent.redC = True
            $ persistent.blueC = True
            $ persistent.purpleC = True
            $ persistent.green_orangeC = True
            "Success"

        "unlock GalleryD's first row":
            $ persistent.redD = True
            $ persistent.blueD = True
            $ persistent.purpleD = True
            $ persistent.green_orangeD = True
            "Success"

        "unlock GalleryE's first row":
            $ persistent.redE = True
            $ persistent.blueE = True
            $ persistent.purpleE = True
            $ persistent.green_orangeE = True
            "Success"
            
        "unlock Placeholders (row 2-3 of all galery)":
            $ persistent.placeholder = True
            "Success"
    return
