import pyautogui
import time

while True:
     
     positionX, positionY = pyautogui.position() # X ve Y olarak kordinat kuralını tanımlıyoruz.
     print("Mouse Kordinatları: ", positionX, positionY) # Ve hareket ettirdikçe bize çıktısını vermesini sağlıyoruz.
     
time.sleep()
