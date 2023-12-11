# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)
def do_connect(ssid, pwd):
    import network

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())


# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)

# Attempt to connect to WiFi network
import os
from dotenv import load_dotenv

load_dotenv("./net.env")

do_connect(
    os.getenv("NAME"),
    os.getenv("PASSWORD")
)

import webrepl

webrepl.start()

exec(open("main.py").read())
