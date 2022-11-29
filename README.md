# Unicorn HAT HD GIF Displayer
Display animated GIF files on your Unicorn HAT HD!

Supports Unicorn HAT Simulator (https://github.com/jayniz/unicorn-hat-sim)

Based on Pimoroni's show-png.py example: https://github.com/pimoroni/unicorn-hat-hd/blob/1dda39a1074d7676fc0c5f9a44037748d32219db/examples/show-png.py


## Usage
```
./unicorn-gif.py file [brightness]
```
The script automatically assumes a ".gif" extension for the filename, so it is optional.

Brightness is an optional float value from 0-1.

### Usage examples
```
./unicorn-gif.py foo.gif
./unicorn-gif.py foo 0.25
./unicorn-gif.py bar
```
