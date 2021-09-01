from model.missile import Missile
from model.battleship import Battleship
from model.player import Player
from model.battleground import Battleground

def test_get_current_def_battleground_map(mocker):
    def_battleground = Battleground(2)
    positions = [[1,1], [0, 1]]
    ship = Battleship()
    def_battleground.set_objects(positions, ship)

    sut = Player(def_battleground, None)
    
    assert def_battleground.show_map() == sut.get_current_def_battleground_map()

def test_attack(mocker):
    def_battleground = Battleground(2)
    positions = [[1,1], [0, 1]]
    ship = Battleship()
    def_battleground.set_objects(positions, ship)

    att_battleground = Battleground(2)
    positions = [[1,1], [0, 1]]
    missile = Missile()
    att_battleground.set_objects(positions, missile)

    opponent = Player(def_battleground, None)
    sut = Player(None, att_battleground)

    sut.attack(opponent)

    assert 0 == opponent.healths



