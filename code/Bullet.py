from code.Entity import Entity


class Bullet(Entity):
    def __init__(self,name, position, target):
        super().__init__(name,position)

        self.rect.center = position
        dir_x = target[0] - self.rect.centerx
        dir_y = target[1] - self.rect.centery

        lenght = (dir_x**2 + dir_y**2) ** 0.5

        dir_x /= lenght
        dir_y /= lenght

        speed = 10
        self.vel_x = dir_x * speed
        self.vel_y = dir_y * speed

    def move(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def update(self):
        pass