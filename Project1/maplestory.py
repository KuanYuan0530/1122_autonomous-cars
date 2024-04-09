import time
import pyautogui
import pydirectinput

def press_key(key, duration):
    pyautogui.press(key)
    time.sleep(duration)

def spress_key(key, duration):
    pydirectinput.press(key)
    time.sleep(duration)

if __name__ == "__main__":
    # 在這裡換成你想要自動操作的應用程式標題
    window_title = 'MapleStory'
    
    while True:
        try:
            #windows = pyautogui.getWindowsWithTitle(window_title)
            windows = pyautogui.getWindowsWithTitle(window_title)
            print(windows)
            if windows:
                print(windows[1])
                window = windows[1]
                window.activate()
            else:
                print("找不到指定的視窗:", window_title)
            time.sleep(5)
            # 按下Page Up鍵
            spress_key('left', 3)  # 每隔十分鐘按一次Page Up鍵
            #print("left")
            # 按下Ins鍵
            #press_key('ins', 30 * 60)     # 每隔三十分鐘按一次Ins鍵
        except KeyboardInterrupt:
            break