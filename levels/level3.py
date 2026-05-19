from platform import Platform
from traps import Trap,HiddenSpike
from trigger import Trigger
from settings import sx,sy

spike=HiddenSpike(
sx(580),
sy(530),
sx(50),
sy(20)
)

platforms=[

Platform(sx(0),sy(550),sx(800),sy(50)),

Platform(sx(150),sy(450),sx(120),sy(20)),

Platform(sx(350),sy(350),sx(120),sy(20)),

Platform(sx(550),sy(250),sx(120),sy(20))
]

traps=[

spike
]

trigger=Trigger(
sx(390),
sy(330),
sx(30),
sy(30),
spike
)

goal_position=(
sx(650),
sy(180)
)

goal_moving=True

player_spawn=(
sx(50),
sy(450)
)