import osmnx as ox
import networkx as nx

def compute_multiple_paths(lat1, lon1, lat2, lon2, num_paths=3):
    # Load the pre-processed simple graph
    graph = ox.load_graphml("bengaluru_simple_graph.graphml")
    
    # Convert coordinates to the nearest node in the projected graph
    orig_node = ox.distance.nearest_nodes(graph, lon1, lat1)
    dest_node = ox.distance.nearest_nodes(graph, lon2, lat2)
    
    # Compute k-shortest paths (3 paths by default)
    k_paths = list(nx.shortest_simple_paths(graph, orig_node, dest_node, weight='length'))[:num_paths]
    
    # Prepare paths with coordinates and their lengths
    paths = []
    for path in k_paths:
        path_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in path]
        path_length = sum(ox.utils_graph.get_route_edge_attributes(graph, path, 'length'))
        paths.append({'path': path_coords, 'length': path_length})
    
    return paths

