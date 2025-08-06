from typing import List

from action import Action
from environment import Environment


class Executor:
    environment: Environment

    def __init__(self, environment: Environment):
        self.environment = environment

    def execute(self, plan: List[Action]) -> None:
        for action in plan:
            self.environment.perform_action(action)
            print(f"Executed action: {action}")