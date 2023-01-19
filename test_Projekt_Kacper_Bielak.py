from Projekt_Kacper_Bielak import Ball
import pytest
import pygame

def test_Ball_create(monkeypatch):
    ball = Ball(5, 5, True)
    def get_3(a):
        return 3
    monkeypatch.setattr("Projekt_Kacper_Bielak.randint", get_3)
    assert ball.x == 5 
    assert ball.y == 5 
    assert ball.infected == True
    assert ball.vx == 3
    assert ball.vy == 3
    