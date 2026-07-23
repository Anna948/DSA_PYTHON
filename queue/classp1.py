from collections import deque

class Order:
    def __init__(self,order_id,date,price,quantity):
        self.order_id=order_id
        self.date=date
        self.price=price
        self.quantity=quantity
        self.next=None

o1=Order(1,'1st jan',11,1)
o2=Order(2,'2nd Jan',12,2)
o3=Order(3,'3rd Jan',13,3)
o4=Order(4,'4th Jan',14,4)
o5=Order(5,'5th Jan',15,5)

q=deque()

q.append(o1)
q.append(o2)
q.append(o3)
q.append(o4)
q.append(o5)


while q:
    o = q.popleft()
    ''''
    print(o.order_id, o.date, o.price, o.quantity)
    print("Remaining in queue:")
    for order in q:
        print(" ", order.order_id, order.date, order.price, order.quantity)
    print()
    '''
    print(o.order_id, o.date, o.price, o.quantity)



