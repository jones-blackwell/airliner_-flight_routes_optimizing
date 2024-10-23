# Airliner Flight Route Optimizer

This project helps an airliner optimize flight routes by calculating the minimum number of additional one-way routes needed to ensure every airport is reachable from a specified starting airport.

## Project Structure
You will find the following files in the project.

1. **`directed_graph.py`**:
   - Contains the `DirectedGraph` class that handles:
     - Adding directed edges to the graph.
     - Finding Strongly Connected Components (SCCs) using **Tarjan's Algorithm**.
     - Compressing the graph based on SCCs.
     - Calculating the additional routes needed to connect all SCCs.

2. **`route_optimizer.py`**:
   - Contains the `RouteOptimizer` class that:
     - Initializes flight routes externally.
     - Sets up the graph using the `DirectedGraph` class.
     - Validates and retrieves the starting airport, either from user input or as a command-line argument.

3. **`main.py`**:
   - The entry point for the program:
     - It initializes the `RouteOptimizer` with the provided routes.
     - Finds SCCs, compresses the graph, and calculates the number of additional routes.
     - Allows the user to provide the starting airport as a command-line argument or prompts for input.

4. **`README.md`**:
   - This file provides the project documentation.

## Algorithm Overview

This project uses **Tarjan's Algorithm** to find **Strongly Connected Components (SCCs)** in the graph of flight routes:
1. **SCC Identification**: Airports that can reach each other directly or indirectly form SCCs. Each SCC is treated as a node in a compressed graph.
2. **Route Calculation**: The program finds SCCs with no incoming edges (in-degree 0), excluding the SCC of the starting airport. The number of these SCCs represents the number of additional routes required to connect all airports.

### Tarjan’s Algorithm Steps:
1. Perform a **Depth-First Search (DFS)** to assign discovery and low-link values to each node (airport).
2. As nodes finish DFS, push them onto a stack.
3. Use the low-link values to identify **Strongly Connected Components (SCCs)**.
4. Compress the graph based on SCCs.
5. Calculate the number of SCCs with no incoming routes (in-degree 0), excluding the SCC of the starting airport.

## Running the Program

### Prerequisites
- Ensure you have Python 3 installed.

### How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/jones-blackwell/airliner_flight_routes_optimizing.git
    cd airliner_flight_routes_optimizing
    ```

2. **Run the program** with the start airport as a command-line argument:
    ```bash
    python main.py SFO
    ```

   Or, if no start airport is provided, the program will prompt for it:
    ```bash
    python main.py
    ```

3. **Output**: The program will print the minimum number of additional one-way routes needed to ensure all airports are reachable.

### Example Usage

```bash
$ python main.py JFK
 3
