from queue import PriorityQueue


class UniformCostSearch:
    def __init__(self):
        self.frontier = PriorityQueue()
        self.maxLenOfFrontier = 0

    def operate(self):
        node = self.frontier.get()
        return node[1]

    def append(self, node):
        self.frontier.put((node.cost, node))
        if self.getLengthOfFrontier() > self.maxLenOfFrontier:
            self.maxLenOfFrontier = self.getLengthOfFrontier()

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        retList = []
        priorityQIterator = list(self.frontier.queue)
        for frtNode in priorityQIterator:
            retList.append(frtNode[1])
        return retList
