<h1 align="center">Dijkstra’s Algorithm</h1>

## Overview

**Dijkstra’s Algorithm** is a graph algorithm used to find the **shortest path from a starting node to all other nodes** in a **weighted graph**.

It works only when **edge weights are non-negative**.

The algorithm was developed by **Edsger W. Dijkstra** in 1956 and is one of the most important algorithms in computer science.

Dijkstra’s Algorithm is commonly used in:

* GPS navigation systems
* Network routing protocols
* Map applications (Google Maps, etc.)
* Logistics and transportation planning
* Telecommunications networks

---

## ⚙️ How Dijkstra’s Algorithm Works

The algorithm repeatedly selects the node with the **smallest known distance** from the start node and updates distances to its neighbors.

### Steps

1. Assign distance **0** to the starting node and **∞ (infinity)** to all other nodes
2. Mark all nodes as **unvisited**
3. Select the **unvisited node with the smallest distance**
4. Update the distances of its neighboring nodes
5. Mark the current node as **visited**
6. Repeat until all nodes are visited or the destination is reached

---

## 🧩 Example Graph

```
        (4)
   A -------- B
   |          |
 (1)|          |(2)
   |          |
   C -------- D
        (1)
```

### Edge Weights

| Edge  | Weight |
| ----- | ------ |
| A → B | 4      |
| A → C | 1      |
| C → D | 1      |
| D → B | 2      |

---

## 🧪 Step-by-Step Example

Find the shortest path from **A**.

| Node | Distance from A |
| ---- | --------------- |
| A    | 0               |
| B    | 3               |
| C    | 1               |
| D    | 2               |

### Shortest Paths

```
A → C = 1
A → C → D = 2
A → C → D → B = 3
```

---

## ⏱️ Time & Space Complexity

| Implementation                  | Time Complexity  |
| ------------------------------- | ---------------- |
| Using Array                     | O(V²)            |
| Using Min Heap / Priority Queue | O((V + E) log V) |

Where:

* **V** = number of vertices
* **E** = number of edges

**Space Complexity:** O(V)

---

## 🧠 Python Implementation

```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances


graph = {
    'A': {'B': 4, 'C': 1},
    'B': {},
    'C': {'D': 1},
    'D': {'B': 2}
}

print(dijkstra(graph, 'A'))
```

### Output

```
{'A': 0, 'B': 3, 'C': 1, 'D': 2}
```

---

## 👍 Advantages

* Efficient for shortest path problems
* Works well with weighted graphs
* Widely used in real-world applications
* Can be optimized with priority queues

---

## 👎 Disadvantages

* Does **not work with negative edge weights**
* Can be slower on very large graphs without optimization
* Requires additional memory for storing distances

---

## 📌 When to Use Dijkstra’s Algorithm

Use Dijkstra’s Algorithm when:

* You need the **shortest path in a weighted graph**
* Edge weights are **non-negative**
* You want distances from **one source node to all nodes**

---

## 📊 Comparison with BFS

| Feature        | BFS            | Dijkstra       |
| -------------- | -------------- | -------------- |
| Graph type     | Unweighted     | Weighted       |
| Shortest path  | Yes            | Yes            |
| Edge weights   | Not considered | Considered     |
| Data structure | Queue          | Priority Queue |

---

## 🏁 Summary

Dijkstra’s Algorithm is a powerful algorithm for finding the shortest paths in weighted graphs with non-negative edge weights. It is fundamental in computer science and is used in many real-world systems such as navigation, networking, and logistics optimization.
