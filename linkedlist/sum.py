class Item:
    def __init__(self, id, date, price):
        self.id = id
        self.date = date
        self.price = price
        self.next = None
        self.prev = None

    def item_info(self):
        print(f"id:{self.id} date:{self.date} price:{self.price}")


n5 = Item(9, '9th jan', 21)
n1 = Item(10, '10th jan', 22)
n2 = Item(11, '11th jan', 23)
n3 = Item(13, '12th jan', 24)
n4 = Item(14, '13th jan', 25)

n1.next = n2
n2.prev = n1
n2.next = n3
n3.prev = n2
n3.next = n4
n4.prev = n3
n4.next = n5
n5.prev = n4

cur = n1
while cur:
    cur.item_info()
    cur = cur.next

n = int(input("Enter the no of ids whose price you want to add: "))
total = 0

for i in range(n):
    search_id = int(input("ID: "))
    cur = n1
    found = False
    while cur:
        if cur.id == search_id:
            total += cur.price
            found = True
            break
        cur = cur.next
    if not found:
        print(f"ID {search_id} not found")

print(f"\nThe sum of price is: {total}")