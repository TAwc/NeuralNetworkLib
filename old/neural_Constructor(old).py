#neural network Constructor 
import numpy as np
import Node
import math
import time

class Network():
	def __init__(self,inputVals,goal):

		self.cost = np.zeros([len(goal)])

		for iteration in range(len(goal)):
			self.test(iteration)																										#test to see if results go prpoerly
			self.forward()																												#does the math

																
			print("output")
			for i in range(len(self.OutputLayer)):																						#prints output layer results
				print(self.OutputLayer[i].PostSigmoid)

			# self.noteTaking(iteration,goal)																								#used in back probagation


			print("end of iteration: ",iteration)																						#legablity
			print()																														#legiblity


		for i in range(8000):
			self.backPropagation(goal,iteration)







	def linkNodes(self, LeftNodes, RightNodes):																							#this is kind of the first half a double forloop nest thing to link nodes
		for nodeA in LeftNodes:
			nodeA.linkingNodes(RightNodes)																								#second half located here


	def test(self, iteration):
				self.SurfaceLayer = [Node.node("surface") for _ in range(len(inputVals[iteration]))]									#creates node objects for surface level based off the input vals length
				self.HL1 = [Node.node("hidden") for _ in range(3)]																		#creates node objects for hidden level
				self.OutputLayer = [Node.node("output") for _ in range(len(goal[iteration]))] 											#creates node objects for output level output input


				self.Layers = [self.SurfaceLayer,self.HL1,self.OutputLayer]																#allows for the layers to be iterable

				for i in range(len(inputVals[iteration])):																				#assign the values of the input to the nodes
					self.SurfaceLayer[i].PostSigmoid = inputVals[iteration][i]

				
				for i in range(len(self.Layers)-1):																						#linkes all nodes correctly
					self.linkNodes(self.Layers[i],self.Layers[i+1])												


	def forward(self):
		for i in range(len(self.Layers)-1):																								#goes through the layers of the neural network
			for j in range(len(self.Layers[i])):																						#through the nodes of the layers
				for k in range(len(self.Layers[i][j].RightLinks)):																		#goes through the linked nodes of that node
					self.Layers[i][j].RightLinks[k].preSigmoid = self.Layers[i][j].PostSigmoid * self.Layers[i][j].weights[k]			#finds the pre sigmoid values for the nodes
					self.Layers[i][j].RightLinks[k].PostSigmoid = self.sigmoid(self.Layers[i][j].RightLinks[k].preSigmoid)				#finds the post sigmoid values for the nodes


	def sigmoid(self,x):																												#sigmoid activation function
		return (1/(1+pow(math.e,-(x))))


	def noteTaking(self,iteration,goal):
		for i in range(len(self.OutputLayer)):
			self.cost[iteration] = pow(self.OutputLayer[i].PostSigmoid-goal[iteration],2)												#takes note of the cost of the neural netowrk

		print("cost: " , self.cost)



#############################################################################################################################################
	
	def backPropagation(self,goal,iteration):
		print("<---------------start of back probagation----------------->")

		totalcost = 0

		for i in range(len(self.cost)):
			totalcost += self.cost[i]																									#find the total cost

		totalcost = totalcost/len(self.cost)																							#take the avg cost


		totalweight = []
		value = 0

		for k in range(len(self.Layers)):
			for i in range(len(self.Layers[k])):
				for j in range(len(self.Layers[k][i].RightLinks)):
					print("K: ",k,"I: ",i,"J: ",j)
					
					value += self.Layers[k][i].weights[j]
			totalweight.append(value)
			value = 0 

		for i in range(5):
			print("kill me")

		ChangeRate = []
		value = 0
		for i in range(len(self.HL1)):
			for j in range(len(self.HL1[i].RightLinks)):
				value += self.HL1[i].weights[j]/totalweight[j]
			ChangeRate.append(value)

		print("total: ", totalweight)
		print("ChangeRate: ", ChangeRate)

		print("<----------------end of back probagation------------------>")
		print()
		





inputVals =np.array([[1, 0], [0, 0],[1, 1], [0, 1]])
goal = ([[0],[1],[1],[0]])

model = Network(inputVals,goal)																											#creates a CNN
print ("time taken: ", time.time())
model.test([0,0])
															