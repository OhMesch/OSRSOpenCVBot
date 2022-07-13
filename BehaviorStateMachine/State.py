from abc import ABC, abstractmethod
import cv2
import os
from pyclick import HumanClicker
import sys

sys.path.append(os.path.realpath(os.path.pardir))
from ImageCapturer import ImageCapturer

class State(ABC):
    def __init__(self, context):
        self.context = context
        self.mouse = HumanClicker()

    def preTask(self):
        pass

    @abstractmethod
    def task(self):
        pass

    def postTask(self):
        pass

    def updateState(self, newState):
        self.context.setState(newState)