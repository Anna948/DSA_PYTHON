def find_max(nums):
    n=nums[0]
    for i in nums:
        if i>n:
            n=i
    return n
m=[1,2,3,4]
res=find_max(m)
print("largest no:",res)