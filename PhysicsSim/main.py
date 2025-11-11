import pygame


class GUI:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Physics Simulation")
        WIDTH, HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        clock = pygame.time.Clock()
        

    def start(self):
        print("Starting GUI...")
