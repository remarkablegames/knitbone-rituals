label reward:

    $ reward_attack = renpy.random.randint(1, 2 + wins // 2)
    $ reward_health = renpy.random.randint(1, 2 + wins // 2) * 2

    menu:
        "Claim a reward:"

        "Reroll rewards (-[wins // 2] gold)" if gold >= wins // 2 and wins > 1:
            $ gold -= wins // 2
            play audio "sound/gold.ogg"
            jump reward

        "Max health {color=[colors.heal]}+[reward_health]
        {tooltip}Increase max health from [player.health_max] to [player.health_max + reward_health]":
            $ player.health += reward_health
            $ player.health_max += reward_health

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

    jump shop
