label start:

    $ quick_menu = False # hide bottom menu

    stop music fadeout .5

    show bg studio1 with dissolve

    $ levels.restart()

    menu:
        "What do you want to do?"

        "Play":
            jump battle

        "Tutorial":
            jump tutorial
