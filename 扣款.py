# _*_ coding:utf-8 _*_
# 开发团队：宣建祥
# 开发人员：xuanjianxiang
# 开发时间：2022/4/29 12:30
# 文件名称：扣款.py
# 开发工具：PyCharm
import time
import pyautogui
pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True
i = 0
while i<200:
    pyautogui.moveTo(95,50)
    pyautogui.leftClick()
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.moveTo(370,410)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.moveTo(360,640)
    time.sleep(0.2)
    pyautogui.leftClick()
    pyautogui.moveTo(555,50)
    time.sleep(0.2)
    pyautogui.leftClick()
    i+=1
