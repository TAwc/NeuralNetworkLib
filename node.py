import random

class node:
    def __init__(self):
        self.pre_sig = None
        self.post_sig = None
        self.weights = []

    def connect_node(self, node):
        self.weights.append(random.random())
        print (self.weights)
