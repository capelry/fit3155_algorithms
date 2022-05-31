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
        pass

    
    def __init__(self, order, root):
        self.order = order
        self.root = root

        
def create_b0_tree(key):
    """ Create an order 0 Binomial Tree

    Args:
        key (Any): The key of the root node for the Binomial Tree
    """
    return Node(key, 0)

    
def create_bn_tree(n, *args):
    """_summary_

    Args:
        n (int): n is the degree of the Binomial Tree
        *args (int): the keys for each Binomial Tree
    """
    if n*2 > len(args):
        raise ValueError(f"Not enough keys for a N Order Binomial Tree. Requires {n*2 - len(args)} extra keys.")
    if n*2 < len(args):
        raise ValueError(f"Too many keys for a N Order Binomial Tree. Requires {len(args) - n*2} fewer keys.")
    pass


