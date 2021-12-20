from queue import PriorityQueue


class UniformCostSearch:
    def __init__(self):
        self.frontier = PriorityQueue()

    def operate(self):
        node = self.frontier.get()
        return node[1]

    def append(self, node):
        self.frontier.put((node.cost, node))

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)
