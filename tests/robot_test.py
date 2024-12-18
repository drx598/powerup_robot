import pytest

from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.enums.orientation import Orientation
from moonrobot.domain.models.plateau import Plateau
from moonrobot.domain.models.position import RobotPosition
from moonrobot.domain.models.robot import Robot


class Test_Robot:

    def test_RobotCanMoveToPosition(self):
        # Given
        initialPosition = RobotPosition(2, 2, Orientation.NORTH)
        plateau = Plateau(5, 5)
        movementCommands = [MovementCommand.MOVE,
                            MovementCommand.RIGHT,
                            MovementCommand.MOVE,
                            MovementCommand.LEFT,
                            MovementCommand.MOVE]
        robot = Robot(plateau, initialPosition)
        # When
        robot.processCommands(movementCommands)
        # Then
        expectedFinalPosition = '3 4 N'
        assert robot.currentPosition.toString() == expectedFinalPosition

    def test_CannotCreateRobotIfInitialPositionOutOfPlateauArea(self):
        # Given
        plateau = Plateau(5, 5)
        initialPosition = RobotPosition(6, 5, Orientation.NORTH)
        # Then
        with pytest.raises(ValueError, match='robot initial position out of plateau area'):
            robot = Robot(plateau, initialPosition)

    def test_CannotMoveRobotOutOfPlateau(self):
        # Given
        initialPosition = RobotPosition(2, 2, Orientation.NORTH)
        plateau = Plateau(3, 3)
        movementCommands = [MovementCommand.MOVE, MovementCommand.MOVE, MovementCommand.MOVE]
        robot = Robot(plateau, initialPosition)
        # Then
        with pytest.raises(ValueError, match='Moving out of bounds prohibited'):
            robot.processCommands(movementCommands)
        assert robot.currentPosition.toString() == RobotPosition(2, 3, Orientation.NORTH).toString()