# Transform a method of a class into a property whose value is computed once
# and then cached as a normal attribute for the life of the instance. Similar
# to property(), with the addition of caching. Useful for expensive computed
# properties of instances that are otherwise effectively immutable.
from functools import cached_property
from node import Node

class BinomialTree:
    """ Binomial Tree Class
    """
    
    @staticmethod
    def merge(tree_1, tree_2):
        """ Merge two Binomial Trees of the same order.
        
        Given two order Bk Binomial Trees, merge them together to create
        a Binomial tree of the Order Bk + 1.

        Args:
            tree_1 (BinomialTree): First Binomial Tree 
            tree_2 (BinomialTree): The other Binomial Tree
        """
        if tree_1.order != tree_2.order:
            raise ValueError("Both Trees must have the same order.")
        
        # Increase order of tree by 1
        order = tree_1.order + 1
        rnode_1, rnode_2 = tree_1.root, tree_2.root
        if rnode_1.key <= rnode_2.key:
            # Merge tree 1 into tree 2 using root nodes
            rnode_2.parent = rnode_1
            if rnode_1.child is not None: # Fix sibling pointers
                rnode_2.sibling = rnode_1.child
            rnode_1.child = rnode_2
            rnode_1.degree += 1
            return BinomialTree(order, rnode_1)
        else:
            # Mergre tree 2 into tree 1 using root nodes
            rnode_1.parent = rnode_2
            if rnode_2.child is not None:
                rnode_1.sibling = rnode_2.child
            rnode_2.child = rnode_1
            rnode_2.degree += 1
            return BinomialTree(order, rnode_2)

    
    def __init__(self, order, root):
        self.order = order
        self.root = root

        
def create_b0_tree(key):
    """ Create an order 0 Binomial Tree

    Args:
        key (Any): The key of the root node for the Binomial Tree
    """
    root = Node(key, 0)
    return BinomialTree(0, root)

    
def create_bn_tree(n, *args):
    """_summary_

    Args:
        n (int): n is the degree of the Binomial Tree
        *args (int): the keys for each Binomial Tree
    """
    if n*2 > len(args):
        raise ValueError(f"Not enough keys for a N={n} Order Binomial Tree. Requires {n*2 - len(args)} extra keys.")
    if n*2 < len(args):
        raise ValueError(f"Too many keys for a N={n} Order Binomial Tree. Requires {len(args) - n*2} fewer keys.")
    pass

    keys = sorted(args)
    if n == 1:
        return create_b0_tree(keys[0])

    tree_stack = []
    # Loop through all the keys and create a Binomial Tree of order 0
    # Merge them if there are more than 2 Binomial Trees together
    for key in keys:         
        tree = create_b0_tree(key)
        tree_stack.append(tree)
        # Try to merge the two Binomial Trees
        while len(tree_stack) >= 2 and tree_stack[-1].order == tree_stack[-2].order:
            tree = BinomialTree.merge(tree_stack.pop(), tree_stack.pop())
            tree_stack.append(tree)

    bn_tree = tree_stack.pop()
    return bn_tree