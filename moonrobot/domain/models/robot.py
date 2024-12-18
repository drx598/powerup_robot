from typing import List
from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.enums.orientation import Orientation
from moonrobot.domain.models.plateau import Plateau
from moonrobot.domain.models.position import RobotPosition

class Robot:

    def __init__(self, plateau: Plateau, initialPosition: RobotPosition, occupied: List[RobotPosition] = []):
        if not plateau.isPositionWithinPlateauArea(initialPosition):
            raise ValueError('robot initial position out of plateau area')
        self.plateau: Plateau = plateau
        self.currentPosition: RobotPosition = initialPosition
        self.occupied: List[RobotPosition] = occupied

    def processCommands(self, commands: List[MovementCommand]):

        for command in commands:
            if command == MovementCommand.MOVE:
                self.move()
            if command == MovementCommand.RIGHT:
                self.turnRight()
            if command == MovementCommand.LEFT:
                self.turnLeft()

    def turnLeft(self) -> RobotPosition:
        leftOrientationMapping = {
            Orientation.NORTH: Orientation.WEST,
            Orientation.WEST: Orientation.SOUTH,
            Orientation.SOUTH: Orientation.EAST,
            Orientation.EAST: Orientation.NORTH
        }
        newOrientation = leftOrientationMapping.get(self.currentPosition.orientation, Orientation.NORTH)
        self.currentPosition.orientation = newOrientation
        return self.currentPosition

    def turnRight(self) -> RobotPosition:
        rightOrientationMapping = {
            Orientation.NORTH: Orientation.EAST,
            Orientation.WEST: Orientation.NORTH,
            Orientation.SOUTH: Orientation.WEST,
            Orientation.EAST: Orientation.SOUTH
        }
        newOrientation = rightOrientationMapping.get(self.currentPosition.orientation, Orientation.NORTH)
        self.currentPosition.orientation = newOrientation
        return self.currentPosition

    def move(self) -> RobotPosition:
        moveMappingTable = {
            Orientation.NORTH: lambda: RobotPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY + 1,
                                                     self.currentPosition.orientation),
            Orientation.SOUTH: lambda: RobotPosition(self.currentPosition.coordinateInX,
                                                     self.currentPosition.coordinateInY - 1,
                                                     self.currentPosition.orientation),
            Orientation.WEST: lambda: RobotPosition(self.currentPosition.coordinateInX - 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation),
            Orientation.EAST: lambda: RobotPosition(self.currentPosition.coordinateInX + 1,
                                                    self.currentPosition.coordinateInY,
                                                    self.currentPosition.orientation)
        }
        newRobotPosition = moveMappingTable.get(self.currentPosition.orientation,
                                                lambda: RobotPosition(0, 0, Orientation.SOUTH))()
        if not self.plateau.isPositionWithinPlateauArea(newRobotPosition):
            raise ValueError('Moving out of bounds prohibited')
        if self.isOccupied(newRobotPosition):
            raise ValueError('Position already Occupied')
        self.currentPosition = newRobotPosition
        return self.currentPosition
    
    def isOccupied( self, position: RobotPosition):
        for occupiedPosition in self.occupied:
            if position.coordinateInX == occupiedPosition.coordinateInX and position.coordinateInY == occupiedPosition.coordinateInY:
                return True
        return False