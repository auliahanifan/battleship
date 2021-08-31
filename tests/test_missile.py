from model.missile import Missile

def test_damage(mocker):
    sut = Missile()

    assert 1 == sut.damage