import pygame

#C

C_BLACK = (28, 28, 28)
C_RED = (255, 0, 0)

#E

ENTITY_DAMAGE = {
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player': 0,
    'Enemy': 1,
    'Bullet': 1

}

ENTITY_HEALTH = {
    'LevelBg0': 999,
    'LevelBg1': 999,
    'Player': 999,
    'Bullet': 1,
    'Enemy': 3
}

ENTITY_SCORE = {
    'LevelBg0': 0,
    'LevelBg1': 0,
    'Player': 0,
    'Enemy': 3
}

ENTITY_SHOT_DELAY = {
    'Player': 20,
}

ENTITY_SPEED = {
    'LevelBg0': 4,
    'LevelBg1': 7,
    'Player': 2,
    'Enemy': 10
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

#G

GRAVITY = 0.5

#J

JUMP_FORCE = 15

#M

MENU_OPTION = (
    'PLAY',
    'SCORE',
    'EXIT',
)

#P

PLAYER_KEY_JUMP ={'Player': pygame.K_SPACE}

#S

SPAWN_TIME = 4000

#W

WIN_WIDTH = 800
WIN_HEIGHT = 400

#S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
}