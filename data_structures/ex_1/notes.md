# Breadth First vs Depth First Searching

## Breadth-First Traversal

* The breadth-first approach when each generation of nodes have meaning

    - In breadth-first, you visit each level before moving on to the next, in a top to bottom order. Each node is visited, once, from left to right.

    **Top-to-bottom, left-to-right!**

    - Breadth-first search is less useful in binary search trees...because of the parent-child relationship that are characteristic of binary search trees. 

    ![breadth-first-image](https://cdn-images-1.medium.com/max/1600/1*fGEE6TYlsgDhZHSAQdjXeQ.png "BFS")

    As you can see in the above image, breadth-first-search happens by level. That is, each generation of nodes is traversed before moving to the next level. 

    In order to keep track of relationships between each node, we need to use a queue data structure that implements a FIFO rule. 

    Why do we need the queue?? 

    ![Why?](https://cdn-images-1.medium.com/max/1600/1*cHJXXL2h4Efg7i6IsaGfDA.png "Why????")

    The Queue structure will allow us to keep track of relationships

-------

## Depth-First Traversal

* Depth first traversal requires a callback function that will keep recursing until each respective branch has no nodes left

-----
## Heapsort

* comparision-based sorting algorithm.
    - divides input into sorted and unsorted and it iteratively shrinks the unsorted region by extracting the largest element and moving it to its proper place in the sorted region. 

* Step 1:
    - heap is built out of data
    - layout is very similar to a binary search tree
    - each array index represents a node
* Step 2:
    - sorted array is created by repeatedly removing the largest element from the heap (the root of the heap) and inserting it into the array.
    - The heap is updated after each removal. 
    - after all nodes have been **removed**, the result is a sorted array. 
    - can be performed in place. Only cost is that of extraction.