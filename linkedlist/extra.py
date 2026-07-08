prices = []
cur = n1
while cur:
    prices.append(cur.price)
    cur = cur.next

prices.sort()
print("All prices:", prices)

if len(prices) >= 2:
    second_largest = prices[-2]
    print("Second largest price:", second_largest)
else:
    print("Not enough items to find a second largest price")



prices = set()
cur = n1
while cur:
    prices.add(cur.price)
    cur = cur.next

sorted_prices = sorted(prices)
print("Unique prices:", sorted_prices)

if len(sorted_prices) >= 2:
    second_largest = sorted_prices[-2]
    print("Second largest price:", second_largest)
else:
    print("Not enough distinct prices to find a second largest")