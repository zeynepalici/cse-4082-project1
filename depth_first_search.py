from queue import LifoQueue


class DFS:
    def __init__(self):
        self.frontier = LifoQueue()
        self.maxLenOfFrontier = 0

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node)
        if self.getLengthOfFrontier() > self.maxLenOfFrontier:
            self.maxLenOfFrontier = self.getLengthOfFrontier()

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
