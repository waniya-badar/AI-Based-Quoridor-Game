

import random
import time

from src.player.BuilderBot import *
from src.player.RunnerBot import *
from src.action.IAction import *


class BuildAndRunBot(BuilderBot, RunnerBot):
    def __init__(self, name=None, color=None, difficulty="medium"):
        super().__init__(name, color)
        self.difficulty = difficulty.lower()

    def play(self, board) -> IAction:
        # If no fence left, move pawn
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveAlongTheShortestPath(board)

        fencePlacingImpacts = self.computeFencePlacingImpacts(board)

        # If no valid fence placing, move pawn
        if len(fencePlacingImpacts) < 1:
            return self.moveAlongTheShortestPath(board)

        # Choose fence placing with the greatest impact
        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)

        # For hard difficulty, sometimes choose a suboptimal fence to make the game more interesting
        if self.difficulty == "hard" and random.random() < 0.1 and len(fencePlacingImpacts) > 1:
            sorted_fences = sorted(fencePlacingImpacts.items(), key=lambda x: x[1], reverse=True)
            if len(sorted_fences) > 1 and sorted_fences[0][1] - sorted_fences[1][1] < 3:
                bestFencePlacing = sorted_fences[1][0]

        # If impact is not positive, move pawn
        if bestFencePlacing is None or fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveAlongTheShortestPath(board)

        return bestFencePlacing

