transform idle:
    subpixel True
    choice:
        pause 0.3
        easein 2.0 yzoom 0.98
    choice:
        pause 0.6
        easein 2.0 yzoom 0.97
    choice:
        pause 0.9
        easein 2.0 yzoom 0.96
    easein 2.0 yzoom 1.0
    repeat


transform idle_zoom:
    linear 0.15 zoom 1.0


transform position(xalign_position=0.5):
    xalign xalign_position
    yalign Enemies.YALIGN


transform shake:
    linear 0.05 xoffset -12
    linear 0.05 xoffset 12
    linear 0.05 xoffset -6
    linear 0.05 xoffset 6
    linear 0.05 xoffset 0


transform slight_shake:
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -3
    linear 0.05 xoffset 3
    linear 0.05 xoffset 0


transform speak_zoom:
    linear 0.15 zoom 1.025


transform zoomin:
    truecenter
    zoom 1
    linear 3 zoom 1.1


transform zoomout:
    truecenter
    zoom 1.1
    linear 3 zoom 1.0
