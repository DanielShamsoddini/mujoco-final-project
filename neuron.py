# import random
# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

# # class NEURALNETWORK:
# #     def __init__(self, size):
# #         self.levelsOfNeurons = 3
# #         self.weights= [[random.uniform(-0.005,0.005) for a in range(size)] for a in range(self.levelsOfNeurons)]

# #     def returnValue(self, data, level=0):
# #         #use numpy.clip ????
# #         motorvals = numpy.zeros(data.ctrl.shape)
# #         for a in range(data.ctrl.shape[0]):
# #             for b in range(5):
# #                 motorvals[a]+= float(data.sensor("test"+str(b+1)).data.copy())*self.weights[level][a+b]
# #         return motorvals


# class NEURALNETWORK:
#     def __init__(self):
#         import numpy as np
#         # Create a Directed Acyclic Graph (DAG)
#         self.G = nx.DiGraph()

#         # Define the input layer
#         self.input_layer = ['X1', 'X2', 'X3']
#         self.G.add_nodes_from(self.input_layer)

#         # Define the hidden layer
#         hidden_layer = ['H1', 'H2', 'H3']
#         self.G.add_nodes_from(hidden_layer)

#         # Connect the input layer to the hidden layer with weighted edges
#         weights = [[0.1, 0.2, 0.3],
#                 [0.4, 0.5, 0.6],
#                 [0.7, 0.8, 0.9]]

#         for i, input_node in enumerate(self.input_layer):
#             for j, hidden_node in enumerate(hidden_layer):
#                 weight = weights[i][j]
#                 self.G.add_edge(input_node, hidden_node, weight=weight)

#         # Define the output layer
#         output_layer = ['O1', 'O2', 'O3']
#         self.G.add_nodes_from(output_layer)

#         # Connect the hidden layer to the output layer with weighted edges
#         weights = [[0.1, 0.2, 0.3],
#                 [0.4, 0.5, 0.6],
#                 [0.7, 0.8, 0.9]]

#         for i, hidden_node in enumerate(hidden_layer):
#             for j, output_node in enumerate(output_layer):
#                 weight = weights[i][j]
#                 self.G.add_edge(hidden_node, output_node, weight=weight)

#         # Visualize the DAG
#         pos = nx.spring_layout(self.G)
#         nx.draw_networkx(self.G, pos=pos, with_labels=True)
#         edge_labels = {(u, v): d['weight'] for u, v, d in self.G.edges(data=True)}
#         nx.draw_networkx_edge_labels(self.G, pos=pos, edge_labels=edge_labels)
#         plt.show()

# # Calculate the output of the DAG given input values
#     def return_value(self, data):
#         input_values = [1, 2, 3]
#         outputs = {}
#         for node in nx.topological_sort(self.G):
#             predecessors = self.G.predecessors(node)
#             if len(predecessors) == 0:
#                 outputs[node] = input_values[self.input_layer.index(node)]
#             else:
#                 weighted_sum = sum(outputs[predecessor] * self.G[predecessor][node]['weight'] for predecessor in predecessors)
#                 outputs[node] = weighted_sum

#         # Print the output values
#         for output_node in output_layer:
#             print(f"{output_node}: {outputs[output_node]}")
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
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
        weights = 5*np.random.rand(input_size, hidden_size) -2.5
        for i, input_node in enumerate(input_layer):
            for j, hidden_node in enumerate(hidden_layer):
                weight = weights[i][j]
                G.add_edge(input_node, hidden_node, weight=weight)

        # Define the output layer
        output_layer = ['O{}'.format(i+1) for i in range(output_size)]
        G.add_nodes_from(output_layer)

        # Connect the hidden layer to the output layer with weighted edges
        weights = 5*np.random.rand(hidden_size, output_size) -2.5
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
        return np.clip(0,10, true_outputs)
