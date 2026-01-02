# Graph Traversal Visualizer

*(Inspired by the exercise  
[Visualizador de Travessia de Grafos em Python](https://neps.academy/br/course/algoritmos-em-grafos/lesson/visualizador-de-travessia-de-grafos-em-python)  
from Neps Academy)*

This project was developed inspired by the **Visualizador de Travessia de Grafos em Python** exercise from **Neps Academy**, part of the Graph Algorithms course.  
It is an interactive desktop application written in **Python using Pygame** that allows users to visually construct a graph and observe how **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** traverse it step by step.
The project focuses on **educational visualization**, **graph construction**, and the use of **fundamental data structures**, following a **competitive programming style** with short variable names and direct logic.

---

## Features

- Interactive creation of nodes by clicking on the screen;
- Prevention of nodes being placed too close to each other;
- Creation of **undirected edges** between existing nodes;
- Multiple interaction modes (node, edge, start selection);
- Step-by-step visualization of:
  - **BFS (Breadth-First Search)**;
  - **DFS (Depth-First Search)**.
- Color-based visualization of node states:
  - Unvisited nodes;
  - Currently visited node;
  - Already visited nodes;
  - Selected / start node.
- Clear traversal visualization and run again on the same graph;
- Save the current graph structure to a `graph.json` file;
- Load a previously saved graph and continue interacting with it.
---

## Controls

| Key | Action |
|----|-------|
| `N` | Node creation mode |
| `E` | Edge creation mode |
| `S` | Select starting node |
| `B` | Run BFS traversal |
| `D` | Run DFS traversal |
| `C` | Clear traversal visualization |
| `K` | Save graph to `graph.json` |
| `L` | Load graph from `graph.json` |

---

## How to Run
To run the project locally:

```bash
git clone https://github.com/your-username/graph-traversal-visualizer.git
cd Graph-Traversal-Visualizer-in-Python
python -m venv venv
pip install -r requirements.txt
python main.py
```
## Project Structure
```
graph-traversal-visualizer/
│── main.py
│── graph.py
│── requirements.txt
│── README.md
```