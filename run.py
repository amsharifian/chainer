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

def main(dotfile):
    ng = ch.CreateGraph(dotfile, [('style', '')]);

    # Check whether the graph has more than one BB node or not
    if ch.CheckStartNode(ng) == 1:
        sys.exit("The graph can not have more than one BB node")
    
    ch.ExpandGEP(ng)
    
    ch.RemoveDataNodes(ng)
    
    ch.Dilworth(ng)

    nx.drawing.nx_pydot.write_dot(ng,'sample.dot')

    ch.BreakHeadNode(ng)


nargs = len(sys.argv)
if (nargs != 3):
        print 'usage: python chains.py <dot file> <output file>'
        sys.exit()

dotfile = sys.argv[1] 
fig = sys.argv[2]
main(dotfile) 

