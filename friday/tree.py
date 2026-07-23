class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=node(10)
n2=node(200)
n3=node(45)
n4=node(34)
n5=node(33)
n6=node(1)
n7=node(4)
n8=node(9)
root.left=n2
root.right=n3

n2.left = n4      # 200 -> 34
n2.right = n5      # 200 -> 33
n3.left = n6       # 45 -> 1
n3.right = n7      # 45 -> 4
n4.left = n8       # 34 -> 9
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
preorder(root)
