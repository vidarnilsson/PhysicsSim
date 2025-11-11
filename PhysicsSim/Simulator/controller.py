class Controller:
    def __init__(self, world):
        self.world = world
        self._queue = []

    def enqueue(self, cmd):
        """GUI calls this with commands (e.g., SpawnCircle(...))."""
        self._queue.append(cmd)

    def advance(self, real_dt):
        """Called once per GUI frame. We'll fill this later."""
        pass

    def get_snapshot(self):
        """Return lightweight data the GUI can draw. Stub for now."""
        return {"bodies": getattr(self.world, "bodies", [])}