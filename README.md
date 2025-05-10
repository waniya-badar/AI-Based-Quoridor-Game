# AI-Based-Quoridor-Game
An Artificial Intelligence-powered implementation of the Quoridor board game using Python and Pygame. This game supports 2 and 4 players, including human and AI-controlled opponents. AI difficulty levels are based on different pathfinding algorithms.

#### Documentations
[AI Project Video Demo](https://drive.google.com/file/d/1B1LBEiAZ91TOKkLZ95AXbCFne00hOj7C/view?usp=sharing)

[AI Project Report](https://drive.google.com/file/d/11TrHb0IiT9lvZiljO_qsrVVA4rb9jZ55/view?usp=sharing)

[AI Project Proposal](https://docs.google.com/document/d/1ndKIAqqc6xcQI3ykf3WHAUshuvmWsvdP/edit?usp=sharing&ouid=108623326638263762592&rtpof=true&sd=true)

#### Features
- Full-featured implementation of the classic Quoridor board game.
- Supports 2 and 4 playersI.
- Multiple AI difficulty levels:
Easy: BFS (Breadth-First Search)
Hard: A* Search Algorithm + BFS
- Intuitive GUI.
- Integrated sound effects for moves, wins, and fence placements.

#### Installation
pip install pygame

#### Running the Game
###### 2 players with difficulty level: easy
python main.py --players=Alain:Human,Benoit:RunnerBot:easy   
###### 4 players with difficulty level: easy
python main.py --players=Alain:Human,Benoit:BuilderBot:easy,Caroline:RandomBot:easy,Daniel:RunnerBot:easy
###### 4 players with difficulty level: hard
python main.py --players=Alain:Human,Benoit:BuilderBot:hard,Caroline:RandomBot:hard,Daniel:RunnerBot:hard
