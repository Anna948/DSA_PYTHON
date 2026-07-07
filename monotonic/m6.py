def checkmono(l):
    return all([ l[i]<=l[i+1] for i in range(len(l)-1)]),all ([l[i]>=l[i+1] for i in range(len(l)-1)])
l=[1,2,3]
res=checkmono(l)
print(res)