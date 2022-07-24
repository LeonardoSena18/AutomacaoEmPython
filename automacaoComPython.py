import pyautogui
import time
pyautogui.alert('Programa iniciando execução de tarefa!')
pyautogui.PAUSE = 0.5 #tempo de execução entre cada linha de código
pyautogui.press('winleft')
time.sleep(15)
pyautogui.write('firefox')
time.sleep(15)
pyautogui.press('enter')
time.sleep(15)
pyautogui.write('https://drive.google.com/drive/my-drive')
pyautogui.press('enter')
time.sleep(15)
#pyautogui.KEYBOARD_KEYS para verificar a nomenclatura das teclas
pyautogui.hotkey('winleft', 'd') #codigo para digitação de teclas simuntâneas
pyautogui.moveTo(446, 146) #move o mouse para essas coordenadas x, y
time.sleep(15)
pyautogui.mouseDown() #clicar e manter mouse pressionado
pyautogui.moveTo(698, 508)
pyautogui.hotkey('alt', 'tab')
time.sleep(45)
pyautogui.mouseUp() #soltar mouse
pyautogui.alert('Execução de tarefa finalizado!')
