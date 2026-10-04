from __future__ import annotations
import json as js
class Entity():
    def __init__(self, life: int, damage: int, name: str, range: int):
        self.life = life
        self.damage = damage
        self.name = name
        self.isAlive = True
        #Hay hasta 3 tipos de rango, 1, rango corto; 2, rango medio y 3, rango alto, si escribes uno mayor o menor, se corregirá a su valor más cercano
        if range > 3:
            range = 3
        elif range < 1:
            range = 1
        self.range = range
    def present(self):
        print(f"Vida actual: {self.life}\nDaño Actual: {self.damage}\nNombre: {self.name}\n¿Está vivo?: {self.isAlive}\nRango actual: {self.range}")
    def kill(self):
        self.life = 0
        self.isAlive = False
        print(f"{self.name} ha muerto.")
    def SimpleAttack(self, Enemy: Entity):
        r"""El tipo de ataque mas simple, le quita vida al oponente según el daño del atacante"""
        if Enemy.range <= self.range:
            Enemy.life -= self.damage
            print(f"{self.name} ha atacado a {Enemy.name}. ")
            if Enemy.life <= 0:
                Enemy.kill()
