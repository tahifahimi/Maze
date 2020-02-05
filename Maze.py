import collections
import sys

"Tahere Fahimi 9539045"
"Maze Project"
"Amirkabir University of technology"

# reading the test file
sys.stdin = open("test.txt", "r")
# reading the number of nodes and edges from file, n is number of nodes and m is number of edges
numberOfNodes, numberOfEdge = map(int, input().split())
# print(n , m)

# create class of nodes and edges
node = collections.namedtuple('node', 'id color adj_edges')
edge = collections.namedtuple('edge', 'id color')

# Create input graph
graph = []
# reading information of nodes from file --> id - color - adj
# adj is an empty array that keeps neighbors
for k in range(numberOfNodes):
    i,c = input().split()
    # print(node(id=i, color=c, adj_edges=[]))
    graph.append(node(id=i, color=c, adj_edges=[]))
# graph.append(node(id=n - 1, color="No Color", adj_edges=[]))

print("****")
# assign the place of ROCKET and LUCKY
ROCKET, LUCKY = map(int, input().split())
# print("the place of rocket and lucky are : ")
# print(ROCKET)
# print(LUCKY)

# reading the edges
for i in range(numberOfEdge):
    # print(i)
    line = input().split()
    # print(line[0])
    graph[int(line[0]) - 1].adj_edges.append(edge(id=int(line[1]), color=line[2]))


# Create pair graph, pair of nodes in the input graph
path = []
# create sub tree for every node of the graph
pair_graph = {(ROCKET, LUCKY): []}
# this queue save the unvisited ways like BFS
queue = [(ROCKET, LUCKY)]
# search for the path until find it or all the path are visited
while len(queue) != 0 and len(path) == 0:
    for i in range(len(queue)):
        key = queue.pop(0)
        print(graph[key[0]-1].id, "color is  : ",graph[key[0]-1].color)
        # print("the neighbours and colors are :")
        for e in graph[key[0]-1].adj_edges:
            # print(e.id, e.color)
            if e.color == graph[key[1]-1].color:
                # print("the matched for 2 is : ",e.id)
                # the final Goal is founded
                if e.id == numberOfNodes  and len(path) == 0:
                    path.append((e.id, key[1]))
                # add new place of the Lucky and Rocket to the queue
                if (e.id, key[1]) not in pair_graph:
                    print("new place L",(e.id, key[1]))
                    queue.append((e.id, key[1]))
                    print(queue)
                # add the subtree to its root
                if key in pair_graph:
                    pair_graph[key].append((e.id, key[1]))
                else:
                    pair_graph[key] = [(e.id, key[1])]

        # print(queue)

        print(graph[key[1]-1].id,"color is ",graph[key[1]-1].color)
        for e in graph[key[1]-1].adj_edges:
            if e.color == graph[key[0]-1].color:
                # the goal is founded
                if e.id == numberOfNodes and len(path) == 0:
                    path.append((key[0], e.id))
                # add new place of the Rocket in the queue
                if (key[0], e.id) not in pair_graph:
                    print("new place R",(key[0], e.id))
                    queue.append((key[0], e.id))
                    print(queue)
                if key in pair_graph:
                    pair_graph[key].append((key[0], e.id))
                else:
                    pair_graph[key] = [(key[0], e.id)]
        # print(queue)
# See if end is reached
if len(path) == 0:
    print("End Can't be reached")
else:
    # Making Path
    t = path[0]
    while t[0] != ROCKET or t[1] != LUCKY:
        for k, v in pair_graph.items():
            if t in v:
                path.insert(0, k)
                t = k
                break
    # Printing travels (Rocket, Lucky)
    for i in range(len(path) - 1):
        if path[i][0] == path[i + 1][0]:
            print("L ",path[i+1][1])
        elif path[i][1] == path[i + 1][1]:
            print("R ",path[i+1][0])