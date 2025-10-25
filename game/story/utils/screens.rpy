init python:
    TEXT_STYLE = "{size=32}{k=-2}"


screen stat(name, current, max):
    text "[TEXT_STYLE][name] [current]/[max]"
    bar value AnimatedValue(current, max):
        xsize 300


screen player_gold():
    frame:
        background Solid((0, 0, 0, 100))
        text "[TEXT_STYLE]{color=[colors.gold]}Gold: [gold]"
        xpos (40 if renpy.variant("web") else 0)


screen player_stats():
    vbox:
        yalign 1.0
        use player_deck(0, 0)
        frame:
            vbox:
                use stat("HP", player.health, player.health_max)
                null height 15
                use stat("Energy", player.energy, player.energy_max)


screen player_end_turn():
    frame:
        padding (10, 10)
        xalign 1.0
        yalign 1.0

        textbutton "End Turn":
            action Function(player.end_turn)


screen player_deck(xalign_pos, yalign_pos):
    frame:
        padding (10, 10)
        textbutton ("Draw Pile" if levels.battle else "Deck"):
            action Show("draw_pile")
        xalign xalign_pos
        yalign yalign_pos


screen tooltip():
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                background Solid((255, 255, 255, 225))
                text "[TEXT_STYLE][tooltip!i]" color "#000"
                xalign 0.5


screen enemy_stats(enemy, xalign_pos):
    frame:
        background Solid((0, 0, 0, 100))
        xalign xalign_pos

        vbox:
            use stat("HP", enemy.health, enemy.health_max)

            button:
                action NullAction()
                text "[TEXT_STYLE][enemy.name][enemy.label()!i]"
                tooltip (enemy.say() or "...")

    use tooltip


screen enemy_stats0(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen enemy_stats1(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen enemy_stats2(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen enemy_stats3(enemy, xalign_pos):
    use enemy_stats(enemy, xalign_pos)


screen draw_pile():

    dismiss action Hide("draw_pile")

    frame:
        modal True
        padding (50, 50)
        xalign 0.5 yalign 0.5
        has vbox

        viewport:
            scrollbars "horizontal"
            ysize 450

            hbox:
                spacing 25
                for card in deck.draw_pile if levels.battle else deck.cards:
                    use card_frame(card)

        null height 50

        frame:
            xalign 0.5
            textbutton "Close":
                action Hide("draw_pile")


screen card_frame(card, draggable=None):
    frame:
        background Frame(card.background)
        add card.image:
            xpos -5 ypos -5
            xysize card.WIDTH, card.HEIGHT
        label card.label_name():
            xpos 48
            ypos (5 if " " in card.name else 19)
        label card.label_cost():
            xpos 7
            ypos 15
        label card.label_description():
            xalign 0
            ypos 220
            padding (10, 0)
        xysize card.WIDTH, card.HEIGHT

        if draggable:
            mousearea:
                area (0, 0, card.OFFSET, card.HEIGHT)
                hovered [
                    Queue(MUSIC_CHANNEL_UI, "ui/mouserelease1.ogg"),
                    Function(draggable.top),
                ]


screen card(card, xalign_pos=0.5, yalign_pos=0.5):
    vbox:
        xalign xalign_pos
        yalign yalign_pos
        use card_frame(card)
