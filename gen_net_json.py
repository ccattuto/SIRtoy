#!/usr/bin/env python
import sys, json
import networkx as nx
from networkx.readwrite import json_graph

g = nx.barabasi_albert_graph(150, 2)
#g = nx.grid_3d_graph(10,10)

nodes = g.nodes()
nodes.sort()

data = json_graph.node_link_data(g)

data['nodes'] = [ {"name": i} for i in range(len(data['nodes'])) ]

f = open(sys.argv[1], 'w')

f.write( json.dumps(data) )

f.close()


