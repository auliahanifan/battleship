from unittest.mock import MagicMock
from model.missile import Missile
from model.battleship import Battleship
from model.player import Player
from model.battleground import Battleground

def test_get_current_def_battleground_map(mocker):
    def_battleground = MagicMock()
    def_battleground.show_map.return_value = 'test'

    sut = Player(def_battleground, None)
    
    assert 'test' == sut.get_current_def_battleground_map()

def test_attack(mocker):
    mock_battleground = MagicMock()
    mock_opponent = MagicMock()
    sut = Player(None, mock_battleground)

    sut.attack(mock_opponent)

    mock_opponent.defense_battleground.get_battle_with.assert_called_once_with(mock_battleground)



