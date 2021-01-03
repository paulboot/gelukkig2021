def on_bluetooth_connected():
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . # . # .
        . . # . .
        . # . # .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . . . .
        . . . . .
        """)
    basic.pause(200)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(200)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

basic.show_leds("""
    # . . . #
    # . . . .
    # # # . .
    # . # . .
    # # # . .
    """)
bluetooth.start_led_service()

