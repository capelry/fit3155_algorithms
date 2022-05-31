
class Node:
    """ Node Class specific for Binomial Heaps
    """
    def __init__(self, key, degree, child=None, sibling=None, parent=None):
        """ Construct a Node object
        
        The node object must have a key and degree during instantiation
        """
        self.key = key
        self.degree = degree
        self.child = child  # Child is a pointer to the left node
        self.sibling = sibling # Sibling is a pointer to the right node
        self.parent = parent

        
    def __repr__(self):
        return f"Node (key={self.key},degree={self.degree})"