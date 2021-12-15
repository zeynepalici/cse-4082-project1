from queue import LifoQueue


class DFS:
    def __init__(self):
        self.frontier = LifoQueue()

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, cost, node):
        self.frontier.put(node)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
