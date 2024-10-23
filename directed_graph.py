from collections import defaultdict

class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.reversed_graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.reversed_graph[v].append(u)

    def dfs(self, node, visited, stack=None):
        visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(node)

    def reverse_dfs(self, node, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in self.reversed_graph[node]:
            if neighbor not in visited:
                self.reverse_dfs(neighbor, visited, component)

    def find_scc(self):
        stack = []
        visited = set()

        for node in list(self.graph):
            if node not in visited:
                self.dfs(node, visited, stack)

        visited.clear()
        scc = []
        while stack:
            node = stack.pop()
            if node not in visited:
                component = []
                self.reverse_dfs(node, visited, component)
                scc.append(component)

        return scc

    # Compressing the graph based on the Components
    def compress_graph(self, sccs):
        compressed_graph = defaultdict(set)
        scc_map = {}

        for i, component in enumerate(sccs):
            for node in component:
                scc_map[node] = i

        for u in self.graph:
            for v in self.graph[u]:
                if scc_map[u] != scc_map[v]:
                    compressed_graph[scc_map[u]].add(scc_map[v])

        return compressed_graph, scc_map

    def calculate_additional_routes(self, compressed_graph, scc_map, start):
        in_degree = defaultdict(int)

        for u in compressed_graph:
            for v in compressed_graph[u]:
                in_degree[v] += 1

        start_scc = scc_map[start]
        zero_in_degree_count = 0
        for scc in range(len(in_degree)):
            if in_degree[scc] == 0 and scc != start_scc:
                zero_in_degree_count += 1

        return zero_in_degree_count
