class item:
    def __init__(self,id,date,price):
        self.id=id
        self.date=date
        self.price=price
        self.next=None
        self.prev=None
    def item_info(self):
        print(f"id:{self.id} date:{self.date} price:{self.price}")
new=item(9,'9th jan',21)
n1=item(10,'10th jan',22)
n2=item(11,'11th jan',23)
n3=item(13,'12th jan',24)
n4=item(14,'13th jan',25)



n1.next=n2
n2.prev=n1       
n2.next=n3
n3.prev=n2
n3.next=n4
n4.prev=n3
n4.next=new
new.prev=n4


cur=n1
while cur:
    cur.item_info()
    cur=cur.next
'''
n=int(input("Enter the no of ids u want whose price u want to add"))
sum=0
for i in range(n):
    print("Enter the id ")
    search_id=int(input("ID:"))
    cur=n1
    found= False
    while cur:
        if cur.id==search_id:
            sum+= cur.price
            found= True
            break
        cur=cur.next
print("The sum of price will be:",sum)
'''
prices = set()
cur = n1
while cur:
    prices.add(cur.price)
    cur = cur.next

sorted_prices = sorted(prices)
print("Unique prices:", sorted_prices)

if(len(sorted_prices)>=2):
    second_largest = sorted_prices[-2]
    print("Second largest price:", second_largest)
else:
    print("Not enough distinct prices to find a second largest")
    

'''
cur=n4
while cur:
    print(cur.data)
    cur=cur.prev
    '''