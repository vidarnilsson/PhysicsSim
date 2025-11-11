import pygame

from renderer import Renderer
from input import InputMapper
from camera import Camera


class Gui:
    def __init__(self, controller, width=800, height=600):
        pygame.init()
        pygame.display.set_caption("Physics Simulation")
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()


        self.controller = controller
        self.renderer = Renderer(self.screen)
        self.camera = Camera(width, height)
        self.user_input = InputMapper(controller)

        self.running = True

    def run(self):
        while self.running:
            frame_time = self.clock.tick(120) / 1000.0  # seconds

            # --- Input & Events ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                #TODO:
                # commands = self.user_input.handle_event(event)
                # for cmd in commands:
                #     self.controller.enqueue(cmd)

            # --- Simulation ---
            self.controller.advance(frame_time)

            # --- Rendering ---
            snapshot = self.controller.get_snapshot()
            self.screen.fill((240, 240, 245))
            # self.renderer.draw(snapshot, self.camera)
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    Gui(controller=Controller, width=800, height=600).run()