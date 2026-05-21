from platform import Platform
from settings import sx, sy
from traps import Trap, MovingTrap
from fake_platform import FakePlatform
from falling_block import FallingBlock

platforms = [

    Platform(sx(0), sy(550), sx(1100), sy(50)),

    Platform(sx(120), sy(480), sx(100), sy(20)),

    FakePlatform(sx(260), sy(420), sx(100), sy(20)),

    Platform(sx(420), sy(360), sx(100), sy(20)),

    FallingBlock(sx(580), sy(300), sx(100), sy(20)),

    FakePlatform(sx(740), sy(240), sx(100), sy(20)),

    Platform(sx(920), sy(180), sx(100), sy(20))
]

traps = [

    Trap(sx(200), sy(530), sx(50), sy(20)),

    MovingTrap(sx(450), sy(330), sx(50), sy(20)),

    Trap(sx(620), sy(530), sx(50), sy(20)),

    MovingTrap(sx(780), sy(210), sx(50), sy(20))
]

goal_position = (sx(970), sy(120))
goal_moving = True
player_spawn = (sx(100), sy(100))