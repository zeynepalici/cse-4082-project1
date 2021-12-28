from A_star_search import A_StarSearch
from breadth_first_search import BFS
from greedy_best_first_search import GreedyBestFirstSearch
from uniform_cost_search import UniformCostSearch
from depth_first_search import DFS
from graph_search import GraphSearch
from IO import IO
from iterative_deepening_search import IterativeDeepeningSearch


def printOutputsOfGivenInput(filename):
    grid, goalNodes, startState = IO().readTheMazeInput(filename)

    print("DFS:")
    strategy1 = DFS()
    graphSearch1 = GraphSearch(strategy1, grid.copy(), startState, goalNodes)
    graphSearch1.search()
    print("Cost of the founded solution: " + str(graphSearch1.cost))
    print("The number of expanded nodes: " + str(len(graphSearch1.exploredSet)))
    print("The maximum size of the frontier: " + str(strategy1.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch1.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch1.printPath(graphSearch1.lastNode)
    print()

    print("BFS")
    strategy2 = BFS()
    graphSearch2 = GraphSearch(strategy2, grid.copy(), startState, goalNodes)
    graphSearch2.search()
    print("Cost of the founded solution: " + str(graphSearch2.cost))
    print("The number of expanded nodes: " + str(len(graphSearch2.exploredSet)))
    print("The maximum size of the frontier: " + str(strategy2.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch2.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch2.printPath(graphSearch2.lastNode)
    print()

    print("IDS")
    strategy3 = IterativeDeepeningSearch()
    graphSearch3 = GraphSearch(strategy3, grid.copy(), startState, goalNodes)
    graphSearch3.search()
    print("Cost of the founded solution: " + str(graphSearch3.cost))
    print("The number of expanded nodes: " + str(len(graphSearch3.IDS_exploredSet)))
    print("The maximum size of the frontier: " + str(strategy3.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch3.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch3.printPath(graphSearch3.lastNode)
    print()

    print("Uniform")
    strategy4 = UniformCostSearch()
    graphSearch4 = GraphSearch(strategy4, grid.copy(), startState, goalNodes)
    graphSearch4.search()
    print("Cost of the founded solution: " + str(graphSearch4.cost))
    print("The number of expanded nodes: " + str(len(graphSearch4.exploredSet)))
    print("The maximum size of the frontier: " + str(strategy4.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch4.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch4.printPath(graphSearch4.lastNode)
    print()

    print("Greedy")
    strategy5 = GreedyBestFirstSearch()
    graphSearch5 = GraphSearch(strategy5, grid.copy(), startState, goalNodes)
    graphSearch5.search()
    print("Cost of the founded solution: " + str(graphSearch5.cost))
    print("The number of expanded nodes: " + str(len(graphSearch5.exploredSet)))
    print("The maximum size of the frontier: " + str(strategy5.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch5.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch5.printPath(graphSearch5.lastNode)
    print()

    print("A*")
    strategy6 = A_StarSearch()
    graphSearch6 = GraphSearch(strategy6, grid.copy(), startState, goalNodes)
    graphSearch6.search()
    print("Cost of the founded solution: " + str(graphSearch6.cost))
    print("The number of expanded nodes: " + str(len(graphSearch6.exploredSet)))
    print("The maximum size of the frontier: " + str(strategy6.maxLenOfFrontier))
    print("The maximum size of the explored set: " + str(graphSearch6.maxLenOfExploredSet))
    print("Solution path: ")
    graphSearch6.printPath(graphSearch6.lastNode)
    print()


if __name__ == "__main__":
    print("GIVEN MAZE OUTPUTS")
    printOutputsOfGivenInput('given_input.json')
    print("-----------------------")
    print("-----------------------")
    print("CUSTOM MAZE OUTPUTS")
    printOutputsOfGivenInput('custom_input.json')
