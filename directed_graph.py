from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.index = 0
        self.stack = []
        self.indices = {}
        self.low_links = {}
        self.on_stack = set()
        self.sccs = []

    # Method to add a directed edge (one-way by default)
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # Method for finding Strongly Connected Components (SCCs) using Tarjan's algorithm
    def tarjan(self, node):
        # Set the index and low-link values for the node
        self.indices[node] = self.index
        self.low_links[node] = self.index
        self.index += 1
        self.stack.append(node)
        self.on_stack.add(node)

        # Visit all neighbors
        for neighbor in self.graph[node]:
            if neighbor not in self.indices:
                # If the neighbor hasn't been visited, do DFS on it
                self.tarjan(neighbor)
                self.low_links[node] = min(self.low_links[node], self.low_links[neighbor])
            elif neighbor in self.on_stack:
                # If the neighbor is on the stack, it's part of the current SCC
                self.low_links[node] = min(self.low_links[node], self.indices[neighbor])

        # If the current node is a root node, pop the stack and form an SCC
        if self.indices[node] == self.low_links[node]:
            scc = []
            while True:
                popped_node = self.stack.pop()
                self.on_stack.remove(popped_node)
                scc.append(popped_node)
                if popped_node == node:
                    break
            self.sccs.append(scc)

    # Method to find all SCCs in the graph using Tarjan's algorithm
    def find_sccs(self):
        for node in list(self.graph.keys()):  # Iterate over a static copy of graph keys
            if node not in self.indices:
                self.tarjan(node)
        return self.sccs

    # Method for Compressing the graph based on the SCCs
    def compress_graph(self, sccs):
        compressed_graph = defaultdict(set)
        scc_map = {}

        # Assign each node to its SCC
        for i, component in enumerate(sccs):
            for node in component:
                scc_map[node] = i

        # Create the compressed graph where each SCC is treated as a node
        for u in self.graph:
            for v in self.graph[u]:
                if scc_map[u] != scc_map[v]:
                    compressed_graph[scc_map[u]].add(scc_map[v])

        return compressed_graph, scc_map

    # Method for Calculating the number of additional routes required
    def calculate_additional_routes(self, compressed_graph, scc_map, start):
        in_degree = defaultdict(int)

        # Calculate in-degrees for the compressed graph
        for u in compressed_graph:
            for v in compressed_graph[u]:
                in_degree[v] += 1

        start_scc = scc_map[start]

        # Count SCCs with in-degree 0, excluding the start SCC
        zero_in_degree_count = 0
        for scc in compressed_graph:
            if in_degree[scc] == 0 and scc != start_scc:
                zero_in_degree_count += 1

        # Return the number of additional routes needed
        return zero_in_degree_count