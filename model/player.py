from __future__ import annotations
from model.battleground import Battleground

from typing import Type

class Player:

    def __init__(self, defense_battleground: Battleground, attack_battleground: Battleground) -> None:
        self.defense_battleground = defense_battleground
        self.attack_battleground = attack_battleground
    
    @property
    def healths(self):
        return self.defense_battleground.get_remaining_power()
    
    def get_current_def_battleship(self):
        return self.defense_battleground.show_map()

    def attack(self, other_player: Player):
        other_player.defense_battleground.get_battle_with(self.attack_battleground)
