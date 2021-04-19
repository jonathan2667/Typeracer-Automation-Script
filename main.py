from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyautogui

import easyocr

from matplotlib import pyplot as plt

import numpy as np

import cv2

driver = webdriver.Firefox()
driver.maximize_window()

driver.get('https://play.typeracer.com/')

sleep(1)
pyautogui.moveTo(500, 970)
pyautogui.click()

sleep(1)
im = pyautogui.screenshot('img.png', region=(460, 700, 980, 150))

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext('img.png')
for i in range (0, len(result) - 1):
    print(result[i][1])
    for j in range (0, len(result[i][1])):
        if (result[i][1][j] == ';'):
            pyautogui.typewrite(',')
        else:
            pyautogui.typewrite(result[i][1][j])
    pyautogui.typewrite(' ')