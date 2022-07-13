from .LoginState import LoginState

class BehaviorStateMachine():
    def __init__(self):
        self.state = LoginState(self)

    def action(self):
        self.state.preTask()
        self.state.task()
        self.state.postTask()

    def setState(self, newState):
        self.state = newState