class GraphSearch:
    def __init__(self, strategy, grid, startState):
        self.strategy = strategy
        self.grid = grid
        self.startState = startState
        self.path = []
        self.cost = 0
        self.exploredSet = []

    def expandNode(self, row, col):
        expandedNodes = []
        # south
        if row + 1 < len(self.grid):
            expandedNodes.append([row + 1, col])
        # east
        if col + 1 < len(self.grid[0]):
            expandedNodes.append([row, col + 1])
        # north
        if row - 1 > 0:
            expandedNodes.append([row - 1, col])
        # west
        if col - 1 > 0:
            expandedNodes.append([row, col - 1])

        return expandedNodes

    def checkInNotFrontierOrExploredSet(self, row, col):
        for [i, j] in self.exploredSet:
            if i == row and j == col:
                return False
        for [i, j] in self.strategy.getAllFrontier():
            if i == row and j == col:
                return False
        return True

    def search(self):
        self.strategy.append(self.cost, self.startState)

        while True:
            if self.strategy.getLengthOfFrontier() == 0:
                return "Failure"

            node_row, node_col = self.strategy.operate()
            self.exploredSet.append([node_row, node_col])
            self.path.append([node_row, node_col])

            if self.grid[node_row][node_col].status == "G":
                self.cost += 1
                return "Goal"

            # if the state is start state, start the path from beginning.
            if self.grid[node_row][node_col].status == "S":
                self.cost = 0
                self.path = [[node_row, node_col]]

            if self.grid[node_row][node_col].status == "N":
                self.cost += 1

            if self.grid[node_row][node_col].status == "T":
                self.cost -= 8

            # expand the node and add resulting nodes to the frontier
            expandedNodes = self.expandNode(node_row, node_col)

            for [row, col] in expandedNodes:
                if self.checkInNotFrontierOrExploredSet(row, col):
                    self.strategy.append(self.cost, [row, col])
