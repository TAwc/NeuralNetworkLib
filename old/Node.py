#node for neural netowrk constrcutions
import numpy as np
import random

random.seed(1) #for ease

class node():
	def __init__(self, Ntype):
		self.type = Ntype							#creates a type 
		self.preSigmoid = 0							#the values before sigmoid calc
		self.PostSigmoid = 0						#the values after sigmoid calc
		self.RightLinks = []						#the nodes this node links to on the right
		self.weights = []							#the weights connected to this node leading to the right
		
	def linkingNodes(self,NodeArray):								#second part of double forloop
		
		for InNode in NodeArray:					
			self.RightLinks.append(InNode)							#adds node to link list
			self.weights.append(random.random())					#creates a random weight
		
		print("Node: ", self, self.type)							#node print out uncomment to use
		print("<-------------Right Nodes-------------->   <- Weights to nodes ->", )
		for i in range(len(NodeArray)):
			print(self.RightLinks[i]," | ", self.weights[i])
		print()

