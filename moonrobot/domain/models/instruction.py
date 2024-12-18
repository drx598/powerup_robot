from typing import List

from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.models.position import RobotPosition

# Single Robot instruction with an initial position and List of movement commands
class RobotInstruction:

    def __init__(self, initialPosition: RobotPosition, movementCommands: List[MovementCommand]):
        self.initialPosition: RobotPosition = initialPosition
        self.movementCommands: List[MovementCommand] = movementCommands

    def toString(self) -> str:
        movementCommandsAsString = ''.join([command.value for command in self.movementCommands])
        return self.initialPosition.toString() + '\n' + movementCommandsAsString