<p align="center">
  <img src="https://raw.githubusercontent.com/remarkablegames/knitbone-card-game/master/game/gui/window_icon.png" alt="KnitBone Card Game">
</p>

# KnitBone Card Game

![release](https://img.shields.io/github/v/release/remarkablegames/knitbone-card-game)
[![build](https://github.com/remarkablegames/knitbone-card-game/actions/workflows/build.yml/badge.svg)](https://github.com/remarkablegames/knitbone-card-game/actions/workflows/build.yml)
[![lint](https://github.com/remarkablegames/knitbone-card-game/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablegames/knitbone-card-game/actions/workflows/lint.yml)

🦴 KnitBone card game.

Play the game on:

- [remarkablegames](https://remarkablegames.org/knitbone-card-game)

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
git clone https://github.com/remarkablegames/knitbone-card-game.git
cd knitbone-card-game
```

Replace the assets:

- [ ] `game/gui/main_menu.png`
- [ ] `game/gui/window_icon.png`
- [ ] `web-icon.png`
- [ ] `web-presplash.webp`

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
