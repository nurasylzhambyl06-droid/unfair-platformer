from platform import Platform
from settings import sx, sy
from traps import Trap, MovingTrap
from fake_platform import FakePlatform
from falling_block import FallingBlock

platforms = [

    Platform(sx(0), sy(550), sx(1100), sy(50)),

    Platform(sx(120), sy(470), sx(120), sy(20)),

    FakePlatform(sx(300), sy(420), sx(120), sy(20)),

    Platform(sx(500), sy(360), sx(120), sy(20)),

    FallingBlock(sx(700), sy(290), sx(120), sy(20)),

    Platform(sx(900), sy(220), sx(100), sy(20))
]

traps = [

    Trap(sx(350), sy(530), sx(50), sy(20)),

    MovingTrap(sx(560), sy(330), sx(50), sy(20)),

    Trap(sx(760), sy(530), sx(50), sy(20))
]

goal_position = (sx(950), sy(150))
goal_moving = True
player_spawn = (sx(100), sy(100))