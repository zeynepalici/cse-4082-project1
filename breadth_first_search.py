from queue import Queue


class BFS:
    def __init__(self):
        self.frontier = Queue()
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
