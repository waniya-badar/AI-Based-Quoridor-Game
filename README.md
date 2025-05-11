# AI-Based-Quoridor-Game
An Artificial Intelligence-powered implementation of the Quoridor board game using Python and Pygame. This game supports 2 and 4 players, including human and AI-controlled opponents. AI difficulty levels are based on different pathfinding algorithms.

#### Documentations
[AI Project Video Demo](https://drive.google.com/file/d/1hjCWxI9Ye2eJ3TWA7tDhzv1o-TxvwpvQ/view?usp=sharing)

[AI Project Report](https://drive.google.com/file/d/11TrHb0IiT9lvZiljO_qsrVVA4rb9jZ55/view?usp=sharing)

[AI Project Proposal](https://docs.google.com/document/d/1ndKIAqqc6xcQI3ykf3WHAUshuvmWsvdP/edit?usp=sharing&ouid=108623326638263762592&rtpof=true&sd=true)

#### Why was the project developed?
This project was developed as part of an AI lab course to practically apply concepts of artificial intelligence, particularly pathfinding algorithms, in a real-time strategic board game. The objective was to demonstrate how decision-making algorithms can be integrated into a user-interactive environment.

#### What does the project do?
- Allows users to play the board game Quoridor against human or AI players.
- Supports 2 and 4 players with dynamically adjusted turns.
- Integrates intelligent AI agents with difficulty levels using different algorithms.
- Provides visual and audio feedback for an engaging user experience.

#### How does it work?
- The game initializes a GUI-based board and allows players to take turns moving or placing fences.
- AI opponents evaluate the best possible move using the selected algorithm (BFS-easy and A*+BFS-hard).
- Players win by reaching the opposite side of the board while blocking others with fences.
  
#### How was it implemented?
- Language & Libraries: Python with pygame for graphics and sound.
- Board Logic: Represented as a grid with validation for legal movements and fence placements.
- Algorithms:
  - Breadth-First Search (BFS): Ensures the shortest available path.
  - A*: Heuristic-based pathfinding for intelligent decision-making.
- GUI: Draws grid, players, fences; handles real-time inputs and updates.
- Sound Effects: Triggered on player moves, fence placements, and game wins

#### What makes this project stand out?
- Unlike many simple AI projects, this game integrates multiple difficulty levels using different search algorithms, allowing a comparison of AI behaviors.
- The 4-player support and real-time GUI make it more interactive than typical 2-player board AI demos.
- Designed with modularity and extensibility in mind, new features or algorithms can be added with ease.
- Adds a complete user experience through game sounds, turn handling, and visual feedback.

#### Features
- Full-featured implementation of the classic Quoridor board game.
- Supports 2 and 4 players.
- Multiple AI difficulty levels:
  - Easy: BFS (Breadth-First Search)
  - Hard: A* Search Algorithm + BFS
- Intuitive GUI.
- Integrated sound effects for moves, wins, and fence placements.

#### Team Contributions:
Waniya Badar 22k-4526 — Implemented the core game engine, AI player logic (BFS, A*), and turn-based logic.

Alishba Hassan 22k-4333 — Designed and implemented the GUI using pygame, integrated sound effects, and managed user interactions.

Nimil Zubair 22k-4617 — Worked on testing, debugging, and documentations.

#### Installation
pip install pygame

#### Running the Game
###### 2 players with difficulty level: easy
python main.py --players=Alain:Human,Benoit:RunnerBot:easy   
###### 4 players with difficulty level: easy
python main.py --players=Alain:Human,Benoit:BuilderBot:easy,Caroline:RandomBot:easy,Daniel:RunnerBot:easy
###### 4 players with difficulty level: hard
python main.py --players=Alain:Human,Benoit:BuilderBot:hard,Caroline:RandomBot:hard,Daniel:RunnerBot:hard
