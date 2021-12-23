from queue import PriorityQueue


class GreedyBestFirstSearch:
    def __init__(self):
        self.frontier = PriorityQueue()

    def operate(self):
        node = self.frontier.get()
        return node

    def append(self, node):
        self.frontier.put(node, node.heuristicCost)

    def getLengthOfFrontier(self):
        return self.frontier.qsize()

    def getAllFrontier(self):
        retList = []
        priorityQIterator = list(self.frontier.queue)
        for frtNode in priorityQIterator:
            retList.append(frtNode[1])
        return retList


def calculateHeuristicValues(self, grid, goalSquares):
    for node in grid:
        for goalNode in goalSquares:
            total = abs(node.verticalIndex - goalNode.verticalIndex) + abs(node.horizontalIndex - goalNode
                                                                           .horizontalIndex)
            if total < node.heuristicCost:
                node.heuristicCost = total
