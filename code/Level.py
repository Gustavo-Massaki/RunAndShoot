import sys
from random import random

import pygame.event
from pygame import Surface, Rect

from pygame.font import Font

from code.Const import C_RED, WIN_HEIGHT, EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, player_score: int):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)
        self.player.score = player_score
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self,):
        pygame.mixer_music.load(f'./asset/Level.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.window.fill((0,0,0))

            for ent in self.entity_list:
                ent.update()
                ent.move()
                self.window.blit(source= ent.surf, dest= ent.rect)

                if ent.name == 'Player':
                    self.level_text(14, f'Player: {ent.health} | Score: {ent.score}', C_RED,(10,25))
            EntityMediator.verify_collision(self.entity_list)
            EntityMediator.verify_health(self.entity_list)

            if self.player.health <= 0:
                return self.player.score

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('Enemy'))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mx, my = pygame.mouse.get_pos()
                        bullet = self.player.shoot((mx ,my ))
                        self.entity_list.append(bullet)


            self.level_text(14, f'entidades: {len(self.entity_list)}', C_RED, (10, WIN_HEIGHT - 20))
            pygame.display.flip()




    def level_text(self, text_size: int, text: str, text_color:tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size= text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)