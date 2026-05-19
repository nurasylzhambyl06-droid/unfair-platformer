from platform import Platform
from settings import sx, sy
from traps import Trap, MovingTrap
from fake_platform import FakePlatform
from falling_block import FallingBlock

platforms=[

    Platform(sx(0),sy(550),sx(800),sy(50)),

    Platform(sx(100),sy(480),sx(100),sy(20)),

    FakePlatform(sx(250),sy(420),sx(100),sy(20)),

    FallingBlock(sx(400),sy(350),sx(100),sy(20)),

    Platform(sx(600),sy(260),sx(100),sy(20)),

    Platform(sx(700),sy(180),sx(80),sy(20))

]

traps=[

    Trap(sx(200),sy(530),sx(50),sy(20)),

    MovingTrap(sx(300),sy(300),sx(50),sy(20)),

    Trap(sx(500),sy(330),sx(50),sy(20))

]

goal_position = (sx(720), sy(130))
goal_moving = False
player_spawn = (sx(100),sy(100))