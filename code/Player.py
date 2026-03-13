import pygame.key

from code.Const import ENTITY_SHOT_DELAY
from code.Entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name,position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        pass
