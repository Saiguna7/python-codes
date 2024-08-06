import random
import pyautogui as pg
import time

time.sleep(8)
words = ('hi  ','what doing');
for i in range(10):
        a = random.choice(words)
        pg.write(a+" chintu anna")
        pg.press('enter')
        
a