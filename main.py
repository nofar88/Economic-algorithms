from typing import List
import networkx as nx


def find_cycle_in_consumption_graph(allocation: List[List[float]]):
    edges_list = [(f'player{i}', f'object{j}') for i in range(len(allocation)) for j in range(len(allocation[0])) if
                  allocation[i][j] > 0]#Checks if an edge exists by definition and builds the graph
    graph = nx.Graph()
    graph.add_edges_from(edges_list)
    try:
        return nx.find_cycle(graph) #Checks if a circuit exists and returns it if there is
    except:
        return None


if __name__ == '__main__':
    # example of a graph with a circle
    matrix = [[1, 1, 0, 0],
              [1, 1, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0]]
    cycle = find_cycle_in_consumption_graph(matrix)
    assert cycle is not None

    # example of a graph without a circle
    matrix = [[1, 1, 0, 0],
              [1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0]]
    cycle = find_cycle_in_consumption_graph(matrix)
    assert cycle is None
