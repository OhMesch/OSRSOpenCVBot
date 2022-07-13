import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
from pyclick import HumanClicker
import time
import random
import subprocess

import CREDS

def isRSOpened():
   # TODO check os
   rs_proccess = "JagexLauncher.exe"
   is_open_call = f'TASKLIST /FI "IMAGENAME EQ {rs_proccess}"'
   is_open_out = subprocess.check_output(is_open_call).decode()
   return is_open_out.strip().split('\r\n')[-1].lower().startswith(rs_proccess.lower())

mouse = HumanClicker()

rs_path = "C:\\Users\\mesch\\jagexcache\\jagexlauncher\\bin\\JagexLauncher.exe oldschool"
print(f"{isRSOpened()=}")
if not isRSOpened():
    subprocess.Popen(rs_path)

while True:
    screen_capture_image = ImageGrab.grab() #x, y, w, h
    current_screen_frame_BGR = np.array(screen_capture_image)
    current_screen_frame = cv2.cvtColor(current_screen_frame_BGR, cv2.COLOR_BGR2RGB)
    current_screen_frame_bw = cv2.cvtColor(current_screen_frame, cv2.COLOR_BGR2GRAY)
    
    login_button = cv2.imread("template_images\\login\\existing_user.png", 0)
    login_width, login_height = login_button.shape[::-1]
    template_match = cv2.matchTemplate(current_screen_frame_bw, login_button, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(template_match)
    print(f"{min_val=}")
    if min_val < 50000:
        top_left = min_loc
        bottom_right = (top_left[0] + login_width, top_left[1] + login_height)
        rand_point = (random.randint(top_left[0], top_left[0] + login_width), random.randint(top_left[1], top_left[1] + login_height))
        cv2.rectangle(current_screen_frame, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(current_screen_frame, "Existing User Button", (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        mouse.move(rand_point, random.uniform(0.13,.66))
        mouse.click()
        time.sleep(.2)
        for char in CREDS.PASS:
            time.sleep(random.uniform(.15, .4))
            pyautogui.typewrite(char)
        pyautogui.press("Enter")

    lower_blue = np.array([55,153,255])
    upper_blue = np.array([77,123,158])
    mask = cv2.inRange(current_screen_frame, lower_blue, upper_blue)
    cv2.imshow("fish", cv2.bitwise_and(current_screen_frame,current_screen_frame, mask= mask))

    cv2.imshow("frame", current_screen_frame)
    if cv2.waitKey(1) & 0Xff == ord('q'):
        break

cv2.destroyAllWindows()