class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
'''
print(n1.data)
print(n2.data)
print(n3.data)
print(n1.next.data)            
'''
cur=n1
while cur:
    print(cur.data)
    cur=cur.next