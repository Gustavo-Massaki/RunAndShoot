import pygame

#C

C_BLACK = (28, 28, 28)
C_RED = (255, 0, 0)

#E

ENTITY_DAMAGE = {
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player': 1,
}

ENTITY_HEALTH = {
    'LevelBg0': 999,
    'LevelBg1': 999,
    'Player': 999,
    'Bullet': 1
}

ENTITY_SCORE = {
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player': 0,
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
}

ENTITY_SPEED = {
    'LevelBg0': 4,
    'LevelBg1': 7,
    'Player': 2,
}

#G

GRAVITY = 5

#M

MENU_OPTION = (
    'PLAY',
    'SCORE',
    'EXIT',
)

#P

PLAYER_KEY_JUMP ={'Player': pygame.K_SPACE}

#W

WIN_WIDTH = 800
WIN_HEIGHT = 400