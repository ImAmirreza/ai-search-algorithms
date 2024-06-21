# Depth-First Search (DFS) algorithm implementation in Python

def dfs(graph, start):
    """
    Performs a Depth-First Search on the graph starting from the given node.

    Args:
        graph: A dictionary representing the graph, where each key is a node and
            the value is a list of neighboring nodes.
        start: The node to start the search from.

    Returns:
        A list of nodes in the order they were visited.
    """
    # Create a set to keep track of visited nodes
    # This set will be used to avoid visiting the same node multiple times
    visited = set()

    # Create a list to store the order of visited nodes
    # This list will be used to store the final order of visited nodes
    order = []

    # Define a recursive helper function to perform the DFS
    def dfs_helper(node):
        # Mark the node as visited
        # This is necessary to avoid visiting the same node multiple times
        visited.add(node)

        # Add the node to the order list
        # This will store the final order of visited nodes
        order.append(node)

        # Iterate over the node's neighbors
        # This will explore the graph depth-first
        for neighbor in graph[node]:
            # Check if the neighbor has not been visited before
            if neighbor not in visited:
                # Recursively call the dfs_helper function on the neighbor
                # This will explore the graph depth-first
                dfs_helper(neighbor)

    # Call the dfs_helper function on the start node
    # This will start the DFS from the given node
    dfs_helper(start)

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
result = dfs(graph, start_node)

print("DFS order:", result)
