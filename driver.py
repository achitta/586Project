from naive import NaiveAlgorithm
from algorithm import Algorithm
import networkx as nx
import numpy as np
import random
import time

def completeGraph(numNodes):
    vertices = [i for i in range(numNodes)]
    edges = []
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:
                edges.append((vertices[i],vertices[j]))
    return vertices, edges

def randomGraph(numNodes, probability):
    vertices = [i for i in range(numNodes)]
    edges = []
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j and random.random() <= probability:
                edges.append((vertices[i],vertices[j]))
    return vertices, edges

def erdos_renyi(numNodes, probability):
    vertices = [i for i in range(numNodes)]
    edges = []
    for i in range(len(vertices)):
        for j in range(i, len(vertices)):
            if i != j and random.random() <= probability:
                edges.append((vertices[i],vertices[j]))
    return vertices, edges

def watts_strogatz(numNodes, k_neighbors, probability):
    watts_strogatz = nx.watts_strogatz_graph(numNodes, k_neighbors, probability)
    return list(watts_strogatz.nodes()), list(watts_strogatz.edges())

def getDeleteOrder(edges, numDelete):
    if numDelete > len(edges):
        numDelete = len(edges)
    
    deleteIndices = np.random.choice([i for i in range(len(edges))], numDelete, False)
    deleteEdges = []
    for idx in deleteIndices:
        deleteEdges.append(edges[idx])
    return deleteEdges

def assertEqual(sccs_1, sccs_2):
    if len(sccs_1) != len(sccs_2):
        pass

    for scc_1 in sccs_1:
        found = False
        for scc_2 in sccs_2:
            if scc_1 == scc_2:
                found = True
                break
        if not found:
            pass

def runAlgorithm(v, e, toDelete, naive=False):
    alg = None
    if naive:
        alg = NaiveAlgorithm(v.copy(), e.copy())
    else:
        alg = Algorithm(v.copy(), e.copy())
    start_time = time.time()
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    end_time = time.time()
    return end_time - start_time, alg.getSccs()

def compare(v, e, numDelete=None):
    if not numDelete:
        numDelete = len(e)

    toDelete = getDeleteOrder(e, numDelete)
    naiveRuntime, sccs_1 = runAlgorithm(v, e, toDelete, naive=True)
    optimizedRuntime, sccs_2 = runAlgorithm(v, e, toDelete)
    assertEqual(sccs_1, sccs_2)
    print(f"Total Deletions: {numDelete}")
    print(f"Naive Runtime: {naiveRuntime}")
    print(f"Optimized Runtime: {optimizedRuntime}")
    print(f"Speedup: {naiveRuntime / optimizedRuntime}")
    print("-----------------------------------------")
    print()


def main():
    print("Complete Graphs")
    print("=======================================")
    for numNodes in range(20, 110, 20):
        print(f"Complete Graph w/ {numNodes} nodes")
        print("-----------------------------")
        v, e = completeGraph(numNodes)
        compare(v, e)

    print("Random Graph: Variable Num Nodes + Probability = 0.5")
    print("=======================================")
    for numNodes in range(20, 110, 20):
        print(f"Random Graph w/ {numNodes} nodes")
        print("-----------------------------")
        v, e = randomGraph(numNodes, 0.5)
        compare(v, e)

    print("Random Graph: Variable Probability + Num Nodes = 50")
    print("=======================================")
    for prob in range(0, 110, 20):
        prob = prob / 100
        print(f"Random Graph w/ {prob} probability")
        print("-----------------------------")
        v, e = randomGraph(50, prob)
        compare(v, e)
    
    print("Erdos-Renyi: Variable Num Nodes + Probability = 0.5")
    print("=======================================")
    for numNodes in range(20, 110, 20):
        print(f"Erdos-Renyi w/ {numNodes} nodes")
        print("-----------------------------")
        v, e = erdos_renyi(numNodes, 0.5)
        compare(v, e)

    print("Watts-Strogatz: Variable Num Nodes + Probability = 0.3 + K = 5")
    print("=======================================")
    for numNodes in range(20, 110, 20):
        print(f"Watts-Strogatz w/ {numNodes} nodes")
        print("-----------------------------")
        v, e = watts_strogatz(numNodes, 5, 0.3)
        compare(v, e)
    

    

if __name__ == "__main__":
    main()