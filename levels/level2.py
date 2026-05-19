from platform import Platform
from settings import sx,sy
from fake_platform import FakePlatform
from traps import Trap
from trigger import Trigger



fake=FakePlatform(
sx(350),
sy(350),
sx(120),
sy(20)
)

platforms=[

Platform(sx(0),sy(550),sx(800),sy(50)),

Platform(sx(150),sy(450),sx(120),sy(20)),

fake,

Platform(sx(550),sy(260),sx(120),sy(20))
]

traps=[

Trap(
sx(420),
sy(530),
sx(50),
sy(20)
)
]

trigger=Trigger(
sx(250),
sy(430),
sx(30),
sy(30),
fake
)

goal_position=(
sx(650),
sy(180)
)

goal_moving=False

player_spawn=(
sx(50),
sy(450)
)