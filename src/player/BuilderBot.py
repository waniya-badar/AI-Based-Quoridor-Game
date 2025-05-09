

import random
import time

from src.player.RandomBot import *
from src.action.IAction import *
from src.exception.PlayerPathObstructedException import *


class BuilderBot(RandomBot):
    def __init__(self, name=None, color=None, difficulty="medium"):
        super().__init__(name, color)
        self.difficulty = difficulty.lower()

    def computeFencePlacingImpacts(self, board):
        fencePlacingImpacts = {}
        for fencePlacing in board.storedValidFencePlacings:
            try:
                impact = board.getFencePlacingImpactOnPaths(fencePlacing)
            except PlayerPathObstructedException as e:
                continue

            globalImpact = 0
            for playerName in impact:
                # Adjust impact based on difficulty
                if self.difficulty == "easy":
                    weight = 0.5 if playerName == self.name else 1.0
                elif self.difficulty == "medium":
                    weight = 0.7 if playerName == self.name else 1.3
                else:  # hard
                    weight = 0.9 if playerName == self.name else 1.5

                globalImpact += (-weight if playerName == self.name else weight) * impact[playerName]

            fencePlacingImpacts[fencePlacing] = globalImpact

        return fencePlacingImpacts

    def getFencePlacingWithTheHighestImpact(self, fencePlacingImpacts):
        if not fencePlacingImpacts:
            return None

        # For easy difficulty, sometimes choose randomly
        if self.difficulty == "easy" and random.random() < 0.4:
            return random.choice(list(fencePlacingImpacts.keys()))

        return max(fencePlacingImpacts, key=fencePlacingImpacts.get)

    def play(self, board) -> IAction:
        if self.remainingFences() < 1 or len(board.storedValidFencePlacings) < 1:
            return self.moveRandomly(board)

        fencePlacingImpacts = self.computeFencePlacingImpacts(board)
        if len(fencePlacingImpacts) < 1:
            return self.moveRandomly(board)

        bestFencePlacing = self.getFencePlacingWithTheHighestImpact(fencePlacingImpacts)
        if bestFencePlacing is None or (self.difficulty == "easy" and random.random() < 0.3):
            return self.moveRandomly(board)

        if fencePlacingImpacts[bestFencePlacing] < 1:
            return self.moveRandomly(board)

        return bestFencePlacing

