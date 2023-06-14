import numpy as np
import networkx as nx

class NEURALNETWORK:
    def __init__(self,input_size, hidden_size, output_size):
        # Create a Directed Acyclic Graph (DAG)
        G = nx.DiGraph()

        # Define the input layer
        input_layer = ['X{}'.format(i+1) for i in range(input_size)]
        G.add_nodes_from(input_layer)

        # Define the hidden layer
        hidden_layer = ['H{}'.format(i+1) for i in range(hidden_size)]
        G.add_nodes_from(hidden_layer)

        # Connect the input layer to the hidden layer with weighted edges
        weights = 20*np.random.rand(input_size, hidden_size) -10
        for i, input_node in enumerate(input_layer):
            for j, hidden_node in enumerate(hidden_layer):
                weight = weights[i][j]
                G.add_edge(input_node, hidden_node, weight=weight)

        # Define the output layer
        output_layer = ['O{}'.format(i+1) for i in range(output_size)]
        G.add_nodes_from(output_layer)

        # Connect the hidden layer to the output layer with weighted edges
        weights = 20*np.random.rand(hidden_size, output_size) -10
        for i, hidden_node in enumerate(hidden_layer):
            for j, output_node in enumerate(output_layer):
                weight = weights[i][j]
                G.add_edge(hidden_node, output_node, weight=weight)

        self.graph = G
        self.final_layer = output_size

    def simulate_neural_network(self, input_values):
        # Calculate the output of the DAG given input values
        input_values = np.clip(0,1, input_values)
        outputs = {}
        input_layer = [node for node in self.graph.nodes if node.startswith('X')]
        output_layer = [node for node in self.graph.nodes if node.startswith('O')]
        for node in nx.topological_sort(self.graph):
            predecessors = list(self.graph.predecessors(node))

            if len(predecessors) == 0:
                outputs[str(node)] = input_values[input_layer.index(node)]
            else:
                weighted_sum = sum(outputs[predecessor] * self.graph[predecessor][node]['weight'] for predecessor in predecessors)
                outputs[str(node)] = weighted_sum


        true_outputs = np.zeros(self.final_layer)
        for a,b in enumerate(list(outputs.keys())[-self.final_layer:]):
            true_outputs[a] = outputs[b]
        return true_outputs/(np.max(np.abs(true_outputs)))
