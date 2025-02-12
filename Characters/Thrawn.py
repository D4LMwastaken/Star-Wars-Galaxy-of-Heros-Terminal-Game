# Dependencies
import random

# Abilities
# Manipulate (Basic)
def Manipulate():
    Mainpulate_Damage = 19473 * (1 + random.uniform(-0.05, 0.05))
    return Mainpulate_Damage
def Fracture():
    Fracture_Damage1 = 7878 * (1+ random.uniform(-0.05, 0.05))
    Fracture_Damage2 = 7878 * (1+ random.uniform(-0.05, 0.05))
    Fracture_Damage3 = 7878 * (1+ random.uniform(-0.05, 0.05))
    Fracture_Damage4 = 7878 * (1+ random.uniform(-0.05, 0.05))
    Fracture_Damage = Fracture_Damage1 + Fracture_Damage2 + Fracture_Damage3 + Fracture_Damage4
    return Fracture_Damage
