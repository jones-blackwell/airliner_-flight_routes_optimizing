from directed_graph import DirectedGraph  # Import the DirectedGraph class from directed_graph.py


class RouteOptimizer:
    def __init__(self, routes):
        # Public property for holding flight routes initialized externally
        self.routes = routes
    
    # Method to set up the graph based on the current routes
    def setup_graph(self):
        graph = DirectedGraph()

        # Add the one-way routes
        for u, v in self.routes:
            graph.add_edge(u, v)

        return graph

    # Method to validate and get the starting airport
    def get_valid_start_airport(self, graph, start_airport=None):
        # Get valid airports from the graph
        valid_airports = set(graph.graph.keys())

        if start_airport and start_airport.upper() in valid_airports:
            return start_airport.upper()

        while True:
            start_airport = input("Enter the starting airport (e.g., EWR, SFO, JFK): ").upper()

            # Check if the airport is valid
            if start_airport in valid_airports:
                return start_airport
            else:
                print(f"Error: '{start_airport}' is not a valid airport code. Please enter one of {valid_airports}.")
