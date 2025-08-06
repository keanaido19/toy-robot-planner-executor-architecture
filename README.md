# toy-robot-planner-executor-architecture

A simple Python simulation project demonstrating the **Planner-Executor Architecture** without involving AI components. This project is designed as a learning tool to understand how planning and execution modules can interact to control an autonomous agent—in this case, a robot moving on a 2D grid.

The robot can:
- Understand its orientation (North, East, South, West)
- Accept user-defined 2D coordinates
- Use actions (`MOVE_FORWARD`, `TURN_LEFT`, `TURN_RIGHT`) to reach the target position

The **Planner** generates a plan (a series of actions), and the **Executor** carries it out. These two components interface continuously, allowing the planner to update in real-time based on the outcome of execution.

---

## 🛠 Installation

**Requirements:**
- Python 3.7 or higher (Tested on Python 3.12)

```bash
# Clone the repository
git clone https://github.com/keanaido19/toy-robot-planner-executor-architecture.git
cd toy-robot-planner-executor-architecture

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Run the program
python main.py
