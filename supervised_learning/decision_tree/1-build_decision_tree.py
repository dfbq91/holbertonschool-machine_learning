#!/usr/bin/env python3
"""
Decision Tree Classifier
"""


import numpy as np


class Node:
    """Node class for decision tree"""
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Returns the maximum depth of the tree below this node"""
        left_child_depth = self.left_child.max_depth_below()
        right_child_depth = self.right_child.max_depth_below()
        return max(left_child_depth, right_child_depth)

    def count_nodes_below(self, only_leaves=False):
        """Returns the number of nodes below this node"""
        left_nodes_count = self.left_child.count_nodes_below(
            only_leaves=only_leaves
        )
        right_nodes_count = self.right_child.count_nodes_below(
            only_leaves=only_leaves
        )
        if only_leaves:
            return left_nodes_count + right_nodes_count
        return 1 + left_nodes_count + right_nodes_count


class Leaf(Node):
    """Leaf class for decision tree"""
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Returns the depth of the leaf node"""
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Returns the number of nodes below this leaf"""
        return 1


class Decision_Tree():
    """Decision Tree class"""
    def __init__(self, max_depth=10, min_pop=1,
                 seed=0, split_criterion="random", root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """Returns the depth of the tree"""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Returns the number of nodes in the tree"""
        return self.root.count_nodes_below(only_leaves=only_leaves)
