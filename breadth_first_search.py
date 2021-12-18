from collections import deque


class BFS:
    def __init__(self):
        self.frontier = deque()

    def operate(self):
        node = self.frontier.pop()
        return node

    def append(self, node):
        self.frontier.append(node)

    def getLengthOfFrontier(self):
        return len(self.frontier)

    def getAllFrontier(self):
        return list(self.frontier)
