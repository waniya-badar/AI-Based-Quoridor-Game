

from src.player.IBot import *
from src.action.IAction import *
from src.Path import *
import random


class RunnerBot(IBot):
    def __init__(self, name=None, color=None, difficulty="medium"):
        super().__init__(name, color)
        self.difficulty = difficulty.lower()

    def moveAlongTheShortestPath(self, board) -> IAction:
        # Easy difficulty uses optimized BFS with direct path checking
        if self.difficulty == "easy":
            # First try without ignoring pawns for optimal path
            path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns=False)

            # If no path found, try ignoring pawns
            if path is None:
                path = Path.BreadthFirstSearch(board, self.pawn.coord, self.endPositions, ignorePawns=True)

            # If path found and we're close to winning, take it
            if path:
                min_dist = min(Path.ManhattanDistance(self.pawn.coord, end) for end in self.endPositions)
                if min_dist <= 3 or random.random() > 0.2:  # 80% chance to follow path when not close
                    first_move = path.firstMove()
                    if board.isValidPawnMove(first_move.fromCoord, first_move.toCoord, ignorePawns=False):
                        return first_move

        # Hard difficulty uses optimized A* algorithm
        elif self.difficulty == "hard":
            # First try without ignoring pawns
            path = Path.AStar(board, self.pawn.coord, self.endPositions, ignorePawns=False)

            # If no path found, try ignoring pawns
            if path is None:
                path = Path.AStar(board, self.pawn.coord, self.endPositions, ignorePawns=True)

            # If path found, consider both path and blocking moves
            if path:
                min_dist = min(Path.ManhattanDistance(self.pawn.coord, end) for end in self.endPositions)
                if min_dist <= 4:  # If close to goal, prioritize our path
                    first_move = path.firstMove()
                    if board.isValidPawnMove(first_move.fromCoord, first_move.toCoord, ignorePawns=False):
                        return first_move

                # Otherwise consider blocking moves
                valid_moves = board.storedValidPawnMoves[self.pawn.coord]
                if valid_moves:
                    best_move = None
                    best_score = -float('inf')

                    for move in valid_moves:
                        score = 0
                        # Progress towards our goal
                        new_dist = min(Path.ManhattanDistance(move.toCoord, end) for end in self.endPositions)
                        score += (min_dist - new_dist) * 2

                        # Temporary move to evaluate opponent paths
                        original_coord = self.pawn.coord
                        self.pawn.coord = move.toCoord

                        for player in board.game.players:
                            if player != self:
                                opp_path = Path.AStar(board, player.pawn.coord, player.endPositions)
                                if opp_path:
                                    score += opp_path.length() * 0.5

                        self.pawn.coord = original_coord

                        if score > best_score:
                            best_score = score
                            best_move = move

                    if best_move:
                        return best_move

        # Medium difficulty or fallback
        else:
            path = Path.AStar(board, self.pawn.coord, self.endPositions, ignorePawns=False)
            if path is None:
                path = Path.AStar(board, self.pawn.coord, self.endPositions, ignorePawns=True)

        # Return the first move if valid path found
        if path is not None:
            first_move = path.firstMove()
            if board.isValidPawnMove(first_move.fromCoord, first_move.toCoord, ignorePawns=False):
                return first_move

        # Fallback to random valid move
        valid_moves = board.storedValidPawnMoves[self.pawn.coord]
        if valid_moves:
            return random.choice(valid_moves)
        return None

    def play(self, board) -> IAction:
        return self.moveAlongTheShortestPath(board)