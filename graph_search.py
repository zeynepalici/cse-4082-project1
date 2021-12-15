class GraphSearch:
    def __init__(self, strategy, grid, startState):
        self.strategy = strategy
        self.grid = grid
        self.startState = startState

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

    def checkInNotFrontierOrExploredSet(self, row, col, exploredSet):
        for [i, j] in exploredSet:
            if i == row and j == col:
                return False
        for [i, j] in self.strategy.frontier:
            if i == row and j == col:
                return False
        return True

    def search(self):
        exploredSet = []
        self.strategy.frontier.append(self.startState)

        while True:
            if len(self.strategy.frontier) == 0:
                return "Failure"

            node_row, node_col = self.strategy.operate()
            exploredSet.append([node_row, node_col])
            if self.grid[node_row][node_col].status == "G":
                return "Goal"

            # expand the node and add resulting nodes to the frontier
            expandedNodes = self.expandNode(node_row, node_col)

            for [row, col] in expandedNodes:
                if self.checkInNotFrontierOrExploredSet(row, col, exploredSet):
                    self.strategy.frontier.append([row, col])
