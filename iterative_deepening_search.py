from queue import LifoQueue


class IterativeDeepeningSearch:
    def __init__(self):
        self.frontier = LifoQueue()

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
