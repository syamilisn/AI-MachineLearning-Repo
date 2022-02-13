# Program to Implement recursive AO* Algorithm
def recAOStar(n):
    global finalPath
    print("Expanding Node : ", n)
    and_nodes = []
    or_nodes = []
    #Segregation of AND and OR nodes
    if (n in allNodes):
        if 'AND' in allNodes[n]:
            and_nodes = allNodes[n]['AND']
        if 'OR' in allNodes[n]:
            or_nodes = allNodes[n]['OR']
    # If leaf node then return
    if len(and_nodes) == 0 and len(or_nodes) == 0:
        return
    solvable = False
    marked = {}
    while not solvable:
    # If all the child nodes are visited and expanded, take the least cost of all the child nodes
        if len(marked) == len(and_nodes) + len(or_nodes):
            min_cost_least, min_cost_group_least = least_cost_group(and_nodes, or_nodes, {})
            solvable = True
            change_heuristic(n, min_cost_least)
            optimal_child_group[n] = min_cost_group_least
            continue
    # Least cost of the unmarked child nodes
    min_cost, min_cost_group = least_cost_group(and_nodes, or_nodes, marked)
    is_expanded = False
    # If the child nodes have sub trees then recursively visit them to recalculate the heuristic of the child node
    if len(min_cost_group) > 1:
        if (min_cost_group[0] in allNodes):
            is_expanded = True
            recAOStar(min_cost_group[0])
        if (min_cost_group[1] in allNodes):
            is_expanded = True
            recAOStar(min_cost_group[1])
        else:
            if (min_cost_group in allNodes):
                is_expanded = True
                recAOStar(min_cost_group)
# If the child node had any subtree and expanded, verify if the new heuristic value is still the least among all nodes
        if is_expanded:
            min_cost_verify, min_cost_group_verify = least_cost_group(and_nodes,or_nodes, {})
    if min_cost_group == min_cost_group_verify:
        solvable = True
        change_heuristic(n, min_cost_verify)
        optimal_child_group[n] = min_cost_group
# If the child node does not have any subtrees then no change in heuristic, so update the min cost of the current node
    else:
        solvable = True
        change_heuristic(n, min_cost)
        optimal_child_group[n] = min_cost_group
#Mark the child node which was expanded
    marked[min_cost_group] = 1
    return heuristic(n)
# Function to calculate the min cost among all the child nodes
def least_cost_group(and_nodes, or_nodes, marked):
    node_wise_cost = {}
    for node_pair in and_nodes:
        if not node_pair[0] + node_pair[1] in marked:
            cost = 0
            cost = cost + heuristic(node_pair[0]) + heuristic(node_pair[1]) + 2
            node_wise_cost[node_pair[0] + node_pair[1]] = cost
    for node in or_nodes:
        if not node in marked:
            cost = 0
            cost = cost + heuristic(node) + 1
            node_wise_cost[node] = cost
    min_cost = 999999
    min_cost_group = None
# Calculates the min heuristic
    for costKey in node_wise_cost:
        if node_wise_cost[costKey] < min_cost:
            min_cost = node_wise_cost[costKey]
            min_cost_group = costKey
    return [min_cost, min_cost_group]
# Returns heuristic of a node
def heuristic(n):
    return H_dist[n]
# Updates the heuristic of a node
def change_heuristic(n, cost):
    H_dist[n] = cost
    return
# Function to print the optimal cost nodes
def print_path(node):
    print(optimal_child_group[node], end="")
    node = optimal_child_group[node]
    if len(node) > 1:
        if node[0] in optimal_child_group:
            print("->", end="")
            print_path(node[0])
        if node[1] in optimal_child_group:
            print("->", end="")
            print_path(node[1])
        else:
            if node in optimal_child_group:
                print("->", end="")
                print_path(node)
#Describe the heuristic here
H_dist = { 'A': -1,'B': 4, 'C': 2, 'D': 3, 'E': 6,'F': 8, 'G': 2,'H': 0, 'I': 0, 'J': 0}
#Describe your graph here
allNodes = {
'A': {'AND': [('C', 'D')], 'OR': ['B']},
'B': {'OR': ['E', 'F']},
'C': {'OR': ['G'], 'AND': [('H', 'I')]},
'D': {'OR': ['J']}
}
optimal_child_group = {}
optimal_cost = recAOStar('A')
print('Nodes which gives optimal cost are')
print_path('A')
print('\nOptimal Cost is :: ', optimal_cost)
