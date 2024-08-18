import pygetwindow as gw
import pynput.keyboard
import pynput.mouse 
import pyautogui
import datetime
import math
import time
import os



pyautogui.PAUSE = 0

def click(x, y):
    mouse = pynput.mouse.Controller()
    mouse.position = (x, y)
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)

press = False
def on_press(key):
    global press
    global tab_key_pressed
    if key == pynput.keyboard.Key.esc:
        tab_key_pressed = True
        print("> Exit !")
        press = True
        return False
    return True

def window():
    print('='*35, ' ESC -> Exit')
    windows = gw.getAllTitles()
    app = {}
    count = 0
    for i, window in enumerate(windows):
        if window:
            print(f"{count}: {window}")
            app[str(count)] = window
            count += 1
    print('-'*45)
    return app

while True:
    window_id = []
    os.system('cls')
    # number = input('\n> Window number : ')
    number = 1
    app = window()
    if number:
        for cu in range(int(number)):
            window_id.append(input("\n> Enter a number (press Enter to reload the list) : "))
            if len(window_id) == int(number):
                break
        if len(window_id) == int(number):
            break
window_ = []
for b in window_id:
    window_.append(app[b])
with pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
    while True:
        keyboard_listener.wait()
        if press:
            break 
        for window_name in window_:
            if press:
                break
            try:
                window = gw.getWindowsWithTitle(window_name)[0]
            except IndexError:
                print("can't find the window")
                exit()
            center_x = (window.left + window.width // 2) 
            center_y = (window.top + window.height // 2) + 50
            click(center_x, center_y)
            # time.sleep(.5)
            points = 9
            move_steps = 10
            move_distance = 300  
            step_size = move_distance // move_steps
            radius = 100 
            pyautogui.moveTo(center_x + radius, center_y)
            for step in range(move_steps):
                radius = 100  
                center_x = (window.left + (window.width // 2) - (move_distance // 2) + (step * step_size))
                for i in range(points):
                    radius += 1
                    angle = math.radians(i * (360 / points))
                    x = center_x + radius * math.cos(angle)
                    y = center_y + radius * math.sin(angle)
                    pyautogui.moveTo(x, y)
                    # time.sleep(.01)
            for step in range(move_steps, 0, -1):
                radius = 100  
                center_x = (window.left + (window.width // 2) - (move_distance // 2) + (step * step_size))
                for i in range(points):
                    radius += 1
                    angle = math.radians(i * (360 / points))
                    x = center_x + radius * math.cos(angle)
                    y = center_y + radius * math.sin(angle)
                    pyautogui.moveTo(x, y)
                    # time.sleep(.01)
keyboard_listener.stop()