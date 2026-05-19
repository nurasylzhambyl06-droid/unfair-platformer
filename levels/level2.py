from platform import Platform
from settings import sx, sy
from traps import Trap
from fake_platform import FakePlatform

platforms=[

    Platform(sx(0),sy(550),sx(800),sy(50)),

    Platform(sx(150),sy(450),sx(100),sy(20)),

    FakePlatform(sx(300),sy(400),sx(100),sy(20)),

    Platform(sx(500),sy(300),sx(100),sy(20)),

    Platform(sx(650),sy(220),sx(100),sy(20))

]

traps=[

    Trap(sx(220),sy(530),sx(50),sy(20)),

    Trap(sx(550),sy(280),sx(50),sy(20))

]

goal_position = (sx(700), sy(170))
goal_moving = False
player_spawn = (sx(100),sy(100))