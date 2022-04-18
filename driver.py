from turtle import distance
from es_tree import EsTree
from kosaraju import KosarajuGraph
from scc import SCC
from naive import NaiveAlgorithm
from algorithm import Algorithm
import networkx as nx
import numpy as np
import random
import time
#        0
#      /  \
#     1    2
#    / \     \
#   3   4  -  5

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

    # visited = set()
    # for _ in range(numDelete):
    #     r = len(edges)
    #     toDelete = random.randint(0, r-1)
    #     if toDelete in visited:
    #         continue
    #     visited.add(toDelete)
    #     deleteEdges.append(edges[toDelete])
    return deleteEdges

def assertEqual(alg1, alg2):
    sccs_1, _ = alg1.getSccs()
    sccs_2, _ = alg2.getSccs()
    if len(sccs_1) != len(sccs_2):
        assert False

    for scc_1 in sccs_1:
        found = False
        for scc_2 in sccs_2:
            if scc_1 == scc_2:
                found = True
                break
        if not found:
            print("ERROR!")
            # assert False

def main():
    print("Complete Graph w/ 100 nodes + 10 deletions")
    print("--------------------------------------------")
    v, e = completeGraph(100)
    toDelete = getDeleteOrder(e, 10)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        naive.deleteEdge(src, dst)
    naive.getSccs()
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    alg.getSccs()
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    print("Complete Graph w/ 100 nodes + 200 deletions")
    print("--------------------------------------------")
    v, e = completeGraph(100)
    toDelete = getDeleteOrder(e, 200)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        naive.deleteEdge(src, dst)
    naive.getSccs()
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    alg.getSccs()
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    print("Erdos-Renyi w/ 100 nodes + 200 deletions")
    print("--------------------------------------------")
    v, e = erdos_renyi(100, 0.3)
    toDelete = getDeleteOrder(e, 200)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        naive.deleteEdge(src, dst)
    naive.getSccs()
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    alg.getSccs()
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    print("Erdos Renyi w/ 100 nodes + 1000 deletions")
    print("--------------------------------------------")
    v, e = erdos_renyi(100, 0.3)
    toDelete = getDeleteOrder(e, 1000)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        naive.deleteEdge(src, dst)
    naive.getSccs()
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    alg.getSccs()
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    print("Watts-Strogatz w/ 200 nodes + 1000 deletions")
    print("--------------------------------------------")
    v, e = watts_strogatz(200, 50, 0.5)
    toDelete = getDeleteOrder(e, 1000)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        naive.deleteEdge(src, dst)
    naive.getSccs()
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        alg.deleteEdge(src, dst)
    alg.getSccs()
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    print("Complete Graph w/ 20 nodes + 1000 deletions")
    print("--------------------------------------------")
    v, e = completeGraph(50)
    toDelete = getDeleteOrder(e.copy(), len(e))
    # toDelete = [(2, 0), (0, 2), (1, 0), (0, 1), (2, 1), (1, 2)]
    # print(toDelete)
    start_time = time.time()
    naive = NaiveAlgorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        # print(f"Deleting {src} to {dst}")
        naive.deleteEdge(src, dst)
        # print("OUTPUT", naive.getSccs()[0])
    end_time = time.time()
    print(f"Naive Algorithm runtime: {end_time - start_time}")

    start_time = time.time()
    alg = Algorithm(v.copy(), e.copy())
    for src, dst in toDelete:
        # print(f"Deleting edge from {src} to {dst}")
        alg.deleteEdge(src, dst)
        # print("OUTPUT", alg.getSccs()[0])
    end_time = time.time()
    print(f"Algorithm runtime: {end_time - start_time}")
    assertEqual(naive, alg)
    print()
    print("=============================================")

    

    

if __name__ == "__main__":
    main()