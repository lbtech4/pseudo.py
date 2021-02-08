import pyautogui
import os, time
def mic():
    pyautogui.moveTo(881, 974); pyautogui.click()
def cam():
    pyautogui.moveTo(1046, 966); pyautogui.click()
def leave():
    pyautogui.moveTo(969, 953); pyautogui.click()
def connectToMeet(url):
    os.system("start " + url)
    time.sleep(1)
    pyautogui.moveTo(1354, 591); pyautogui.click(); time.sleep(1); pyautogui.click()
def sendChat(message):
    pyautogui.moveTo(1621, 122); pyautogui.click(); time.sleep(1); pyautogui.typewrite(message); pyautogui.press("enter"); pyautogui.press("esc")
def presentScreen():
    pyautogui.moveTo(1731, 977); pyautogui.click(); pyautogui.moveTo(1692, 762); time.sleep(1); pyautogui.click(); time.sleep(2); pyautogui.press("tab"); pyautogui.press("enter")
def selectScreen(urlorprogram):
    os.system("start " + urlorprogram)
def stopShare():
    pyautogui.click(1094, 999)
    
    
    
