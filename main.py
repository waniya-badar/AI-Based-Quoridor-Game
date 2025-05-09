
import getopt
import random
from src.Settings              import *
from src.Game                  import *
from src.player.Human          import *
from src.player.RandomBot      import *
from src.player.RunnerBot      import *
from src.player.BuilderBot     import *
from src.player.BuildAndRunBot import *


PARAMETERS_ERROR_RETURN_CODE = 1

def printUsage():
    print("Usage: python quoridor.py [{-h|--help}] {-p|--players=}<PlayerName:PlayerType[:difficulty],...> [{-r|--rounds=}<roundCount>] [{-x|--cols=}<ColCount>] [{-y|--rows=}<RowCount>] [{-f|--fences=}<TotalFenceCount>] [{s|--square_size=}<SquareSizeInPixels>]")
    print("Example: python quoridor.py --players=Alain:Human,Benoit:BuilderBot:hard,Caroline:RandomBot,Daniel:RunnerBot:medium --square-size=32")


def readArguments():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:r:w:x:y:s:h",
                                   ["players=", "rounds=", "cols=", "rows=",
                                    "fences=", "square_size=", "help"])
    except getopt.GetoptError as err:
        print(err)
        printUsage()
        sys.exit(PARAMETERS_ERROR_RETURN_CODE)
    players = []
    rounds = 1
    cols = 9
    rows = 9
    totalFenceCount = 20
    squareSize = 32
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            printUsage()
            sys.exit(0)
        elif opt in ("-p", "--players"):
            for playerData in arg.split(","):
                parts = playerData.split(":")
                playerName = parts[0]
                playerType = parts[1]
                difficulty = "medium"  # default
                if len(parts) > 2:
                    difficulty = parts[2].lower()
                    if difficulty not in ["easy", "medium", "hard"]:
                        difficulty = "medium"

                if playerType not in globals():
                    print("Unknown player type %s. Abort." % (playerType))
                    sys.exit(PARAMETERS_ERROR_RETURN_CODE)

                # Create bot with difficulty level
                if playerType in ["RunnerBot", "BuilderBot", "BuildAndRunBot"]:
                    players.append(globals()[playerType](playerName, None, difficulty))
                else:
                    players.append(globals()[playerType](playerName))

            if len(players) not in (2, 4):
                print("Expect 2 or 4 players. Abort.")
                sys.exit(PARAMETERS_ERROR_RETURN_CODE)
        elif opt in ("-r", "--rounds"):
            rounds = int(arg)
        elif opt in ("-x", "--cols"):
            cols = int(arg)
        elif opt in ("-y", "--rows"):
            rows = int(arg)
        elif opt in ("-f", "--fences"):
            totalFenceCount = int(arg)
        elif opt in ("-s", "--square_size"):
            squareSize = int(arg)
        else:
            print("Unhandeld option. Abort.")
            sys.exit(PARAMETERS_ERROR_RETURN_CODE)
    return players, rounds, cols, rows, totalFenceCount, squareSize

def main():
    """
    Main function of quoridor.
    Create a game instance and launch game rounds.
    """
    players, rounds, cols, rows, totalFenceCount, squareSize = readArguments()

    game = Game(players, cols, rows, totalFenceCount, squareSize)
    game.start(rounds)
    game.end()

    global TRACE
    print("TRACE")
    for i in TRACE:
    	print("%s: %s" % (i, TRACE[i]))

main()
