Explanation:

First, create a graph in a function.
Intialize a starting node and destination node.
Create a list for the visited nodes and stack for the next node to be visited.
Call the graph function.
 Initially, the stack is empty.Push the starting node into the stack (stack.append(start) ).
Mark the starting node as visited (visited.append(start) ).
Repeat this process until all the neighbours are visited in the stack till the destination node is found.
If the destination node is found exit the while loop.
If the destination node is not present then “Not found” is printed.
Finally, print the path from starting node to the destination node.
