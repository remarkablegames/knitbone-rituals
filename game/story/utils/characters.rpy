init python:
    MUSIC_CHANNEL_DIALOGUE="dialogue"

    renpy.music.register_channel(MUSIC_CHANNEL_DIALOGUE, "voice", loop=True, file_prefix="voice/", file_suffix=".ogg")


    def apply_zoom(character_prefix, zoom_type) -> None:
        for tag in renpy.get_showing_tags():
            if tag.startswith(character_prefix):
                renpy.show(tag, at_list=[zoom_type])


    def narrator_callback(event, interact=True, **kwargs) -> None:
        if event == "show_done":
            renpy.music.play("narrator", channel=MUSIC_CHANNEL_DIALOGUE, relative_volume=0.3)
        elif event == "slow_done":
            renpy.music.stop(channel=MUSIC_CHANNEL_DIALOGUE, fadeout=0.2)


    def ryohei_callback(event, interact=True, **kwargs) -> None:
        if event == "begin":
            apply_zoom("ryohei", speak_zoom)
        elif event == "end":
            apply_zoom("ryohei", idle_zoom)
        if event == "show_done":
            renpy.music.play("narrator", channel=MUSIC_CHANNEL_DIALOGUE, relative_volume=0.3)
        elif event == "slow_done":
            renpy.music.stop(channel=MUSIC_CHANNEL_DIALOGUE, fadeout=0.2)


    def dismiss_callback() -> bool:
        renpy.play("ui/click.ogg")
        return True

    config.say_allow_dismiss = dismiss_callback


define narrator = Character(None, callback=narrator_callback)
define ryohei = Character("Ryohei", callback=ryohei_callback, image="ryohei", what_color="#272e3f", who_color="#6b7c95", who_outlines=[(3, "#303133", 0, 0)])
