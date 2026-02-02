# Python Snake Game

A small, classic Snake game written in Python using the standard turtle module. This repository contains a simple, single-player implementation with score tracking and persistence to a local file.

<img width="599" height="626" alt="image" src="https://github.com/user-attachments/assets/ab5f005c-9420-47b8-92ac-4e81f2d03ee5" />

## Table of Contents
- [Preview](#preview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the game](#running-the-game)
- [Controls and Gameplay](#controls-and-gameplay)
- [Project Structure](#project-structure)
- [How scoring and persistence work](#how-scoring-and-persistence-work)
- [Tips, troubleshooting & common issues](#tips-troubleshooting--common-issues)
- [Development & Ideas for improvement](#development--ideas-for-improvement)
- [Contributing](#contributing)
- [License](#license)

## Preview
This is a small GUI game that runs with turtle and tkinter. Use the arrow keys to move the snake, eat food to increase score, and avoid colliding with walls or your tail.

## Requirements
- Python 3.x (3.6+ recommended)
- The project uses only the Python standard library but depends on tkinter (used by turtle). On many systems tkinter is included, but on some (especially minimal Linux installs) you may need to install it (e.g., `sudo apt install python3-tk` on Debian/Ubuntu).
- A graphical desktop environment (turtle opens a window; it will not run on headless servers without an X server).

## Installation
Clone the repository (if needed):
```bash
git clone https://github.com/sriram2k3/python-course-projects.git
cd python-course-projects
```

No further package installation is needed.

## Running the game
Important: the scoreboard implementation opens `score_data.txt` using a relative path. To run the game with the existing files as-is, run the main script from the snake_game directory so the score file can be found.

From the repository root:
```bash
cd snake_game
python main.py
```

Alternatively, if you prefer to run directly from the repository root without changing the working directory, you can modify the code to use an absolute path to `score_data.txt` (see the section "Make high-score file path robust" below).

## Controls and Gameplay
- Arrow keys: move the snake
  - Up: move up (if not directly moving down)
  - Down: move down (if not directly moving up)
  - Left: turn left (if not directly moving right)
  - Right: turn right (if not directly moving left)
- Eat the red food to increase your score by 1 and grow the snake by one segment.
- Collision with the walls (window edges) or with the snake's own tail ends the game.
- When the game ends, the scoreboard checks if you have a new high score and updates `score_data.txt`.

## Project Structure
- snake_game/
  - main.py — entry point; screen setup, input handling, main loop
  - Snake.py — Snake class: creates segments, handles movement, turning, collision detection, and adding segments
  - food.py — Food class: spawns food and detects when the snake eats it
  - scoreboard.py — Scoreboard class: displays the current score and persists the high score to `score_data.txt`
  - score_data.txt — persistent high score file (single integer)
- README.md — this file

## How scoring and persistence work
- The scoreboard reads the high score from `score_data.txt` when it is instantiated:
  - `with open("score_data.txt","r") as file: self.high_score = int(file.read())`
- When a game ends, the scoreboard compares the current score to the saved high score and overwrites `score_data.txt` when the current score is higher.
- `score_data.txt` is a single line containing an integer (e.g., `5`).

Resetting the high score:
- Edit `snake_game/score_data.txt` with a text editor and set the value to `0` (or delete the file; on next run you'll need to recreate it or the code will crash because it expects the file to exist).
- Suggested improvement: handle the missing file gracefully (see next section).

Make high-score file path robust
If you want to run `python snake_game/main.py` from the repository root or run the module without changing the working directory, update `scoreboard.py` to locate `score_data.txt` relative to the file itself:

Example fix (replace the file open calls in scoreboard.py with the following):
```python
import os
# inside Scoreboard.__init__
data_path = os.path.join(os.path.dirname(__file__), "score_data.txt")
with open(data_path, "r") as file:
    self.high_score = int(file.read())
# later when writing:
with open(data_path, "w") as file:
    file.write(str(self.high_score))
```
This makes the path robust regardless of the process's current working directory.

## Code overview (where to look to modify behavior)
- main.py
  - Starts the turtle Screen, creates Snake, Food, Scoreboard instances, maps keys (Up/Down/Left/Right) to snake turns, and runs the game loop.
  - Game loop details: updates the screen, sleeps 0.1s per frame, checks for collision or food eaten, and handles resetting the game on collision.
- Snake.py
  - Class: Snake
    - create_snake: makes the initial three segments.
    - move: moves segments, checks edge and tail collisions (check_edges, check_tail). On collision, it moves segments off-screen and returns True to indicate game over.
    - add_segment: adds a new segment at the tail position.
    - snake_up/down/left/right: heading control that prevents direct reverse turns.
  - Tweak: change starting positions, speed (modify sleep in main or step length), or collision thresholds.
- food.py
  - Class: Food
    - create_food: picks a random position inside the screen bounds and places a small red circle.
    - snake_ate_food: returns True if the head is within 15 units of the food.
  - Tweak: change spawn range, appearance, or spawn logic.
- scoreboard.py
  - Class: Scoreboard (inherits from Turtle)
    - Tracks `score` and `high_score`, displays the values, writes high score to `score_data.txt`.
  - Tweak: change font, position, or persistence mechanism.

## Tips, troubleshooting & common issues
- No display / headless environment: turtle requires a GUI. On servers you need an X server or use a local machine.
- Missing tkinter: On Debian/Ubuntu, install with `sudo apt install python3-tk`.
- FileNotFoundError for `score_data.txt`: Make sure you run the game from the `snake_game` folder, or apply the path fix above.
- If the snake seems to jump or controls are ignored occasionally, ensure the turtle window has focus and capture of key events is active (click the window once to ensure focus).
- To change game speed: edit the sleep time in `main.py` (default `time.sleep(0.1)`) or change the `forward(20)` step in Snake.move.

## Development & Ideas for improvement
- Add a start screen and a proper game-over message instead of resetting abruptly.
- Make the high score file creation/reading robust (create file if missing; handle invalid contents).
- Add levels or increasing speed as score increases.
- Add obstacles or different food types.
- Use a package structure and allow running via `python -m snake_game.main` by adding `__init__.py` and fixing relative paths.
- Add tests for non-GUI logic (e.g., food spawn coordinates, snake movement logic without turtle graphics by separating logic from rendering).

## Contributing
Contributions are welcome. A short suggested workflow:
- Fork the repository
- Create a branch for your feature/fix
- Open a pull request describing the change and rationale

Before submitting changes that affect file paths or behavior, include notes in the README to help others run the code.

## License
No license file is included in this repository. If you plan to share or reuse this code publicly, consider adding an explicit license (for example, MIT, Apache-2.0) so others know how they are permitted to use it.

---

Enjoy the game!
