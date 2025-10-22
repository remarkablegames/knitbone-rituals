<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/knitbone-rituals/master/game/gui/window_icon.png" alt="KnitBone : Rituals">
</p>

# KnitBone: Rituals

![release](https://img.shields.io/github/v/release/remarkablegames/knitbone-rituals)
[![build](https://github.com/remarkablegames/knitbone-rituals/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/knitbone-rituals/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/knitbone-rituals/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/knitbone-rituals/actions/workflows/lint.yml)

👁️ **KnitBone: Rituals** is a roguelike deckbuilding card game where you battle entities.

> _Knitbone: Rituals_ is a standalone spinoff of the original visual novel, [KnitBone](https://remarkablegames.itch.io/knitbone).
>
> This time, Ryohei drags you into another of his “guided rituals”... and before you know it, you’re pulled straight into a TV, trapped in a surreal world of cards, combat, and strange symbols.

Play the game on:

- [itch.io](https://remarkablegames.itch.io/knitbone-rituals)
- [remarkablegames](https://remarkablegames.org/knitbone-rituals)

Or download:

- [Windows](https://github.com/remarkablegames/knitbone-rituals/releases/latest/download/win.zip)
- [Mac](https://github.com/remarkablegames/knitbone-rituals/releases/latest/download/mac.zip)
- [Linux](https://github.com/remarkablegames/knitbone-rituals/releases/latest/download/pc.zip)

## How To Play

- Drag your card to the enemy.
- Hover over the enemy's name to see their next move.
- Press **End Turn** when out of **Energy**.
- Defeat all the enemies while staying alive!

## Credits

### Art

- [aespipu](https://aespipu.itch.io/)

### Development

- [remarkablemark](https://github.com/remarkablemark)

### Music

- [seamus](https://seemvevo.itch.io/)

### Audio

- [Kenney Interface Sounds](https://kenney.nl/assets/interface-sounds)
- Pixabay
  - [Bag of Gold](https://pixabay.com/sound-effects/bag-of-gold-28095/)
  - [Heal Up](https://pixabay.com/sound-effects/heal-up-39285/)
  - [Health Pickup](https://pixabay.com/sound-effects/health-pickup-6860/)
  - [Heartbeat 01 - BRVHRTZ](https://pixabay.com/sound-effects/heartbeat-01-brvhrtz-225058/)
  - [Knife Stab Sound Effect](https://pixabay.com/sound-effects/knife-stab-sound-effect-36354/)
  - [Punch Sound Effects](https://pixabay.com/sound-effects/punch-sound-effects-28649/)
  - [Soothing White Noise](https://pixabay.com/sound-effects/soothing-white-noise-323619/)
  - [card mixing](https://pixabay.com/sound-effects/card-mixing-48088/)

## Prerequisites

Download [Ren'Py SDK](https://www.renpy.org/latest.html):

```sh
git clone https://github.com/remarkablegames/renpy-sdk.git
```

Symlink `renpy`:

```sh
sudo ln -sf "$(realpath renpy-sdk/renpy.sh)" /usr/local/bin/renpy
```

Check the version:

```sh
renpy --version
```

## Install

Clone the repository to the `Projects Directory`:

```sh
git clone https://github.com/remarkablegames/knitbone-rituals.git
cd knitbone-rituals
```

## Run

Launch the project:

```sh
renpy .
```

Or open the `Ren'Py Launcher`:

```sh
renpy
```

Press `Shift`+`R` to reload the game.

Press `Shift`+`D` to open the developer menu.

## Cache

Clear the cache:

```sh
find game -name "*.rpyc" -delete
```

Or open `Ren'Py Launcher` > `Force Recompile`:

```sh
renpy
```

## Lint

Lint the game:

```sh
renpy game lint
```
