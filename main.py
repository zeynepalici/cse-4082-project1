from breadth_first_search import BFS
from node import Node
from graph_search import GraphSearch

if __name__ == "__main__":
    grid = [[Node("S", False, False, False, False), Node("N", True, False, False, False),
             Node("N", False, True, False, False), Node("N", False, False, False, True),
             Node("N", False, False, False, False), Node("N", False, False, False, True),
             Node("S", False, False, False, True), Node("N", False, False, False, False)],
            [Node("N", True, False, False, False), Node("N", False, True, False, True),
             Node("N", False, False, False, True), Node("T", True, False, True, False),
             Node("N", True, True, False, False), Node("N", False, True, True, False),
             Node("N", False, False, True, False), Node("G", False, False, False, False)]]

    startState = [0, 0]
    strategy = BFS()
    graphSearch = GraphSearch(strategy, grid, startState)

    message = graphSearch.search()
    print(message)
    print(graphSearch.cost)
    print(graphSearch.path)
    print(graphSearch.exploredSet)
