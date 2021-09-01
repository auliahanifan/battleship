from model.battleship import Battleship

def test_get_damage_health_change(mocker):
    sut = Battleship()
    sut.get_damage(3)

    assert sut.health == 0

def test_get_damage_health_not_change_if_minus(mocker):
    sut = Battleship()
    sut.get_damage(1)

    # this method not works
    sut.get_damage(20)

    assert sut.health == 0
