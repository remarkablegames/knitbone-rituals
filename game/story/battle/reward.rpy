label reward:

    if not rewards:
        jump shop

    $ reward_attack = renpy.random.randint(1, 2 + wins // 2)
    $ reward_heal = renpy.random.randint(1, 3 + wins // 2) * 2

    menu:
        "Claim your reward (remaining: [rewards]):"

        "Reroll rewards (-$[wins // 2])" if gold >= wins // 2 and wins > 1:
            $ gold -= wins // 2
            jump reward

        "Get a card
        {tooltip}Add 1 card to your deck":
            $ rewards -= 1
            $ cards = Card.generate(player.shop_cards)
            call screen card_add(cards)

        "Max health {color=[colors.heal]}+[reward_heal]
        {tooltip}Increase max health from [player.health_max] to [player.health_max + reward_heal]":
            $ player.health += reward_heal
            $ player.health_max += reward_heal

        "Max energy {color=[colors.energy]}+1
        {tooltip}Increase max energy from [player.energy_max] to [player.energy_max + 1]" if wins > 4 and renpy.random.random() < 0.1:
            $ player.energy_max += 1

        "Draw cards {color=[colors.gold]}+1
        {tooltip}Increase draw cards to [player.draw_cards + 1] and shop cards to [player.shop_cards + 1]" if wins > 2 and renpy.random.random() < 0.1:
            $ player.draw_cards += 1
            $ player.shop_cards += 1

        "Recover all health" if player.health < player.health_max:
            $ player.health = player.health_max

        "Skip":
            pass

    $ rewards -= 1

    jump reward
