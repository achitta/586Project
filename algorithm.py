"""
Algorithm Steps:
1. Compute the SCCs 
2. For each SCC select one of the nodes to serve as the root
3. For each root, construct an ES-Tree with the graph's edges normal + ES-Tree with the graph's edges reversed
4. If an edge deletion causes a breakdown in the SCC, then we need to recompute 
"""

