#Enums are readable names bound by a constant value
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State["ACTIVE"])
