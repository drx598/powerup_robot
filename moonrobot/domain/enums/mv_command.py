from enum import Enum

# robot movement commands to move forward one point or turn right/left 90degrees
class MovementCommand(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    MOVE = 'M'