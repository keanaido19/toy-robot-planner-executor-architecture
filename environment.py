from action import Action
from direction import Direction
from location import Location


class Environment:
    direction: Direction
    location: Location

    def __init__(self):
        self.direction = Direction.NORTH
        self.location = Location()

    def perform_action(self, action: Action) -> None:

        if action == Action.TURN_RIGHT or action == Action.TURN_LEFT:
            if self.direction == Direction.NORTH:
                self.direction = Direction.EAST if action == Action.TURN_RIGHT else Direction.WEST

            elif self.direction == Direction.EAST:
                self.direction = Direction.SOUTH if action == Action.TURN_RIGHT else Direction.NORTH

            elif self.direction == Direction.SOUTH:
                self.direction = Direction.WEST if action == Action.TURN_RIGHT else Direction.EAST

            elif self.direction == Direction.WEST:
                self.direction = Direction.NORTH if action == Action.TURN_RIGHT else Direction.SOUTH

        elif action == Action.MOVE_FORWARD:
            if self.direction == Direction.NORTH:
                self.location.set_y(self.location.get_y() + 1)

            elif self.direction == Direction.EAST:
                self.location.set_x(self.location.get_x() + 1)

            elif self.direction == Direction.SOUTH:
                self.location.set_y(self.location.get_y() - 1)

            elif self.direction == Direction.WEST:
                self.location.set_x(self.location.get_x() - 1)

    def get_state(self) -> tuple[tuple[int, int], Direction]:
        return (self.location.get_x(), self.location.get_y()), self.direction
