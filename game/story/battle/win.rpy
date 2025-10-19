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
    $ loot = max(renpy.random.randint(wins, round(wins * 1.5) + 1), 3)
    $ gold += loot + interest

    play audio "sound/gold.ogg"
    "You earned [loot] + [interest] (interest) gold."

    if wins == 1:
        call reward_card(
            Card(action={"attack": {"value": 1, "blood": True}}, cost=2, image="knife", name="Blood Blade"),
            "{i}Blood Blade{/i} deals extra damage based on your missing health."
        )

        jump reward

    elif wins == 2:
        call reward_card(
            Card(action={"attack": {"value": 3, "stun": True}}, cost=1, image="knife", name="Blunt Blade", uses=5),
            "{i}Blunt Blade{/i} damages and stuns the enemy, but it has a limited number of uses."
        )

    jump shop


label reward_card(card, dialogue):

    show screen card(card)

    "[dialogue]"

    menu:
        "Add this card to your deck?"

        "Yes":
            $ deck.cards.append(card)
            play audio "sound/draw.ogg"

        "No (+[max(wins, 3)] gold)
        {tooltip}Sell card and earn gold":
            $ gold += max(wins, 3)
            play audio "sound/gold.ogg"

    hide screen card

    return
