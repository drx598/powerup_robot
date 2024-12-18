
from moonrobot.domain.enums.orientation import Orientation

# X Y coordinates and movement direction representing current position of a robot
class RobotPosition:

    def __init__(self, coordinateInX: int, coordinateInY: int, orientation: Orientation):
        self.coordinateInX: int = coordinateInX
        self.coordinateInY: int = coordinateInY
        self.orientation: Orientation = orientation

    def toString(self) -> str:
        return str(self.coordinateInX) + " " + str(self.coordinateInY) + " " + self.orientation.value