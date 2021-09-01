from os import openpty
import pytest
from model.battleground import Battleground
from model.battleship import Battleship
from model.missile import Missile

SHIP_HEALTH = 2
SHIP_HEALTH_SECONDARY = 10

MISSILE_DAMAGE = 2
MISSILE_DAMAGE_SECONDARY = 5


def test_map(mocker):

    sut = Battleground(2)

    expected = [['_', '_'], ['_', '_']]

    assert isinstance(sut.map, list)
    assert expected == sut.map

def test_set_objects_battleship(mocker):
    # given
    position = [[0, 0, SHIP_HEALTH]]
    object_to_insert = Battleship()

    sut = Battleground(2)

    # when
    sut.set_objects(position, object_to_insert)

    assert type(sut.map[0][0]) == type(object_to_insert)

def test_set_objects_missile(mocker):
    # given
    position = [[0, 0, MISSILE_DAMAGE]]
    object_to_insert = Missile()

    sut = Battleground(2)

    # when
    sut.set_objects(position, object_to_insert)

    assert type(sut.map[0][0]) == type(object_to_insert)

def test_show_map():
    sut = Battleground(2)

    expected = """_ _ 
_ _ 
"""
    assert expected == sut.show_map()

def test_get_battle_with_if_collided(mocker):
    ship_position = [[0, 0, SHIP_HEALTH]]
    missile_position = [[0, 0, MISSILE_DAMAGE_SECONDARY]]

    opponent = Battleground(2)
    opponent.set_objects(missile_position, Missile())

    sut = Battleground(2)
    sut.set_objects(ship_position, Battleship())

    sut.get_battle_with(opponent)

    assert 'X' == str(sut.map[0][0])

def test_get_battle_with_if_not_collided():
    ship_position = [[0, 1, SHIP_HEALTH_SECONDARY]]
    missile_position = [[0, 0, MISSILE_DAMAGE]]

    opponent = Battleground(2)
    opponent.set_objects(missile_position, Missile())

    sut = Battleground(2)
    sut.set_objects(ship_position, Battleship())

    sut.get_battle_with(opponent)

    assert 'O' == str(sut.map[0][0])

def test_get_remaining_power():

    ship_position = [[0,0, SHIP_HEALTH], [0, 1, SHIP_HEALTH_SECONDARY]]
    sut = Battleground(2)
    sut.set_objects(ship_position, Battleship())

    result = sut.get_remaining_power()
    expected = SHIP_HEALTH + SHIP_HEALTH_SECONDARY

    assert expected == result

def get_battle_with_raise_EXCEPTION_if_length_not_same():
    ship_position = [[0, 0, SHIP_HEALTH_SECONDARY]]
    missile_position = [[0, 0, MISSILE_DAMAGE]]

    opponent = Battleground(3)
    opponent.set_objects(missile_position, Missile())

    sut = Battleground(2)
    sut.set_objects(ship_position, Battleship())

    with pytest.raises(Exception):
        sut.get_battle_with(opponent)

def test_set_object_raise_INDEX_ERROR():
    missile_position = [[200, 100, MISSILE_DAMAGE_SECONDARY]]
    sut = Battleground(2)

    with pytest.raises(IndexError):
        sut.set_objects(missile_position, Battleship())








# def test_set_objects_battleship(mocker):
#     sut = Battleground(2)
#     positions = [[0,0]]
#     battle_ship = Battleship()
#     sut.set_objects(positions, battle_ship)
    
#     expected = sut.map[0][0]
#     assert type(expected) == type(battle_ship)
#     assert expected != battle_ship

# def test_set_objects_missile(mocker):
#     sut = Battleground(2)
#     positions = [[0,0]]
#     missile = Missile()
#     sut.set_objects(positions, missile)
    
#     expected = sut.map[0][0]
#     assert type(expected) == type(missile)
#     assert expected != missile

# def test_show_map(mocker):
#     sut = Battleground(2)

#     expected = """_ _ 
# _ _ 
# """
#     assert expected == sut.show_map()

# def test_get_remaining_power(mocker):
#     sut = Battleground(2)
#     positions = [[0,0], [0, 1]]
#     battle_ship = Battleship()
#     sut.set_objects(positions, battle_ship)
    
#     assert 2 == sut.get_remaining_power()

# def test_get_battle_with_raise_exception_different_vertical(mocker):
#     att_battleground = Battleground(4)
#     positions = [[0,0], [0, 1]]
#     missile = Missile()
#     att_battleground.set_objects(positions, missile)

#     sut = Battleground(2)
#     positions = [[0,0], [0, 1]]
#     battle_ship = Battleship()
#     sut.set_objects(positions, battle_ship)

#     with pytest.raises(Exception):
#         sut.get_battle_with(att_battleground)

# def test_get_battle_ship_get_damage(mocker):
#     att_battleground = Battleground(2)
#     positions = [[1,1], [0, 1]]
#     missile = Missile()
#     att_battleground.set_objects(positions, missile)

#     sut = Battleground(2)
#     positions = [[0,0], [0, 1]]
#     battle_ship = Battleship()
#     sut.set_objects(positions, battle_ship)

#     sut.get_battle_with(att_battleground)

#     assert 1 == sut.get_remaining_power()
#     assert 0 == sut.map[0][1].health
#     assert 1 == sut.map[0][0].health