import pygame

class Renderer:
    def __init__(self, surface):
        self.surface = surface

    def draw(self, snapshot, camera):
        # snapshot: immutable read-only view of world (positions, shapes)
        for body in snapshot.bodies:
            x, y = camera.world_to_screen(body.pos)
            if body.shape_type == "circle":
                pygame.draw.circle(self.surface, (40,40,40),
                                   (int(x), int(y)), int(body.radius), 2)
            elif body.shape_type == "aabb":
                hw, hh = body.half_size
                rect = pygame.Rect(int(x - hw), int(y - hh), int(2*hw), int(2*hh))
                pygame.draw.rect(self.surface, (40,40,40), rect, 2)