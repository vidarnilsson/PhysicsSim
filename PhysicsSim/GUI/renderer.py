import pygame

class Renderer:
    def __init__(self, surface):
        self.surface = surface

    def draw(self, snapshot, camera):
        # snapshot: immutable read-only view of world (positions, shapes)
        x, y = 40, 50

        pygame.draw.circle(self.surface, (40,40,40),(int(x), int(y)), int(20), 2)

        hw, hh = 100, 500
        rect = pygame.Rect(int(x - hw), int(y - hh), int(2*hw), int(2*hh))
        pygame.draw.rect(self.surface, (40,40,40), rect, 2)