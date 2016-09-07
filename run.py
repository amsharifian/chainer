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
import re
#from scipy import stats as sp


from graph.dilworth import chains as ch

def main(dotfile):
        ng = ch.CreateGraph(dotfile, [('style', '')]);
        # PrintGraph(ng)

        ch.ExpandGEP(ng)
        # PrintGraph(ng)
       

        ch.RemoveDataNodes(ng)
        # PrintGraph(ng)

        


        ch.Dilworth(ng)
        # PrintGraph(ng)
        nx.drawing.nx_pydot.write_dot(ng,'sample.dot')


nargs = len(sys.argv)
if (nargs != 3):
        print 'usage: python chains.py <dot file> <output file>'
        sys.exit()

dotfile = sys.argv[1] 
fig = sys.argv[2]
main(dotfile) 

