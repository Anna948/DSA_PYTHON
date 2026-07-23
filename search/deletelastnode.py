class delete:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

n1=delete(10)
n2=delete(20)
n3=delete(30)

n1.next=n2
n2.prev=n1
n2.next=n3
n3.prev=n2

cur=n1
while cur:
    print(cur.data)
    cur=cur.next
