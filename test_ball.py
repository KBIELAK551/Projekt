from ball import Ball


def test_Ball_create(monkeypatch):

    def get_3(a, b):
        return 3
    monkeypatch.setattr('ball.randint', get_3)
    ball = Ball(5, 5, True)
    assert ball.x == 5
    assert ball.y == 5
    assert ball.infected is True
    assert ball.vx == 3
    assert ball.vy == 3 