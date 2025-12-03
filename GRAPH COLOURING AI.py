def is_safe(graph, node, color, colors):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True

def color_map(graph, colors, node, available_colors):
    if node == len(graph):
        return True
    for color in available_colors:
        if is_safe(graph, node, color, colors):
            colors[node] = color
            if color_map(graph, colors, node + 1, available_colors):
                return True
            colors[node] = None
    return False

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1],
    3: [1]
}

available_colors = ["Red", "Green", "Blue"]
colors = {node: None for node in graph}

if color_map(graph, colors, 0, available_colors):
    print(colors)
else:
    print("No coloring possible")
