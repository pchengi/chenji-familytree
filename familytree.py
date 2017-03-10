# -*- coding: utf-8 -*-
"""
familytree 1
@author: Prashanth Dwarakanath
"""
import pydot,sys 
familydicts=[]
graph = pydot.Dot(graph_type='graph')
with open('chenji-tree') as inf:
	for line in inf:
		familydicts.append(eval(line))

for pdict in familydicts:
	#print type(pdict)
	for parent,children in pdict.iteritems():
		#print "parent is %s, children are %s"%(parent, children)
		for child in children:
			edge=pydot.Edge(parent,child)
			graph.add_edge(edge)
graph.write_pdf('chenji-family.pdf')

# and we are done!
