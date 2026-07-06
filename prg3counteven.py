def count_even(nums):
    count=0
    l=[]
    for i in nums:
        if i%2==0:
            l.append(i)
            count+=1
    return l,count        


n=[1,2,3,4]
res=count_even(n)
print(res)