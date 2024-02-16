#Python script to constantly reposition mouse onto the middle of the screen when playing with the Keyboard + Mouse playstyle. Intended for Brawlhalla.

import pyautogui
import threading
import keyboard
import time

# Global feature toggle
freeze_toggle = False

# Toggle function
def mouse_freeze_toggle():
    global freeze_toggle

    freeze_toggle = not freeze_toggle
    print(f"{'Frozen' if freeze_toggle else 'Unfrozen'}")

# Input reading function. Thread 1
def read_input():

    # Hotkeys
    # CHANGE THIS TO WHATEVER YOU LIKE FOR YOUR BIND. 
    # THIS IS THE LEAST CONFLICTING ONE I KNOW SO I DECIDED TO USE IT HERE :)
    keyboard.add_hotkey("ctrl+shift+alt+s", mouse_freeze_toggle)

    keyboard.wait()

# Feature function. Thread 2
def mouse_freeze():
    global freeze_toggle
    x, y = pyautogui.size()

    while True:
        if freeze_toggle == True:
            pyautogui.moveTo(x/2,x/2)
        time.sleep(.01)

def main():
    global freeze_toggle

    print("Freeze utility now ready for use. Press 'CTRL + SHIFT + ALT + S' (by default) to toggle the freeze.")
    print("Please play Brawlhalla on fullscreen so you do not unfocus the game.")
    print("Use 'CTRL + C' to exit the script.")

    # Exception catch for CTRL+C just for feedback purposes.
    # Functionality is in threaded functions above.
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Program exited by user")

# Initializing input and freeze thread
input_thread = threading.Thread(target=read_input, daemon=True)
input_thread.start()

freeze_thread = threading.Thread(target=mouse_freeze, daemon=True)
freeze_thread.start()

if __name__ == "__main__":
    main()