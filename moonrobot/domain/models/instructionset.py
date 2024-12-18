from typing import List

from moonrobot.domain.models.instruction import RobotInstruction
from moonrobot.domain.models.plateau import Plateau

# set of instructions for one or more robots on given plateau
class InstructionSet:

    def __init__(self, plateau: Plateau, robotInstructions: List[RobotInstruction]):
        self.plateau: Plateau = plateau
        self.robotInstructions: List[RobotInstruction] = robotInstructions

    def toString(self) -> str:
        robotInstructionsAsStrings = []
        for instruction in self.robotInstructions:
            robotInstructionsAsStrings.append(instruction.toString())
        return self.plateau.toString() + '\n' + '\n'.join(robotInstructionsAsStrings)