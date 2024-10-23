import sys
from route_optimizer import RouteOptimizer  # Import the RouteOptimizer class from route_optimizer.py


# Main function
if __name__ == "__main__":
    # Define provided Routes
    routes = [
        ('SFO', 'SAN'), ('SAN', 'EYW'), ('EYW', 'LHR'), ('LHR', 'SFO'),
        ('SFO', 'DSM'), ('DSM', 'ORD'), ('ORD', 'BGI'), ('BGI', 'LGA'),
        ('EWR', 'HND'), ('HND', 'ICN'), ('ICN', 'JFK'), ('HND', 'JFK'), ('JFK', 'LGA'),
        ('TLV', 'DEL'), ('DEL', 'CDG'), ('CDG', 'BUD'),
        ('CDG', 'SIN'), ('SIN', 'CDG'),
        ('DEL', 'DOH')
    ]

    # Instantiate the RouteOptimizer with defined routes
    optimizer = RouteOptimizer(routes)
    
    # [1] Set up the graph
    graph = optimizer.setup_graph()

    # [2] Find SCCs
    sccs = graph.find_sccs()

    # [3] Compress the graph based on SCCs
    compressed_graph, scc_map = graph.compress_graph(sccs)

    # [4] Get start airport from command-line argument or prompt the user
    start_airport = sys.argv[1] if len(sys.argv) > 1 else None
    start_airport = optimizer.get_valid_start_airport(graph, start_airport)

    # [5] Calculate the minimum additional routes (considering in-degree 0 SCCs)
    try:
        additional_routes = graph.calculate_additional_routes(compressed_graph, scc_map, start_airport)
        print(f"{additional_routes}")
    except KeyError:
        print(f"Error: The start airport '{start_airport}' does not exist in the graph.")
