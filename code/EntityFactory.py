import random

import pygame

from code.Background import Background
from code.Bullet import Bullet
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position = (0,0), target=None):
        match entity_name:
            case 'LevelBg':
                list_bg = []
                for i in range(2):
                    list_bg.append(Background(f'LevelBg{i}', (0,0)))
                    list_bg.append(Background(f'LevelBg{i}', (WIN_WIDTH , 0)))
                return list_bg
            case 'Player':
                return Player('Player',(100 ,WIN_HEIGHT / 2))
            case 'Bullet':
                return Bullet('Bullet', position, target)
            #case 'Enemy1':
                #return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))