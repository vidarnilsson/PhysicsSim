import pygame
# from PhysicsSim.Simulator.commands import SpawnCircle, SpawnBox, TogglePause

class InputMapper:
    def __init__(self, camera):
        self.camera = camera

    def handle_event(self, event):
        cmds = []
        if event.type == pygame.MOUSEBUTTONDOWN:
            world_pos = self.camera.screen_to_world(event.pos)
            print("Mouse click at world position:", world_pos)
            # if event.button == 1:
            #     cmds.append(SpawnCircle(world_pos))
            # elif event.button == 3:
            #     cmds.append(SpawnBox(world_pos))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # cmds.append(TogglePause())
                print("Toggle Pause Command Issued")
        return cmds