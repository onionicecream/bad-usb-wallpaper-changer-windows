"""schimbator tapet"""
"""de mec"""
import time

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

delay = 2
delayStroke = 0.001
delayWrite = 0.001
delayAlt = 1
delayCompensatorNetProst = 3

link = "https://i.postimg.cc/85wSVLfD/image-4.png"

# ca sa nu-l grabim
time.sleep(5)

# deschide terminal
keyboard.press(Keycode.GUI, Keycode.SPACE)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.R)
time.sleep(delayStroke)
keyboard_layout.write("Terminal\n", delayWrite)
time.sleep(delay)

# mergi la directorul 'acasa'
keyboard_layout.write("cd\n", delayWrite)
time.sleep(delay)

# da-l jos
keyboard_layout.write("curl -O", delayWrite)
keyboard_layout.write(link, delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)

# pune-l pe susul biroului
keyboard_layout.write("cp image-4.png Desktop/", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)

# pune tapet
keyboard_layout.write("osascript << EOF", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("tell application \"Finder\"", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("set desktop picture to file \"image-4.png\" of desktop")
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("end tell", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("EOF", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)

# curatenia
keyboard_layout.write("rm image-4.png", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("cd Desktop/", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("rm image-4.png", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("cd", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard_layout.write("history -c", delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)
keyboard.press(Keycode.GUI, Keycode.W)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.W)
time.sleep(delay)
keyboard.press(Keycode.GUI, Keycode.Q)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.Q)
time.sleep(delay)
