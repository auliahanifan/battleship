class Missile:
    def __init__(self, damage=1):
        self.__damage = damage
    
    def __str__(self) -> str:
        return 'O'
    
    @property
    def damage(self):
        return self.__damage 
