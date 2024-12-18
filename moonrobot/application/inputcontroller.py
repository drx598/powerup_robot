from typing import List

from moonrobot.application.parser import Parser, ParsingError
from moonrobot.domain.models.robot import Robot

class InputFileController:

    def __init__(self):
        self.robots = List[Robot]

    def processFile(self, filePath: str, parser: Parser):
        try:
            setOfInstructions = parser.parseFile(filePath)
            occupied = []
            for instruction in setOfInstructions.robotInstructions:
                robot = Robot(setOfInstructions.plateau, instruction.initialPosition, occupied)
                robot.processCommands(instruction.movementCommands)
                occupied.append(robot.currentPosition)
                print(robot.currentPosition.toString())
        except ParsingError as error:
            print(error)
        except ValueError as error:
            print(error)