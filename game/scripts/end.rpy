label end:

    hide screen player_end_turn
    hide screen player_stats
    hide screen player_gold

    hide screen enemy_stats0
    hide screen enemy_stats1
    hide screen enemy_stats2
    hide screen enemy_stats3

    pause 1

    play music "music/theme5.ogg" volume 0.7

    scene bg hallway at zoomout
    with fade

    "You survived the ritual...{w=.3} and escaped alive."

    scene black with Dissolve(1)

    "Wins: [wins]"

    stop music fadeout 1

    return
