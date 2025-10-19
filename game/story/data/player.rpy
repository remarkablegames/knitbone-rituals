default player = Player(
    health=10,
    energy=3,
)


init python:
    class Player(RPGCharacter):
        XSIZE = 310
        YSIZE = 170


        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)

            # battle
            self.draw_cards = 3
            self.energy = self.energy_max = kwargs.get("energy", 0)

            # shop
            self.cards_bought = 0
            self.cards_removed = 0
            self.cards_upgraded = 0
            self.shop_cards = 2


        def end_turn(self) -> None:
            """
            End player turn.
            """
            deck.discard_hand()
            renpy.hide_screen("player_end_turn")
            renpy.jump("enemy_turn")
