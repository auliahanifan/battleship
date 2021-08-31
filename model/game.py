from model.player import Player

class Game():
    def __init__(self, player1: Player, player2: Player) -> None:
        self.__player1 = player1
        self.__player2 = player2

    def start_battle(self) -> None:
        self.__player1.attack(self.__player2)
        self.__player2.attack(self.__player1)
    
    def get_result(self) -> str:
        result = ''
        result += 'Player 1 \n'
        result += self.__player1.get_current_def_battleship()
        result += '\n'
        result += 'Player 2 \n'
        result += self.__player2.get_current_def_battleship()
        result += '\n'

        result += f'P1: {self.__player1.healths}\n'
        result += f'P2: {self.__player2.healths}\n\n'

        if self.__player1.healths > self.__player2.healths:
            result += 'Player 1 Win'
        elif self.__player2.healths > self.__player1.healths: 
            result += 'Player 2 Win'
        else:
            result += 'It is Draw'
        return result