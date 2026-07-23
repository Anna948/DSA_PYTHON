'''
num=[1,2,3,4,5]
for i in range(0,6):
    print(i)
    
a=len(num)//2
print(num[a])
'''

def bsearch(num,target):
    low=0
    high=len(num)-1
    
    while low<=high:
        mid=(low+high)//2
        if target==num[mid]:
            return num[mid]
        elif target<num[mid]:
            high=mid-1
        else:
            low=mid+1
        
num=[1,2,3,4,5]
res=bsearch(num,4)
print(res)
