
import json
from node import Node
class IO:

    def readTheMazeInput(self, fileName):

        f =open(fileName)
        data = json.load(f)
        nodes = data["nodes"]
        horizontal = data["horizontal"]
        goalSquares = []
        nodeList = []
        nodeRow = []
        j = 0
        i = 0
        for node in nodes:
            nodeRow.append(Node(node["status"], node["eastWall"]
                                , node["westWall"], node["northWall"]
                                , node["southWall"], j, i))
            i += 1
            if nodeRow[-1].status == 'G':
                goalSquares.append(nodeRow[-1])
            if i == horizontal:
                nodeList.append(nodeRow.copy())
                nodeRow.clear()
                i = 0
                j += 1
        return nodeList, goalSquares