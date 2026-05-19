from platform import Platform
from settings import sx, sy
from traps import Trap, MovingTrap
from fake_platform import FakePlatform
from falling_block import FallingBlock

platforms = [

    Platform(sx(0),sy(550),sx(800),sy(50)),

    Platform(sx(200),sy(450),sx(150),sy(20)),

    Platform(sx(450),sy(350),sx(150),sy(20)),

    Platform(sx(650),sy(250),sx(100),sy(20))

]

traps=[

    Trap(sx(300),sy(530),sx(50),sy(20)),

    MovingTrap(sx(500),sy(330),sx(50),sy(20))

]

goal_position=(sx(700),sy(180))
player_spawn = (sx(100),sy(100))