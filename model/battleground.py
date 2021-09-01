from __future__ import annotations
from model.missile import Missile
from model.battleship import Battleship

class Battleground:
    __map = None
    __EMPTY_SYMBOL = '_'
    total_power = 0

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
            value_of_object = position[2]
            # instantiate new object instead
            if isinstance(object, Battleship):
                self.__map[x][y] = Battleship(value_of_object)
                self.total_power += value_of_object
            elif isinstance(object, Missile):
                self.__map[x][y] = Missile(value_of_object)

    def show_map(self):
        map_string = ''

        for i in self.__map:
            line_string = ''
            for j in i:
                line_string += f'{j} '
            line_string += '\n'
            map_string += line_string
        
        return map_string
    
    def get_battle_with(self, opponent_battleground: Battleground):
        if len(self.__map) != len(opponent_battleground.map):
            raise Exception('Sorry, not same vertical battleground')

        for y in range(len(self.__map)):
            for x in range(len(self.__map[y])):
                if isinstance(opponent_battleground.map[y][x], Missile):
                    if isinstance(self.__map[y][x], Battleship):
                        # collide the missile to battleship
                        battleship = self.__map[y][x]
                        
                        # calculate the total power
                        temp = battleship.health - opponent_battleground.map[y][x].damage
                        if temp >= 0:
                            self.total_power -= opponent_battleground.map[y][x].damage
                        else:
                            self.total_power -= battleship.health

                        battleship.get_damage(opponent_battleground.map[y][x].damage)
                        self.__map[y][x] = battleship

                    else:
                        self.__map[y][x] = f'{opponent_battleground.map[y][x]}'

    def get_remaining_power(self):
        return self.total_power
        # power = 0
        # for y in self.__map:
        #     for x in y:
        #         if isinstance(x, Battleship):
        #             power += x.health

