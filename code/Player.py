

import pygame.key


from code.Const import ENTITY_SHOT_DELAY, PLAYER_KEY_JUMP, GRAVITY, WIN_HEIGHT
from code.Entity import Entity



class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name,position)
        self.frames = [
            pygame.transform.scale(pygame.image.load('./asset/player_walk1.png').convert_alpha(),(104,128)),
            pygame.transform.scale(pygame.image.load('./asset/player_walk2.png').convert_alpha(), (104, 128))
        ]
        self.frame_index = 0
        self.animation_speed = 0.1
        self.on_ground = True
        self.vel_y = 0
        #self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def update(self):
        self.frame_index += self.animation_speed

        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.surf = self.frames[int(self.frame_index)]

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        ground = WIN_HEIGHT - 50

        if pressed_key[PLAYER_KEY_JUMP[self.name]] and self.on_ground:
            self.vel_y = -50
            self.on_ground = False

        #Gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom >= ground:
            self.rect.bottom = ground
            self.vel_y = 0
            self.on_ground = True

    def shoot(self, target_pos):
        from code.EntityFactory import EntityFactory

        spawn_x = self.rect.centerx + 50
        spawn_y = self.rect.centery + 20
        bullet = EntityFactory.get_entity(
            'Bullet',
            (spawn_x, spawn_y),
            target_pos
        )
        return bullet
