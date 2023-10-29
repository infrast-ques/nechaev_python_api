# алгоритм дейкстры

my_graph = {"start": {"a": 6, "b": 2}}
my_graph["a"] = {}
my_graph["a"]["fin"] = 1
my_graph["b"] = {}
my_graph["b"]["a"] = 3
my_graph["b"]["fin"] = 5
my_graph["fin"] = {}
print(my_graph)

infinity = float("inf")
my_costs = {}
my_costs["a"] = 6
my_costs["b"] = 2
my_costs["fin"] = infinity
print(my_costs)

my_parent = {}
my_parent["a"] = "start"
my_parent["b"] = "start"
my_parent["in"] = None

processed = []

# node = find_lowest_cost_node(my_costs)
# while node is not None:
#     my_cost = my_costs[node]
#     neighbors = my_graph[node]
#     for n in neighbors.keys():
#         new_cost = my_cost + neighbors[n]
#         if my_costs[n] > new_cost:
#             my_costs[n] = new_cost
#             my_parent[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(my_costs)
