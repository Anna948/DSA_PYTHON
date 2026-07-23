class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

n1=Node(34)
n2=Node(4)
n3=Node(67)
n4=Node(10)

n4.next=n3
n3.prev=n4
n3.next=n2
n2.prev=n3
n2.next=n1
n1.prev=n2

cur=n4
result=[]
while cur:
    print(cur.data)
    result.append(str(cur.data))
    
    cur=cur.next
print(" -> ".join(result))
'''
cur=n4
while cur:
    print(cur.data)
    cur=cur.prev
    '''
result.sort(key=int, reverse=True)
print(result)