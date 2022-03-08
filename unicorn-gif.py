#!/usr/bin/env python

'''Unicorn HAT HD: GIF Displayer

This piece of software was made for the fantastic Unicorn Hat HD by Pimoroni: https://shop.pimoroni.com/products/unicorn-hat-hd

Based on Pimoroni's show-png.py example: https://github.com/pimoroni/unicorn-hat-hd/blob/1dda39a1074d7676fc0c5f9a44037748d32219db/examples/show-png.py

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License. (https://creativecommons.org/licenses/by-nc-sa/3.0/)

Press Ctrl+C to exit!

'''

import signal
import time
from sys import argv
from sys import exit

try:
    from PIL import Image, ImageSequence
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

try:
    import unicornhathd as unicorn
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

print("\nUnicorn HAT HD: GIF Displayer\n")

try:
    gif = argv[1]
    if gif[-4:] != ".gif":
        gif += ".gif"
except IndexError:
    name = argv[0]
    exit(f"""usage: {name} file [brightness]

   ex: {name} foo.gif
       {name} bar.gif 0.5
       {name} foo 0.25""")

try:
    brightness = float(argv[2])
except IndexError:
    brightness = (0.2)

unicorn.rotation(0)
unicorn.brightness(brightness)

width, height = unicorn.get_shape()

print(f"Reading and processing frames from {gif}...")
try:
    img = Image.open(gif)
    frames = [frame.copy().convert("RGBA") for frame in ImageSequence.Iterator(img)]
except FireNotFoundError:
    exit(f"{gif} not found.")

print("Playing animation...\nPress Ctrl+C to stop.")

try:
    while True:
        for im in frames:
            valid = False
            for x in range(width):
                for y in range(height):
                    pixel = im.getpixel((y, x))
                    r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                    if r or g or b:
                        valid = True
                    unicorn.set_pixel(x, y, r, g, b)
            if valid:
                unicorn.show()
                time.sleep((im.info["duration"] / 1000) - 0.02)
except KeyboardInterrupt:
    unicorn.off()
    print("\nStopped.")
