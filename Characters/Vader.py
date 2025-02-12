# Dependencies
import random

# Abilities
# Manipulate (Basic)
def Terrifying_Swing():
    Terrifying_Swing_Damage1 = 23089 * (1 + random.uniform(-0.05, 0.05))
    Terrifying_Swing_Damage2 = 23089 * (1 + random.uniform(-0.05, 0.05))
    return Terrifying_Swing_Damage1 + Terrifying_Swing_Damage2
def Force_Crush():
    Force_Crush_Damage = 7851 * (1 + random.uniform(-0.05, 0.05))
    return Force_Crush_Damage
