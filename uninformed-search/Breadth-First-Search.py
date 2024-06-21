# Breadth-First Search (BFS) algorithm implementation in Python

from collections import deque

def bfs(graph, start):
    """
    Performs a Breadth-First Search on the graph starting from the given node.

    Args:
        graph: A dictionary representing the graph, where each key is a node and
            the value is a list of neighboring nodes.
        start: The node to start the search from.

    Returns:
        A list of nodes in the order they were visited.
    """
    # Create a queue to hold the nodes to visit, and add the start node
    # This queue will be used to keep track of the nodes to visit next
    queue = deque([start])

    # Create a set to keep track of visited nodes
    # This set will be used to avoid visiting the same node multiple times
    visited = set()

    # Create a list to store the order of visited nodes
    # This list will be used to store the final order of visited nodes
    order = []

    # Loop until the queue is empty
    # This loop will continue until we have visited all reachable nodes
    while queue:
        # Dequeue the next node to visit
        # This node will be the next one to be processed
        node = queue.popleft()

        # If we haven't visited this node before, mark it as visited and add it to the order
        # This check is necessary to avoid visiting the same node multiple times
        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # Add the node to the order list
            order.append(node)

            # Add the node's neighbors to the queue
            # This will ensure that we visit all reachable nodes
            for neighbor in graph[node]:
                # Check if the neighbor has not been visited before
                if neighbor not in visited:
                    # Add the neighbor to the queue
                    queue.append(neighbor)

    # Return the final order of visited nodes
    return order

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
result = bfs(graph, start_node)

print("BFS order:", result)
