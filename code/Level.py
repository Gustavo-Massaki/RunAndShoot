import sys

import pygame.event
from pygame import Surface, Rect

from pygame.font import Font

from code.Const import C_RED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        #player = EntityFactory.get_entity('Player')
        #player.score = 0
        #self.entity_list.append(player)

    def run(self,):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source= ent.surf, dest= ent.rect)
                ent.move()

                #if ent.name == 'Player':
                     #self.level_text(14, f'Player: {ent.health} | Score: {ent.score}', C_RED,(10,25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
    def level_text(self, text_size: int, text: str, text_color:tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)