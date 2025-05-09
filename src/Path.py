

import math
import heapq

from src.Settings import *
from src.action.PawnMove import *


class Path:
    """
    Find path for pawn
    """

    def __init__(self, moves):
        self.moves = moves

    def length(self):
        """
        Number of moves needed to access path target
        """
        return len(self.moves)

    def startCoord(self):
        """
        Coordinates where the path starts from
        """
        return self.moves[0].fromCoord

    def endCoord(self):
        """
        Coordinates where the path ends
        """
        return self.moves[-1].toCoord

    def firstMove(self):
        """
        First move of the path, which is the next move for pawn
        """
        return self.moves[0]

    def __str__(self):
        return "[%s] -> %s" % (str(self.startCoord()), " -> ".join(map(lambda move: str(move.toCoord), self.moves)))

    def ManhattanDistance(fromCoord, toCoord):
        """
        Manhattan distance (l1 norm) between 2 coordinates (4-connectivity)
        """
        return abs(toCoord.col - fromCoord.col) + abs(toCoord.row - fromCoord.row)

    def ManhattanDistanceMulti(fromCoord, toCoords):
        """
        Minimal manhattan distance between one coordinate and a set of target coordinates
        """
        minManhattanDistance = math.inf
        for toCoord in toCoords:
            manhattanDistance = Path.ManhattanDistance(fromCoord, toCoord)
            if manhattanDistance < minManhattanDistance:
                minManhattanDistance = manhattanDistance
        return minManhattanDistance

    def BreadthFirstSearch(board, startCoord, endCoords, ignorePawns=False):
        """
        Path finding using breadth first search algorithm
        """
        global TRACE
        TRACE["Path.BreadthFirstSearch"] += 1
        root = PawnMove(None, startCoord)

        previousMoves = {startCoord: root}
        nextMoves = [root]
        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves
        while nextMoves:
            move = nextMoves.pop(0)
            for endCoord in endCoords:
                if move.toCoord == endCoord:
                    pathMoves = [move]
                    while move.fromCoord is not None:
                        move = previousMoves[move.fromCoord]
                        pathMoves.append(move)
                    pathMoves.reverse()
                    return Path(pathMoves[1:])
            validMoves = validPawnMoves[move.toCoord]
            sorted(validMoves, key=lambda validMove: Path.ManhattanDistanceMulti(validMove.toCoord, endCoords))
            for validMove in validMoves:
                if validMove.toCoord not in previousMoves:
                    previousMoves[validMove.toCoord] = validMove
                    nextMoves.append(validMove)
        return None

    def AStar(board, startCoord, endCoords, ignorePawns=False):
        """
        Path finding using A* algorithm with Manhattan distance heuristic
        """
        global TRACE
        TRACE["Path.AStar"] += 1

        def heuristic(coord):
            return min(Path.ManhattanDistance(coord, endCoord) for endCoord in endCoords)

        # Use a priority queue that stores tuples of (f_score, tiebreaker, coord)
        tiebreaker = 0
        open_set = []
        heapq.heappush(open_set, (0, tiebreaker, startCoord))
        tiebreaker += 1

        came_from = {}
        g_score = {startCoord: 0}
        f_score = {startCoord: heuristic(startCoord)}

        validPawnMoves = board.storedValidPawnMovesIgnoringPawns if ignorePawns else board.storedValidPawnMoves

        while open_set:
            current_f, _, current_coord = heapq.heappop(open_set)

            for endCoord in endCoords:
                if current_coord == endCoord:
                    path = []
                    while current_coord in came_from:
                        path.append(current_coord)
                        current_coord = came_from[current_coord]
                    path.reverse()
                    if not path:
                        return None
                    moves = []
                    prev_coord = startCoord
                    for coord in path:
                        moves.append(PawnMove(prev_coord, coord))
                        prev_coord = coord
                    return Path(moves)

            for move in validPawnMoves[current_coord]:
                neighbor = move.toCoord
                tentative_g_score = g_score[current_coord] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current_coord
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                    heapq.heappush(open_set, (f_score[neighbor], tiebreaker, neighbor))
                    tiebreaker += 1

        return None
