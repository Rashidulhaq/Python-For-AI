Explanation
Lines 2-9: The illustrated graph is represented using an adjacency list - an easy way to do it in Python is to use a dictionary data structure. Each vertex has a list of its adjacent nodes stored.
Line 11: visited is a set that is used to keep track of visited nodes.
Line 21: The dfs function is called and is passed the visited set, the graph in the form of a dictionary, and A, which is the starting node.
Lines 13-18: dfs follows the algorithm described above:
It first checks if the current node is unvisited - if yes, it is appended in the visited set.
Then for each neighbor of the current node, the dfs function is invoked again.
The base case is invoked when all the nodes are visited. The function then returns.
Time Complexity
Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E)
O(V+E)
, where V
V
 is the number of vertices and E
E
 is the number of edges. In case of DFS on a tree, the time complexity is O(V)
O(V)
, where V
V
 is the number of nodes.

Note: We say average time complexity because a set’s in operation has an average time complexity of O(1)
O(1)
. If we used a list, the complexity would be higher.
