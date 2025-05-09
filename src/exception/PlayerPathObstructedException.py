

from src.player.IPlayer      import *
from src.action.FencePlacing import *



class PlayerPathObstructedException(Exception):
        def __init__(self, player: IPlayer, fencePlacing: FencePlacing = None):
            self.message = "Path of player %s is obstructed" % (player)
            if fencePlacing is not None:
                self.message += "by %s" % (fencePlacing)
