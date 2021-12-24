from breadth_first_search import BFS
from uniform_cost_search import UniformCostSearch
from depth_first_search import DFS
from node import Node
from graph_search import GraphSearch
from IO import IO
from iterative_deepening_search import IterativeDeepeningSearch

if __name__ == "__main__":
    grid, goalNodes = IO().readTheMazeInput("input.json")

    startState = [0, 0]
    strategy = IterativeDeepeningSearch()
    graphSearch = GraphSearch(strategy, grid.copy(), startState, goalNodes)

    message = graphSearch.search()
    print(message)
    print(graphSearch.cost)
    graphSearch.printPath(graphSearch.lastNode)
    print()
    graphSearch.printExploredSet()
    print()

    strategy2 = UniformCostSearch()
    graphSearch2 = GraphSearch(strategy2, grid.copy(), startState, goalNodes)
    message2 = graphSearch2.search()
    print(message2)
    print(graphSearch2.cost)
    graphSearch2.printPath(graphSearch2.lastNode)
    print()
    graphSearch2.printExploredSet()
    print(len(graphSearch2.exploredSet))
