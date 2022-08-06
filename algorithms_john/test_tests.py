from binomialtree import *

def test_create_bn_tree():
    n = 2
    bn_tree = create_bn_tree(n, 2, 4, 6, 7)
    print(bn_tree)

    
test_create_bn_tree()