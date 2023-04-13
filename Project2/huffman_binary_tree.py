import numpy as np
import heapq as hq

class HuffmanBinaryTree:

    def __init__(self, word_prob_dict):
        self.word_proc_dict = word_prob_dict
        self.leaves = {key: self.HuffmanBinaryNode(value, key) for key, value in word_prob_dict.items()}

        self.root = self.build_tree_from_leaves()
        self.generate_codes(self.root, "")

    class HuffmanBinaryNode:

        def __init__(self, probability, word=None):
            self.probability = probability
            self.word = word
            self.right = None
            self.left = None
            self.code = None

        #We order the nodes of the tree based on their probability
        def __lt__(self, other):
            return self.probability < other.get_probability()

        def is_leaf(self):
            return self.right is None and self.left is None

        def get_probability(self):
            return self.probability

        def set_right(self, right):
            self.right = right

        def set_left(self, left):
            self.left = left

        def get_right(self):
            return self.right

        def get_left(self):
            return self.left

        def set_code(self, code):
            self.code = code

        def get_code(self):
            return self.code

    def build_tree_from_leaves(self):
        node_heap = list(self.leaves.values())
        hq.heapify(node_heap)

        min_node = hq.heappop(node_heap)
        while len(node_heap) > 0:
            next_min_node = hq.heappop(node_heap)
            new_node = self.HuffmanBinaryNode(min_node.get_probability() + next_min_node.get_probability())

            new_node.set_right(min_node)
            new_node.set_left(next_min_node)

            hq.heappush(node_heap, new_node)
            min_node = hq.heappop(node_heap)

        return min_node

    #The algorithm for generating codes over the tree will be implemented recursively
    #This is because the number of words encoded is small
    def generate_codes(self, root, code):

        if root.is_leaf():
            root.set_code(code)
            return

        #Both children should exist as there can be no unused leaves
        self.generate_codes(root.get_right(), code + "0")
        self.generate_codes(root.get_left(), code + "1")

    def get_codes(self):
        return {key: value.get_code() for key, value in self.leaves.items()}

    
