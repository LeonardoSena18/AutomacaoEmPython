import pyautogui
import time
pyautogui.alert('dominando o mundo... agora!')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
time.sleep(15)
pyautogui.write('firefox')
time.sleep(15)
pyautogui.press('enter')
time.sleep(15)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
time.sleep(15)
#pyautogui.KEYBOARD_KEYS
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(446, 146)
time.sleep(15)
pyautogui.mouseDown()
pyautogui.moveTo(698, 508)
pyautogui.hotkey('alt', 'tab')
time.sleep(45)
pyautogui.mouseUp()
pyautogui.alert('Dominei!')

