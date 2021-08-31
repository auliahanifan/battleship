from model.battleship import Battleship

def test_get_damage_health_change(mocker):
    sut = Battleship()
    sut.get_damage(3)

    assert sut.health == -2

def test_get_damage_health_not_change(mocker):
    sut = Battleship()
    sut.get_damage(1)
    sut.get_damage(20)

    assert sut.health == 0
