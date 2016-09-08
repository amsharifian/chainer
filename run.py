import pdb
import sys
import networkx as nx
import json
from graph.dilworth import chains as ch
from graph.limitio import limitcheck as check


def main(dotfile):

    # Reading
    # Reading dot file
    ng = ch.CreateGraph(dotfile, [('style', '')])

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

    check.checkEdgeOut(ng, 2)

    check.limitChainOut(ng, 2)

    check.limitChainIn(ng, 2)

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
if __name__ == "__main__":
    main(dotfile)
