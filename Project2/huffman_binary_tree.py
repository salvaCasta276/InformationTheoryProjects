import numpy as np
import heapq as hq

class HuffmanBinaryTree:

    def __init__(self, word_prob_dict):
        self.word_proc_dict = word_prob_dict
        self.leaves = {key: HuffmanBinaryNode(value, key) for key, value in word_prob_dict.items()}

        self.root = build_tree_from_leaves()
        generate_codes()

    class HuffmanBinaryNode:

        def __init__(self, probability, word=None):
            self.probability = probability
            self.word = word
            self.right = None
            self.left = None
            self.code = None

        def __lt__(self, other):
            return self.probability < other.get_probability()

        def is_leaf(self):
            return right is None and left is None

        def get_probability(self):
            return self.probability

        def set_right(self, right):
            self.right = right

        def set_left(self, left):
            self.left = left

        def get_right(self):
            return right

        def get_left(self):
            return left

        def set_code(self, code)
            self.code = code

        def get_code(self)
            return self.code

    def build_tree_from_leaves(self):
        node_heap = list(leaves.values())
        hq.heapify(node_heap)

        min_node = hq.heappop(node_heap)
        while len(node_heap) > 0:
            next_min_node = hq.heappop(node_heap)
            new_node = HuffmanBinaryNode(min_node.get_probability() + next_min_node.get_probability())

            new_node.set_right(min_node)
            new_node.set_left(next_min_node)

            hq.heappush(node_heap, new_node)

        return min_node

    #The algorithm for generating codes over the tree will be implemented recursively
    #This is because the number of words encoded is small
    def generate_code(self, root, code):

        if root.is_leaf():
            root.set_code(code)
            return

        #Both children should exist as there can be no unused leaves
        generate_code(root.get_right(), code + "0")
        generate_code(root.get_left(), code + "1")

    def get_codes(self):
        return {key: value.get_code() for key, value in self.leaves}

    
