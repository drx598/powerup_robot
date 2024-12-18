## Installing

Requirements : Python3, pip

optionally use virtualenv

```
   git clone git@github.com:drx598/powerup_robot.git
   cd powerup_robot
   pip3 install .
```
## How to use:
###  Running the test input
```
   python3 run.py
```
This will take the test input from ```inputFile.txt``` and print the Robot(s) final position(s) to stdout.
    
### Modifying the input
By editing ```inputFile.txt```  and running ```run.py``` again you can test different set of instructions 
## Running the tests
```
python3 -m pytest
```
## Assumptions/ Thought process

- Any number of robots could be present on the plateau
- Robots cannot move to an occupied position
- Robots are limited to navigation within the plateau
- Robot cannot exist without a plateau and commands cannot be sent to a robot not on a plateau

