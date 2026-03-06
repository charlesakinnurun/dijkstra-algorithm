import heapq  # Import heapq for the priority queue (min-heap) implementation
import time   # Import time to simulate "steps" for visualization

def dijkstra(graph, start_node):
    """
    Finds the shortest paths from start_node to all other nodes in a weighted graph.
    :param graph: Dictionary where keys are nodes and values are lists of (neighbor, weight)
    :param start_node: The node to start the search from
    """
    
    # --- INITIALIZATION ---
    
    # distances stores the current shortest distance from start_node to each node.
    # We initialize all distances to 'infinity' because we haven't found a path yet.
    distances = {node: float('infinity') for node in graph}
    
    # The distance from the start node to itself is always 0.
    distances[start_node] = 0
    
    # priority_queue will store tuples of (distance, node).
    # We use a min-heap so that we always process the node with the smallest distance first.
    priority_queue = [(0, start_node)]
    
    # predecessor tracks the path taken so we can reconstruct the shortest path later.
    predecessor = {node: None for node in graph}
    
    print(f"\n{'='*60}")
    print(f" STARTING DIJKSTRA'S ALGORITHM")
    print(f" Starting Node: {start_node}")
    print(f"{'='*60}\n")

    # --- MAIN LOOP ---
    
    while priority_queue:
        # Step 1: Pop the node with the smallest cumulative distance from the heap.
        current_distance, current_node = heapq.heappop(priority_queue)
        
        print(f"--> Visiting Node: [ {current_node} ] (Current distance from start: {current_distance})")

        # Step 2: Optimization - if we found a better path already, skip this stale entry.
        if current_distance > distances[current_node]:
            print(f"    (Skipping {current_node}: A shorter path was already found)")
            continue

        # Step 3: Explore neighbors of the current node.
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Step 4: Relaxation step.
            # If the new calculated distance is less than the known distance, update it.
            if distance < distances[neighbor]:
                old_dist = distances[neighbor]
                distances[neighbor] = distance
                predecessor[neighbor] = current_node
                
                # Push the updated distance and neighbor onto the priority queue.
                heapq.heappush(priority_queue, (distance, neighbor))
                
                print(f"    * Path to {neighbor} updated: {old_dist} -> {distance} via {current_node}")
        
        # Visualize the current state of distances
        visualize_state(distances)
        time.sleep(0.3) # Short pause for readability

    return distances, predecessor

def visualize_state(distances):
    """Helper function to print a simple bar chart of current distances."""
    print("    Current Distance Table:")
    for node, dist in distances.items():
        val = "inf" if dist == float('inf') else dist
        bar = "#" * int(dist) if dist != float('inf') else ""
        print(f"      {node}: {str(val).ljust(4)} {bar}")
    print("-" * 30)

def reconstruct_path(predecessor, start, end):
    """Traces back from the end node to the start node to find the specific path."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()
    return path if path[0] == start else []

# --- EXAMPLES & ILLUSTRATIONS ---

def run_demonstration():
    # Illustration of a Graph:
    # (A) --4-- (B)
    #  | \       |
    #  2  5     10
    #  |   \     |
    # (C) --3-- (D)
    
    example_graph = {
        'A': [('B', 4), ('C', 2), ('D', 5)],
        'B': [('A', 4), ('D', 10)],
        'C': [('A', 2), ('D', 3)],
        'D': [('A', 5), ('B', 10), ('C', 3)]
    }

    start = 'A'
    end = 'B'
    
    final_distances, parents = dijkstra(example_graph, start)
    
    shortest_path = reconstruct_path(parents, start, end)
    
    print("\n" + "#" * 40)
    print(" FINAL RESULTS")
    print("#" * 40)
    print(f"Shortest distance from {start} to {end}: {final_distances[end]}")
    print(f"Path taken: {' -> '.join(shortest_path)}")
    print("#" * 40)

if __name__ == "__main__":
    run_demonstration()