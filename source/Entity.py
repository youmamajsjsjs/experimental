from __future__ import annotations
import json as js
def resetToZero(num: int):
    if num < 0:
        return 0
    else:
        return num
class Entity():
    """Esta es la clase principal de las entidades, los jugadores y enemigos se guardan ahí.\n
    Debes declarar sus valores de vida, daño, un nombre, rango, mana  y armadura."""
    def __init__(self, life: int, damage: int, name: str, range: int, armor:float, mana:int):
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
        #la armadura es un porcentaje de resistencia, así que debe estar entre 0 y 1
        self.armorMultiply = 0.75
        if armor > 1:
            armor = 1
        elif armor < 0:
            armor = 0
        self.armor = armor * self.armorMultiply
        self.mana = mana
    def present(self):
        """Esto te manda toda la data de tu personaje, o de cualquier entidad."""
        print(f"Vida actual: {self.life}\nDaño Actual: {self.damage}\nNombre: {self.name}\n¿Está vivo?: {self.isAlive}\nRango actual: {self.range}\nA")
    def AdvertAction(self):
        if self.mana == 0:
            print(f"{self.name} se ha quedado sin mana.")
    def kill(self):
        """Declara la muerte de una entidad."""
        self.life = 0
        self.isAlive = False
        print(f"{self.name} ha muerto.")
    def SimpleAttack(self, Enemy: Entity):
        r"""El tipo de ataque mas simple, le quita vida al oponente según el daño del atacante, ignora armadura, cuesta 10 de mana. """
        if Enemy.range <= self.range:
            Enemy.life -= self.damage
            self.mana = resetToZero(self.mana - 10)
            self.AdvertAction() 
            print(f"{self.name} ha atacado a {Enemy.name}. ")
            if Enemy.life <= 0:
                Enemy.kill()
        else:
            print(f"{Enemy.name} está muy lejos de tí")
    def NormalAttack(self, Enemy: Entity):
        r"""El ataque mas común, cuenta la armadura del objetivo para hacer daño"""
