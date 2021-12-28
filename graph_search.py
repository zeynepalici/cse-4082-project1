from A_star_search import A_StarSearch
from greedy_best_first_search import GreedyBestFirstSearch
from iterative_deepening_search import IterativeDeepeningSearch
from queue import LifoQueue


class GraphSearch:
    def __init__(self, strategy, grid, startState, goalNodes):
        self.strategy = strategy
        self.grid = grid
        self.startState = startState
        self.cost = 0
        self.exploredSet = []
        self.lastNode = None
        self.goalNodes = goalNodes
        self.maxDepth = 0
        self.currentDepth = 0
        self.IDS_exploredSet = []
        self.maxLenOfExploredSet = 0

    def expandNode(self, curr_node):
        expandedNodes = []
        # east
        if not curr_node.eastWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex][curr_node.horizontalIndex + 1])
        # south
        if not curr_node.southWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex + 1][curr_node.horizontalIndex])
        # west
        if not curr_node.westWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex][curr_node.horizontalIndex - 1])
        # north
        if not curr_node.northWall:
            expandedNodes.append(self.grid[curr_node.verticalIndex - 1][curr_node.horizontalIndex])

        return expandedNodes

    def checkInNotFrontierOrExploredSet(self, nextNode):
        if nextNode in self.exploredSet:
            return False

        if nextNode in self.strategy.getAllFrontier():
            return False
        return True

    def search(self):

        if isinstance(self.strategy, (A_StarSearch, GreedyBestFirstSearch)):
            self.strategy.calculateHeuristicValues(self.grid, self.goalNodes)

        self.strategy.append(self.grid[self.startState[0]][self.startState[1]])

        while True:
            if self.strategy.getLengthOfFrontier() == 0:
                return "Failure"

            curr_node = self.strategy.operate()

            if curr_node.status == "G":
                self.IDS_exploredSet.append(curr_node)
                self.cost = curr_node.cost
                self.lastNode = curr_node
                return "Goal"

            self.exploredSet.append(curr_node)
            if len(self.exploredSet) > self.maxLenOfExploredSet:
                self.maxLenOfExploredSet = len(self.exploredSet)

            # if the state is start state, start the path from beginning.
            # this part may be unnecessary, i put in a comment for now - Furkan
            '''if self.grid[node_row][node_col].status == "S":
                self.cost = 0
                self.path = [[node_row, node_col]]'''

            # expand the node and add resulting nodes to the frontier
            expandedNodes = self.expandNode(curr_node)

            IDS = isinstance(self.strategy, IterativeDeepeningSearch)
            if not IDS or (IDS and self.currentDepth <= self.maxDepth):
                for nextNode in expandedNodes:
                    if self.checkInNotFrontierOrExploredSet(nextNode):
                        if nextNode.status == "T":
                            nextNode.cost = curr_node.cost + 10
                        else:
                            nextNode.cost = curr_node.cost + 1
                        nextNode.successor = curr_node
                        self.strategy.append(nextNode)
                self.currentDepth += 1
            else:
                self.IDS_exploredSet = self.IDS_exploredSet + self.exploredSet
                self.strategy.frontier = LifoQueue()
                self.cost = 0
                for row in self.grid:
                    for node in row:
                        node.successor = None
                self.exploredSet = []
                self.lastNode = None

                self.currentDepth = 0
                self.maxDepth += 1
                return self.search()

    def printPath(self, node):
        if node.successor is not None:
            self.printPath(node.successor)
            print("-(" + str(node.horizontalIndex + 1) + "," + str(node.verticalIndex + 1) + ")", end="")
        else:
            print("(" + str(node.horizontalIndex + 1) + "," + str(node.verticalIndex + 1) + ")", end="")

    def printExploredSet(self):
        for node in self.exploredSet:
            print("(" + str(node.horizontalIndex + 1) + "," + str(node.verticalIndex + 1) + ")", end=" ")

    def printIterativeDeepeningExploredSet(self):
        for node in self.IDS_exploredSet:
            print("(" + str(node.horizontalIndex + 1) + "," + str(node.verticalIndex + 1) + ")", end=" ")
