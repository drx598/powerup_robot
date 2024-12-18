from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.enums.orientation import Orientation
from moonrobot.domain.models.instruction import RobotInstruction
from moonrobot.domain.models.position import RobotPosition


class Test_RobotInstruction:

    def test_shouldReturnInstructionAsString(self):
        # Given
        instruction = RobotInstruction(RobotPosition(2, 2, Orientation.NORTH),
                                       [MovementCommand.MOVE, MovementCommand.LEFT])
        expectedInstructionAsString = '2 2 N' + '\n' + 'ML'
        # When
        result = instruction.toString()
        # Then
        assert  result == expectedInstructionAsString
