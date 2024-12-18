from mock import patch, mock_open
import pytest

from moonrobot.application.parser import Parser, ParsingError
from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.enums.orientation import Orientation
from moonrobot.domain.models.instruction import RobotInstruction
from moonrobot.domain.models.instructionset import InstructionSet
from moonrobot.domain.models.plateau import Plateau
from moonrobot.domain.models.position import RobotPosition


class Test_Parser:

    def test_shouldParseAValidSetOfInstructions(self):

        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMR\n2 2 N\nRMLM'

        parser = Parser()

        plateau = Plateau(5, 5)
        movementCommands1 = [MovementCommand('M'), MovementCommand('M'), MovementCommand('R')]
        movementCommands2 = [MovementCommand('R'), MovementCommand('M'), MovementCommand('L'), MovementCommand('M')]
        robotInstruction1 = RobotInstruction(RobotPosition(3, 3, Orientation('E')), movementCommands1)
        robotInstruction2 = RobotInstruction(RobotPosition(2, 2, Orientation('N')), movementCommands2)

        expectedSetOfInstructions = InstructionSet(plateau, [robotInstruction1, robotInstruction2])


        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            result = parser.parseFile(filePath)


        assert result.toString() == expectedSetOfInstructions.toString()

    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotValid(self):

        filePath = 'fakeFile/file.txt'
        mockedFileContent = 's 5\n3 3 E\nMMRMMRMRRM'

        parser = Parser()


        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = 'hjhkjj\n3 3 E\nMMRMMRMRRM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialPositionIsNotValid(self, capsys):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid robot initial position'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialPositionIsNotExactlyThreeValues(self, capsys):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5 5\n3 3\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid robot initial position'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionIfPlateauDimensionsAreNotExactlyTwo(self):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5\n3 3 E\nMMRMMRMRRM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match='Invalid plateau dimensions'):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenInitialOrientationIsNotValid(self, capsys):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        parser = Parser()

        # Then
        with pytest.raises(ParsingError, match="Invalid robot initial position"):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)

    def test_shouldRaiseExceptionWhenAnMovementCommandIsNotValid(self, capsys):
        # Given
        filePath = 'fakeFile/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'
        parser = Parser()

        # Then
        with pytest.raises(ValueError, match="'X' is not a valid MovementCommand"):
            with patch('builtins.open', mock_open(read_data=mockedFileContent)):
                parser.parseFile(filePath)
