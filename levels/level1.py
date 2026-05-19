from platform import Platform
from traps import Trap
from settings import sx,sy

platforms=[

Platform(sx(0),sy(550),sx(800),sy(50)),

Platform(sx(180),sy(450),sx(120),sy(20)),

Platform(sx(360),sy(370),sx(120),sy(20)),

Platform(sx(550),sy(290),sx(120),sy(20))
]

traps=[

Trap(
sx(320),
sy(530),
sx(50),
sy(20)
)
]

goal_position=(
sx(650),
sy(220)
)

goal_moving=False

player_spawn=(
sx(50),
sy(450)
)