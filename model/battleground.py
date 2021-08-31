from __future__ import annotations
from model.missile import Missile
from model.battleship import Battleship

class Battleground:
    __map = None
    __EMPTY_SYMBOL = '_'

    def __init__(self, length) -> None:
        self.__map = []
        self.__horizontal_length = length
        self.__vertical_length = length

        for _ in range(self.__vertical_length):
            line = []
            for _ in range(self.__horizontal_length):
                line.append(self.__EMPTY_SYMBOL)
            self.__map.append(line)
    
    @property
    def map(self):
        return self.__map
    
    def set_objects(self, positions: list, object: object):
        for position in positions:
            x = position[0]
            y = position[1]
            # instantiate new object instead
            if isinstance(object, Battleship):
                self.__map[x][y] = Battleship()
            elif isinstance(object, Missile):
                self.__map[x][y] = Missile()

    def show_map(self):
        map_string = ''

        for i in self.__map:
            line_string = ''
            for j in i:
                line_string += f'{j} '
            line_string += '\n'
            map_string += line_string
        
        return map_string
    
    def get_challenge(self, opponent_battleground: Battleground):
        if len(self.__map) != len(opponent_battleground.map):
            raise Exception('Sorry, not same vertical battleground')

        for y in range(len(self.__map)):
            if len(self.__map[y]) != len(opponent_battleground.map[y]):
                raise Exception('Sorry, not same horizontal battleground')
            
            for x in range(len(self.__map[y])):
                if isinstance(opponent_battleground.map[y][x], Missile):
                    if isinstance(self.__map[y][x], Battleship):
                        battleship = self.__map[y][x]
                        battleship.get_damage(opponent_battleground.map[y][x].damage)
                        self.__map[y][x] = battleship

                    else:
                        self.__map[y][x] = f'{opponent_battleground.map[y][x]}'

    def get_power(self):
        power = 0
        for y in self.__map:
            for x in y:
                if isinstance(x, Battleship):
                    power += x.health
        return power

