from collections import namedtuple
from sys import stdout
 
Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))
 
def printwithspace(i):
    stdout.write("%i " % i)
 
def preorder(node, visitor = printwithspace):
    if node is not None:
        visitor(node.data)
        preorder(node.left, visitor)
        preorder(node.right, visitor)
 
stdout.write('  preorder: ')
preorder(tree)
stdout.write('\n')
