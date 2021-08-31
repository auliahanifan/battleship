class Missile:
    def __init__(self):
        self.__damage = 1
    
    def __str__(self) -> str:
        return 'O'
    
    @property
    def damage(self):
        return self.__damage 
