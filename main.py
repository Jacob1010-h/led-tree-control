from Controller import Controller
from Color import Colors
import time

controller = Controller(4, 50)

while True:
    controller.rainbow_cycle(10, 0.01)
    controller.clear()
    time.sleep(1)