class Battleship:
    __DEAD_SYMBOL = 'X'
    __ALIVE_SYMBOL = 'B'

    def __init__(self, health=1):
        self.__health = health
    
    def __str__(self):
        if self.__health <= 0:
            return self.__DEAD_SYMBOL
        else:
            return self.__ALIVE_SYMBOL

    @property
    def health(self):
        return self.__health
    
    def get_damage(self, damage):
        temp = self.__health - damage
        if temp >= 0:
            self.__health = self.__health - damage
        else:
            self.__health = 0