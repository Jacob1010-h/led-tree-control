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
import net

do_connect(
    net.NAME,
    net.PASS
)

import webrepl

webrepl.start()

# exec(open("main.py").read())
