import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, C_BLACK, MENU_OPTION, C_RED, WIN_HEIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:

            mouse_pos = pygame.mouse.get_pos()
            option_rects = []

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Infinite", C_BLACK, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", C_BLACK, ((WIN_WIDTH / 2), 120))
            self.menu_text(20, "Space - jump", C_BLACK, ((WIN_WIDTH / 2), (WIN_HEIGHT - 40)))
            self.menu_text(20, "Mouse - shoot", C_BLACK, ((WIN_WIDTH / 2), (WIN_HEIGHT - 20)))
            for i in range(len(MENU_OPTION)):

                pos = ((WIN_WIDTH / 2), 200 + 25 * i)

                rect = self.menu_text(20, MENU_OPTION[i], C_BLACK, pos)

                if rect.collidepoint(mouse_pos):
                    rect = self.menu_text(22, MENU_OPTION[i], C_RED, pos)
                    menu_option = i

                option_rects.append(rect)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):

        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)

        self.window.blit(text_surf, text_rect)

        return text_rect