def foreverLoop():
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(500)
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
    basic.pause(500)

basic.forever(foreverLoop)