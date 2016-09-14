import pygraphviz as pgv
import networkx as nx
from networkx.drawing.nx_pydot import write_dot
from collections import defaultdict
from collections import OrderedDict
import collections


def checkEdgeOut(ng,limit):
    # TODO add COPY node
    for n in nx.nodes(ng):
        if len(ng.successors(n)) > limit:
            print 'error out' + n


def checkEdgeIn(ng,limit):
    # TODO add COPY node
    for n in nx.nodes(ng):
        if len(ng.in_edges(n)) > limit:
            print 'error in ' + n


def build_chain_dic_helper(ng):
    # Building chain dicitonary
    chdic = defaultdict(list)
    for n in nx.nodes(ng):
        chdic[ng.node[n]['cid']].append(n)
        if ng.node[n]['opcode'] == 'BB':
            headnode = n
            headcid  = ng.node[n]['cid']
    return chdic


def build_chain_edge_helper(ng):
    # Building chain's edges
    ch_edge = defaultdict(list)
    for n in nx.nodes(ng):
        for t in ng.successors(n):
            if ng.node[n]['cid'] != ng.node[t]['cid']:
                ch_edge[ng.node[n]['cid']].append(ng.node[t]['cid'])
    return ch_edge


def build_chain_edge_reverse_helper(ng):
    # Building chain's edges
    ch_edge = defaultdict(list)
    for n in nx.nodes(ng):
        for (s,t) in ng.in_edges(n):
            if ng.node[n]['cid'] != ng.node[s]['cid']:
                ch_edge[ng.node[n]['cid']].append(ng.node[s]['cid'])
    return ch_edge


def SetColor(ng, n, rank):
	r = rank % 6 
	if (r == 0):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'red'
	if (r == 1):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'blue'
	if (r == 2):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'green'
	if (r == 3):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'yellow'
	if (r == 4):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'orange'
	if (r == 5):
		ng.node[n]['style'] = 'filled'
		ng.node[n]['fillcolor'] = 'violet'


def limitChainOut(ng, limit):
    has_liveout = True
    while has_liveout:
        has_liveout = False
        ch_dic = build_chain_dic_helper(ng)
        ch_edge = build_chain_edge_helper(ng)

        new_cid = len(ch_dic)
        for key, value in ch_edge.items():
            if len(value) > limit:
                has_liveout = True
                temp_ch = ch_dic[key]
                temp_ch.sort()

                # iterate from top node and if it has an edge outside of the chain
                # break the chain from that point
                update = True
                for c in temp_ch:
                    if update:
                        for t in ng.successors(c):
                            if ng.node[c]['cid'] != ng.node[t]['cid']:
                                update = False
                    else:
                        ng.node[c]['cid'] = new_cid
                        SetColor(ng, c, new_cid)


                new_cid += 1



def limitChainIn(ng, limit):
    has_livein = True
    while has_livein:
        has_livein = False
        ch_dic = build_chain_dic_helper(ng)
        ch_edge = build_chain_edge_reverse_helper(ng)

        new_cid = len(ch_dic)
        for key, value in ch_edge.items():
            if len(value) > limit:
                has_livein = True
                temp_ch = ch_dic[key]
                int_temp_ch = [int(x) for x in temp_ch]
                int_temp_ch.sort()
                temp_ch = [str(x) for x in int_temp_ch]

                # iterate from top node and if it has an edge outside of the chain
                # break the chain from that point
                update = True
                for c in temp_ch:
                    if update:
                        for (s,t) in ng.in_edges(c):
                            if ng.node[c]['cid'] != ng.node[s]['cid']:
                                update = False
                    else:
                        ng.node[c]['cid'] = new_cid
                        SetColor(ng, c, new_cid)


                new_cid += 1
