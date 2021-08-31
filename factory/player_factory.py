from model.player import Player
from model.battleground import Battleground
from model.battleship import Battleship
from model.missile import Missile

class PlayerFactory:

    @staticmethod
    def create_new_player(length: int, defense_positions: list, attack_positions: list):
        def_battleground = Battleground(length)
        att_battleground = Battleground(length)
        ship = Battleship()
        missile = Missile()
        def_battleground.set_objects(defense_positions, ship)
        att_battleground.set_objects(attack_positions, missile)

        return Player(def_battleground, att_battleground)
