from typing import List

from action import Action
from direction import Direction
from environment import Environment
from location import Location


class Planner:
    environment: Environment

    def __init__(self, environment: Environment):
        self.environment = environment

    def plan(self, goal: Location) -> List[Action]:

        current_location: Location = self.environment.get_state()[0]
        current_direction: Direction = self.environment.get_state()[1]

        actions: List[Action] = []

        if current_direction == Direction.NORTH:

            if goal.get_y() > current_location.get_y():
                actions.extend([Action.MOVE_FORWARD] * (goal.get_y() - current_location.get_y()))
            elif goal.get_x() > current_location.get_x():
                actions.append(Action.TURN_RIGHT)
            else:
                actions.append(Action.TURN_LEFT)

        elif current_direction == Direction.EAST:

            if goal.get_x() > current_location.get_x():
                actions.extend([Action.MOVE_FORWARD] * (goal.get_x() - current_location.get_x()))
            elif goal.get_y() > current_location.get_y():
                actions.append(Action.TURN_LEFT)
            else:
                actions.append(Action.TURN_RIGHT)

        elif current_direction == Direction.SOUTH:

            if goal.get_y() < current_location.get_y():
                actions.extend([Action.MOVE_FORWARD] * (current_location.get_y() - goal.get_y()))
            elif goal.get_x() > current_location.get_x():
                actions.append(Action.TURN_LEFT)
            else:
                actions.append(Action.TURN_RIGHT)

        elif current_direction == Direction.WEST:

            if goal.get_x() < current_location.get_x():
                actions.extend([Action.MOVE_FORWARD] * (current_location.get_x() - goal.get_x()))
            elif goal.get_y() > current_location.get_y():
                actions.append(Action.TURN_RIGHT)
            else:
                actions.append(Action.TURN_LEFT)

        return actions
