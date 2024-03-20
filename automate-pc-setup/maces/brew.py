import keyboard
import time
pwdfile = open("~/jsfhd.txt","r")
password = pwdfile.read()
time.sleep(1)
keyboard.write(password)
time.sleep(1)
keyboard.send("enter")
time.sleep(3)
keyboard.send("enter")
