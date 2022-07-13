from BehaviorStateMachine.BehaviorStateMachine import BehaviorStateMachine
import cv2
from PIL import ImageGrab
import numpy as np
import pyautogui
from pyclick import HumanClicker
import time
import random

import CREDS

class Player():
    def __init__(self):
        self.sm = BehaviorStateMachine()

    def play(self):
        while True:
            self.sm.action()

if __name__ == "__main__":
    player = Player()
    player.play()