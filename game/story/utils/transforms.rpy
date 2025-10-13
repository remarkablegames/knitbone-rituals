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
