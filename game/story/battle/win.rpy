default gold = 0
default loot = 0
default interest = 0
default wins = 0


init python:
    from math import ceil


label win:

    $ levels.end()

    hide screen player_end_turn
    hide screen player_stats

    hide screen enemy_stats0
    hide screen enemy_stats1
    hide screen enemy_stats2
    hide screen enemy_stats3

    show screen player_gold

    "You survived the encounter."

    $ wins += 1
    $ interest = ceil(gold * 0.4)
    $ loot = renpy.random.randint(wins, round(wins * 1.5) + 1)
    $ gold += loot + interest

    "You earned [loot] + [interest] (interest) gold."

    if wins == 1:
        jump reward

    elif wins == 2:
        $ card = Card(action={"attack": {"value": 3, "stun": True}}, cost=1, image="knife", name="Blunt Blade", uses=5)
        call reward_card(card)

    jump shop


label reward_card(card):

    show screen card(card)

    "Add this card to your deck?"

    menu:

        "Yes":
            $ deck.cards.append(card)
            play audio "sound/draw.ogg"

        "No (+[max(wins, 3)] gold)
        {tooltip}Sell card and earn gold":
            $ gold += max(wins, 3)
            # play audio "sound/gold.ogg" volume 0.5

    hide screen card

    return
