class Battleship:
    __DEAD_SYMBOL = 'X'
    __ALIVE_SYMBOL = 'B'

    def __init__(self):
        self.__health = 1
    
    def __str__(self):
        if self.__health <= 0:
            return self.__DEAD_SYMBOL
        else:
            return self.__ALIVE_SYMBOL

    @property
    def health(self):
        return self.__health
    
    def get_damage(self, damage):
        if self.__health > 0:
            self.__health = self.__health - damage