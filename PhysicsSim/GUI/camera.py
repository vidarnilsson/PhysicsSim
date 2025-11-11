class Camera:
    def __init__(self, width, height, zoom=1.0):
        self.offset = [0, 0]
        self.zoom = zoom
        self.screen_center = (width // 2, height // 2)

    def world_to_screen(self, pos):
        return (self.screen_center[0] + (pos[0] + self.offset[0]) * self.zoom,
                self.screen_center[1] - (pos[1] + self.offset[1]) * self.zoom)

    def screen_to_world(self, pos):
        return ((pos[0] - self.screen_center[0]) / self.zoom - self.offset[0],
                -(pos[1] - self.screen_center[1]) / self.zoom - self.offset[1])