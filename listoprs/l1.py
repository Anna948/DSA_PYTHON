print(" All list operations\n")
print(" Adding elements\n")
print("1)")
l=[1,2,3]
l.append(4)
print(l)
print("2)")
l.extend([5,6])
print(l)
print("3)")
l.insert(1,6)
print(l)

print("Removing elements")
l1=[7,8,9]
last=l1.pop()
print(last)

l1.remove(7)
print(l1)

print("Searching Operations")
l2=[4,5,6]
print(l2.index(4))
print(l2.count(4))
print(4 in l2)

print("Sorting & Reversing")
l3=[9,8,7]
l3.sort()
print(l3)
l3.reverse()
print(l3)