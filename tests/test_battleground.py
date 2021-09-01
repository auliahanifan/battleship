import pytest
from model.battleground import Battleground
from model.battleship import Battleship
from model.missile import Missile

def test_set_objects_battleship(mocker):
    sut = Battleground(2)
    positions = [[0,0]]
    battle_ship = Battleship()
    sut.set_objects(positions, battle_ship)
    
    expected = sut.map[0][0]
    assert type(expected) == type(battle_ship)
    assert expected != battle_ship

def test_set_objects_missile(mocker):
    sut = Battleground(2)
    positions = [[0,0]]
    missile = Missile()
    sut.set_objects(positions, missile)
    
    expected = sut.map[0][0]
    assert type(expected) == type(missile)
    assert expected != missile

def test_show_map(mocker):
    sut = Battleground(2)

    expected = """_ _ 
_ _ 
"""
    assert expected == sut.show_map()

def test_get_remaining_power(mocker):
    sut = Battleground(2)
    positions = [[0,0], [0, 1]]
    battle_ship = Battleship()
    sut.set_objects(positions, battle_ship)
    
    assert 2 == sut.get_remaining_power()

def test_get_battle_with_raise_exception_different_vertical(mocker):
    att_battleground = Battleground(4)
    positions = [[0,0], [0, 1]]
    missile = Missile()
    att_battleground.set_objects(positions, missile)

    sut = Battleground(2)
    positions = [[0,0], [0, 1]]
    battle_ship = Battleship()
    sut.set_objects(positions, battle_ship)

    with pytest.raises(Exception):
        sut.get_battle_with(att_battleground)

def test_get_battle_ship_get_damage(mocker):
    att_battleground = Battleground(2)
    positions = [[1,1], [0, 1]]
    missile = Missile()
    att_battleground.set_objects(positions, missile)

    sut = Battleground(2)
    positions = [[0,0], [0, 1]]
    battle_ship = Battleship()
    sut.set_objects(positions, battle_ship)

    sut.get_battle_with(att_battleground)

    assert 1 == sut.get_remaining_power()
    assert 0 == sut.map[0][1].health
    assert 1 == sut.map[0][0].health