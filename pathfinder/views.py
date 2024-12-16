from rest_framework.decorators import api_view
from rest_framework.response import Response
import osmnx as ox
import networkx as nx
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(['POST'])
def find_multiple_paths(request):
    """
    Compute the shortest path between origin and destination using OSMnx.
    """
    try:
        data = request.data
        print(data)
        origin_coords = tuple(data['origin'])
        destination_coords = tuple(data['destination'])

        # Load the graph for Bengaluru (use OSMnx)
        graph = ox.graph_from_place("Bengaluru, India", network_type="drive")
        #print(graph)
        # Find the nearest nodes
        origin_node = ox.nearest_nodes(graph, origin_coords[1], origin_coords[0])
        print(origin_node)
        destination_node = ox.nearest_nodes(graph, destination_coords[1], destination_coords[0])
        print(destination_node)
        # Compute shortest paths
        shortest_path = nx.shortest_path(graph, origin_node, destination_node, weight='length')
        print(shortest_path)
        # Convert path to coordinates
        path_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in shortest_path]
        print(path_coords)
        return Response({"paths": [path_coords]})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
