from typing import List
import re

from moonrobot.domain.enums.mv_command import MovementCommand
from moonrobot.domain.enums.orientation import Orientation
from moonrobot.domain.models.instruction import RobotInstruction
from moonrobot.domain.models.instructionset import InstructionSet
from moonrobot.domain.models.plateau import Plateau
from moonrobot.domain.models.position import RobotPosition

class Parser:

    validPlateauInput = re.compile("^[0-9]* [0-9]*$")
    validRobotPosition = re.compile("^[0-9]* [0-9]* [NSEW]$")

    def parseFile(self, filePath: str) -> InstructionSet:
        with open(filePath, 'r') as inputFile:
            # reads 1st line from text file
            plateauInputLine = inputFile.readline()
            plateau = self.parsePlateauInput(plateauInputLine)

            robotInstructions = []
            # iterate over remaining lines in file starting from second line
            for lineCount, line in enumerate(inputFile, 1):
                # odd line count always contains position text so initialize robot position here else create robot instruction
                if lineCount % 2 != 0:
                    robotInitialPosition = self.parseInitialPosition(line)
                else:
                    robotInstruction = RobotInstruction(robotInitialPosition, self.parseMovementCommands(line))
                    robotInstructions.append(robotInstruction)

        return InstructionSet(plateau, robotInstructions)

    def parseMovementCommands(self, line: str) -> List[MovementCommand]:
        commandsToMoveRobot = [MovementCommand(command) for command in list(line.replace('\n', ''))]
        return commandsToMoveRobot

    def parseInitialPosition(self, line: str) -> RobotPosition:
        if not re.match(self.validRobotPosition, line):
            raise ParsingError("Invalid robot initial position")
        inputLineAsList = line.split()
        orientation = Orientation(inputLineAsList[2])
        return RobotPosition(int(inputLineAsList[0]),
                             int(inputLineAsList[1]),
                             orientation)

    # splits input string and returns platea object
    def parsePlateauInput(self, inputString: str) -> Plateau:
        if not re.match(self.validPlateauInput, inputString):
            raise ParsingError("Invalid plateau dimensions")
        inputStringAsList = inputString.split()
        return Plateau(int(inputStringAsList[0]), int(inputStringAsList[1]))
    
class ParsingError(Exception):
    pass