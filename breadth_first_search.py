from collections import deque


class BFS:
    def __init__(self):
        self.frontier = deque()

    def operate(self):
        node = self.frontier.pop()
        return node
