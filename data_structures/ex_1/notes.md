# Depth First Search

* determines whether two nodes, x and y, have a bath between them
    - it does this by looking at the children of the starting node....x....and recursively determining if a path exists

    Here's an example:

Example: 
![example](https://algocoding.files.wordpress.com/2014/08/graph2.png?w=598&h=414 "DFS")
The adjacency list representation looks as follows:

```
0: [1, 2, 3]
1: [5, 6]
2: [4]
3: [2, 4]
4: [1]
5: []
6: [4]
```
If we run DFS by hand the vertices are visited in the following order: 0, 1, 5, 6, 4, 2, 3.
```