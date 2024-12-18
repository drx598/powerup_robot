
from moonrobot.domain.models.position import RobotPosition

# representation of a plateau on the moon surface assuming 0,0 as lower bound and passed dimensions as upper bounds
class Plateau:

    def __init__(self, dimensionInX: int, dimensionInY: int):
        self.dimensionInX: int = dimensionInX
        self.dimensionInY: int = dimensionInY

    def isPositionWithinPlateauArea(self, position: RobotPosition):
        return not (position.coordinateInX > self.dimensionInX or
                position.coordinateInY > self.dimensionInY)

    def toString(self):
        return str(self.dimensionInX) + ' ' + str(self.dimensionInY)