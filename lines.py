import pygame


class Lines():
    def __init__(self, screen):
        self.line_color = (60, 60, 60)
        self.screen = screen
        #for i in range(600):


    def draw(self):
        pygame.draw.rect(self.screen, self.line_color, (300, 560, 20, 20))
