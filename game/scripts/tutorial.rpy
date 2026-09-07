label tutorial:

    stop dialogue

    show ryohei seated neutral with dissolve

    show screen player_gold

    ryohei "Your gold is on the top-left."

    show screen player_stats

    ryohei seated look "Your stats are on the bottom-left."
    ryohei "When {b}HP{/b} reaches 0, you lose."
    ryohei seated neutral "{b}Energy{/b} allows you to play cards."
    ryohei seated serious "Click {b}Deck{/b} to view your cards."

    $ card = Card(action={"attack": {"value": 3}}, cost=1, image="knife", name="Knife")
    show screen card(card)

    ryohei seated neutral "The {b}Energy{/b} cost of the card is on the top-left."
    ryohei seated crazy "The action is written in the card description."

    hide screen card

    hide ryohei with Dissolve(1)

    $ levels.start()

    ryohei "The enemy’s stats are above."
    ryohei "Hover over the enemy’s name to see its next move."

    $ deck.draw_cards(player.draw_cards)

    ryohei "You draw cards at the start of your turn."
    ryohei "Drag the card to the {i}enemy{/i} or to your {i}stats{/i} to play it."

    show screen player_end_tutorial
    call screen player_hand
