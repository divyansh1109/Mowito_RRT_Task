class RRTNode:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.parent = None
        self.children = []