from mock import patch, mock_open

from moonrobot.application.inputcontroller import InputFileController
from moonrobot.application.parser import Parser

class Test_InputFileController:

    parser = Parser()

    def test_shouldCalculateFinalPositionForOneRobot(self, capsys):
        
        filePath = 'tests/fixtures/1robot.txt'
        inputFileController = InputFileController()
        
        inputFileController.processFile(filePath, self.parser)
        printedOutput = capsys.readouterr().out

        expectedFinalPosition = "5 1 E\n"

        assert expectedFinalPosition == printedOutput

    def test_shouldCalculateFinalPositionForTwoRobots(self, capsys):
        parser = Parser()

        inputFilePath = 'tests/fixtures/2robots.txt'
        inputFileController = InputFileController()

        inputFileController.processFile(inputFilePath, parser)
        printedOutput = capsys.readouterr().out

        expectedRobotsFinalPositions = '1 3 N' + '\n' + '5 1 E' + '\n'
        assert expectedRobotsFinalPositions == printedOutput

    def test_shouldCalculateFinalPositionForThreeeRobots(self, capsys):
        parser = Parser()

        inputFilePath = 'tests/fixtures/3robots.txt'
        inputFileController = InputFileController()

        inputFileController.processFile(inputFilePath, parser)
        printedOutput = capsys.readouterr().out
        expectedFinalPosition = "5 1 E\n3 4 N\n1 2 N\n"
        assert printedOutput == expectedFinalPosition

    def test_shouldPrintAnErrorWhenPlateauDimensionsAreNotValid(self, capsys):
        parser = Parser()

        inputFilePath = 'tests/fixtures/invalid_plateau.txt'
        inputFileController = InputFileController()

        inputFileController.processFile(inputFilePath, parser)
        printedOutput = capsys.readouterr().out
        errorMessage = "Invalid plateau dimensions\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenRobotInitialPositionIsNotValid(self, capsys):

        filePath = 'fakepath/file.txt'
        mockedFileContent = '5 5\n3 s E\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()


        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)


        printedOutput = capsys.readouterr().out
        errorMessage = "Invalid robot initial position\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenRobotInitialOrientationIsNotValid(self, capsys):

        filePath = 'fakepath/file.txt'
        mockedFileContent = '5 5\n3 3 X\nMMRMMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()


        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)


        printedOutput = capsys.readouterr().out
        errorMessage = "Invalid robot initial position\n"
        assert printedOutput == errorMessage

    def test_shouldPrintAnErrorWhenAnMovementCommandIsNotValid(self, capsys):

        filePath = 'fakepath/file.txt'
        mockedFileContent = '5 5\n3 3 E\nMMRXMRMRRM\n2 2 N\nMRMLM\n1 1 N\nM'

        inputFileController = InputFileController()


        with patch('builtins.open', mock_open(read_data=mockedFileContent)):
            inputFileController.processFile(filePath, self.parser)


        printedOutput = capsys.readouterr().out
        errorMessage = "'X' is not a valid MovementCommand\n"
        assert printedOutput == errorMessage
