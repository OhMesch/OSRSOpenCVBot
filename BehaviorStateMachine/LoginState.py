import subprocess

from .State import *

class LoginState(State):
    RS_PROCESS = "JagexLauncher.exe"
    RS_LAUNCH = "C:\\Users\\mesch\\jagexcache\\jagexlauncher\\bin\\JagexLauncher.exe oldschool"
    LOGIN_BUTTON_IMG = "..\\template_images\\login\\existing_user.png"

    def preTask(self):
        print(f"{self.isRSOpened()=}")
        if not self.isRSOpened():
            subprocess.Popen(self.RS_LAUNCH)

    def isRSOpened(self):
        is_open_call = f'TASKLIST /FI "IMAGENAME EQ {self.RS_PROCESS}"'
        is_open_out = subprocess.check_output(is_open_call).decode()
        return is_open_out.strip().split('\r\n')[-1].lower().startswith(self.RS_PROCESS.lower())

    def task(self):
        isLoggedIn = False
        while not isLoggedIn:
            current_screen_frame_bw = ImageCapturer.getBWCapture()
            login_button = cv2.imread(self.LOGIN_BUTTON_IMG, 0)

            print(f"{login_button=}")

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

            cv2.imshow("frame", current_screen_frame)
            if cv2.waitKey(1) & 0Xff == ord('q'):
                break
                #TODO Should exit state

        cv2.destroyAllWindows()

    def postTask(self):
        pass

    def updateState(newState):
        self.context.state = newState()