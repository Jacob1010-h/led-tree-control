---
date: 2023-11-28
categories:
    - Creating the Controller
---

# Iterations

Sense I was going to be writing this code on a ESP32 I assumed that I would be writing in C++, however after several iterations and a bit more research, I landed on micropython, as I already had some experience with python in general.

## Creating the Wrapper

I needed some way to control and edit the colors as well as what index each LED on the strip would need to be set to.

After I created a basic color class as well as a controller that used neopixel to control the color in RGB. I first thought of a way to figure out how to control the LEDs over wifi. Looking back on it I really would've liked to just make a GET request to a website to get the LED's desired color (which is what i eventually did)... but I guess thats what I get for not planning out a project enough.
