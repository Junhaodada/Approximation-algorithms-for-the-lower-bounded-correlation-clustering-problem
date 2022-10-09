# Approximation algorithms for the lower bounded correlation clustering problem

## introduce

Lower bounded correlation clustering problem (LBCorCP) is a new
generalization of the correlation clustering problem (CorCP). In the LBCorCP, 
we are given an integer L and a complete labelled graph. Each edge in the graph
is either positive or negative based on the similarity of its two endpoints. The
goal is to partition the vertices of the graph into some clusters, each cluster
contains at least L vertices, so as to minimize the sum of the number of
positive cut edges and negative uncut edges. In this paper, we first introduce
the LBCorCP and give three algorithms for this problem. The first algorithm
is a random algorithm, which is designed for the instances of the LBCorCP
with fewer positive edges. The second one is that we let the set V itself as a
cluster and prove that the algorithm works well on two specially instances with
fewer negative edges. The last one is an LP-rounding based iterative algorithm, 
which is provided for the instances with fewer negative edges. Although these
three algorithms are not applicable to all instances of the LBCorCP, they can
quickly solve some special instances in polynomial time and obtain a smaller
approximation ratio.

## environment

Implementation details. The code is actually implemented on VsCode1.71.2 using Python 3.8.
The whole experiment is implemented on a single processwith an Intel(R) Core(TM) i5-9300H CPU at 2.40GHz and 8 GB RAM.
