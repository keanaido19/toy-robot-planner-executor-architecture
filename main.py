import re
from typing import List

from action import Action
from environment import Environment
from executor import Executor
from location import Location
from planner import Planner

MAX_X = 1000
MAX_Y = 1000


def get_user_input() -> str:
    return "".join(input(
        f"Please enter x and y between x({-MAX_X} to {MAX_X}) & y({-MAX_Y} to {MAX_Y}) eg; '1,2' or type 'q' to quit: ").split())


def parse_user_input(usr_input: str) -> Location | bool:
    ret: Location | bool

    match = re.match(r"^(-?\d+),(-?\d+)$", usr_input)

    try:
        x = int(match.group(1))
        y = int(match.group(2))

        if abs(x) > MAX_X or abs(y) > MAX_Y:
            raise ValueError

        ret = Location(x, y)
    except (AttributeError, ValueError):
        ret = False

    return ret


def print_robot_state(env: Environment) -> None:
    location = env.get_state()[0]
    direction = env.get_state()[1]
    print(f"Robot is at: ({location.get_x()}, {location.get_y()}) - facing {direction.value[0]}")


if __name__ == '__main__':
    environment = Environment()
    planner = Planner(environment)
    executor = Executor(environment)

    print_robot_state(environment)

    while True:
        user_input = get_user_input()
        if user_input == "q":
            break

        goal: Location | bool = parse_user_input(user_input)

        if not goal:
            print("Invalid input!")
            continue

        while environment.get_state()[0] != goal:
            plan: List[Action] = planner.plan(goal)
            executor.execute(plan)

        print_robot_state(environment)
