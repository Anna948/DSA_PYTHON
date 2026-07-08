class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
new=Node(100)
n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
new.next=n1
n1.prev=new
n1.next=n2
n2.prev=n1       
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
cur=new
while cur:
    print(cur.data)
    cur=cur.next

'''
cur=n4
while cur:
    print(cur.data)
    cur=cur.prev
    '''