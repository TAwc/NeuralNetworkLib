import node
import math

class sequential_nn():
    def __init__(self):
        self.layers_num = 0
        self.layers = []

    def addLayer(self, num_nodes):

        self.layers.append([node.node() for i in range(num_nodes)])

        self.layers_num  += 1
        
        if self.layers_num != 1:
            for pre_node in self.layers[self.layers_num-2]:
                for next_node in self.layers[self.layers_num-1]:
                    pre_node.connect_node(next_node)

            
    def test(self, input):

        for node in self.layers[0]:
            node.post_sig = input[0]

        for layer_level in range(1,len(self.layers)):                       #skip first layer
            for node in self.layers[layer_level-1]:
                values = []
                for weight_index in range(len(node.weights)):
                post_sig of prev layer += value of x node
                    



        



            

    def sigmoid(self,x):																												
        return (1/(1+pow(math.e,-(x))))     


if __name__ == "__main__":
    nn = sequential_nn()
    nn.addLayer(5)
    print("layer 1 done")
    nn.addLayer(3)