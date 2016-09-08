import pdb
import sys
import os
import pygraphviz as pgv
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import json
from collections import OrderedDict
import numpy as np
from graph.dilworth import chains as ch
from graph.limitio import limitio as lim
from graph.limitio import limitcheck as check

def main(dotfile):
    # Reading dot file
    ng = ch.CreateGraph(dotfile, [('style', '')]);

    # Check whether the graph has more than one BB node or not
    if ch.CheckStartNode(ng) == 1:
        sys.exit("The graph can not have more than one BB node")

    # Expanding GEP instructions
    ch.ExpandGEP(ng)

    # Removing data nodes
    ch.RemoveDataNodes(ng)

    # Running Dilworth algorithm
    ch.Dilworth(ng)

    # Breaking head node
    ch.BreakHeadNode(ng)

    check.checkEdgeOut(ng,2)

    check.limitChainOut(ng,2)

    check.limitChainIn(ng,2)
    # cg = nx.DiGraph()
    # lim.AddChainNodes(cg, ng)

    # d = lim.CreateChainDict(cg, ng)

    # lim.CheckInEdges(ng)

    # lim.LimitChains(ng, cg, d)

    # lim.ColorGraph(ng, cg, d)

    # g = lim.OutputGraph(ng, cg, d)

    # Writing output graph
    nx.drawing.nx_pydot.write_dot(ng, 'sample.dot')



nargs = len(sys.argv)
if (nargs != 3):
        print 'usage: python chains.py <dot file> <output file>'
        sys.exit()

dotfile = sys.argv[1] 
fig = sys.argv[2]
main(dotfile) 

