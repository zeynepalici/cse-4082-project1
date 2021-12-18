from queue import PriorityQueue


class A_StarSearch:
    def __init__(self):
        self.frontier = PriorityQueue()

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node, self.getHeuristicValue(node) + node.cost)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        return list(self.frontier.queue)

    def getHeuristicValue(self, node):
        pass
