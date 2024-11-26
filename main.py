import tensorflow as tf
import numpy as np
import random
from collections import deque
import osmnx as ox
import networkx as nx
import folium
from matplotlib import cm
import matplotlib.colors as mcolors
import logic

locations = [
    (-7.257472, 112.752088),  # Depot
    (-7.265279, 112.737845), (-7.289617, 112.734900)
]
depot_location = locations[0]

# Fetch road network with extended distance
G = ox.graph_from_point(depot_location, dist=25000, network_type='drive')

# Function to validate nearest nodes and map locations to the road network
def map_to_nearest_nodes(locations, graph, distance_threshold=5000):
    valid_nodes = []
    valid_demands = []
    for idx, (lat, lng) in enumerate(locations):
        nearest_node = ox.nearest_nodes(graph, lng, lat)
        nearest_point = (graph.nodes[nearest_node]['y'], graph.nodes[nearest_node]['x'])
        dist_to_nearest = ox.distance.great_circle(lat, lng, nearest_point[0], nearest_point[1])
        print(f"Location {idx}: Distance to nearest node = {dist_to_nearest:.2f} meters")
        if dist_to_nearest > distance_threshold:  # Skip locations too far from the network
            print(f"Warning: Location {idx} is far from the road network! Skipping this location.")
            continue
        valid_nodes.append(nearest_node)
        if idx > 0:  # Exclude depot from demands
            valid_demands.append(10)
    return valid_nodes, valid_demands

# Map locations to nearest nodes
valid_nodes, valid_demands = map_to_nearest_nodes(locations, G)

# Convert graph to undirected for connectivity check
G_undirected = G.to_undirected()

# Check connectivity of the graph
if not nx.is_connected(G_undirected):
    print("Warning: The road network graph is not fully connected. Consider increasing the distance or changing locations.")
else:
    print("The road network graph is fully connected.")

# Build distance matrix for valid nodes
def build_distance_matrix(valid_nodes, graph):
    distance_matrix = np.zeros((len(valid_nodes), len(valid_nodes)))
    paths = {}
    for i, start_node in enumerate(valid_nodes):
        for j, end_node in enumerate(valid_nodes):
            if i != j:
                try:
                    path = nx.shortest_path(graph, start_node, end_node, weight='length')
                    distance = nx.shortest_path_length(graph, start_node, end_node, weight='length')
                    distance_matrix[i][j] = distance
                    paths[(i, j)] = path
                except nx.NetworkXNoPath:
                    print(f"Warning: No path between nodes {start_node} and {end_node}")
                    distance_matrix[i][j] = float('inf')
                    paths[(i, j)] = []
    return distance_matrix, paths

# Build distance matrix and paths
distance_matrix, paths = build_distance_matrix(valid_nodes, G)

# Print summary
print(f"Valid nodes: {valid_nodes}")
print(f"Distance matrix:\n{distance_matrix}")


