import time
from bluezero import microbit

ADAPTER_ADDR = 'B8:27:EB:AB:2E:4D'
ubits = []

ubits.append(microbit.Microbit(adapter_addr=ADAPTER_ADDR,
                         device_addr='D0:29:D7:1A:E2:28',
                         accelerometer_service=False,
                         button_service=False,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False))

ubits.append(microbit.Microbit(adapter_addr=ADAPTER_ADDR,
                         device_addr='D8:16:97:22:FE:DA',
                         accelerometer_service=False,
                         button_service=False,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False))


def display(message):

    print("Message: {0}".format(message))
    for ubit in ubits:
        print("Connecting ubit")
        ubit.connect()
        ubit.text = message
        ubit.disconnect()
        print("Disconnected ubit")
    time.sleep(5)

    # print("Connecting ubit")
    # time.sleep(2)
    # print("Disconnected ubit")
