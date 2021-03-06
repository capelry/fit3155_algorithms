from binomialtree import *
from datastructure_utils import BNode
import unittest


class TestBinomialTree(unittest.TestCase):
    
    def test_create_b0_tree(self):
        root = BNode(4, 0)
        bt = BinomialTree(0, root)
        test_bt = create_b0_tree(4)
        self.assertEqual(bt.root.key, test_bt.root.key)
        self.assertEqual(bt.order, test_bt.order)

        
if __name__ == "__main__":
    unittest.main()