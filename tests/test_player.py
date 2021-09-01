from unittest.mock import MagicMock
from model.player import Player


def test_get_health(mocker):
    mock = MagicMock()

    sut = Player(mock, None)
    sut.healths

    mock.get_remaining_power.assert_called_once()


def test_get_current_def_battleground_map(mocker):
    mock = MagicMock()
    mock.show_map.return_value = 'test'

    sut = Player(mock, None)
    
    assert 'test' == sut.get_current_def_battleground_map()
    mock.show_map.assert_called_once()

def test_attack(mocker):
    mock_battleground = MagicMock()
    mock_opponent = MagicMock()
    
    sut = Player(None, mock_battleground)

    sut.attack(mock_opponent)

    mock_opponent.defense_battleground.get_battle_with.assert_called_once_with(mock_battleground)



