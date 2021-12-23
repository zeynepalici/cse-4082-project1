from queue import Queue


class BFS:
    def __init__(self):
        self.frontier = Queue()

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
