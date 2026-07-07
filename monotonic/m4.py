#m1=[1,3,5,6,6,7]
#m2=[m1[i]<=m1[i+1] for i in range (0,5)]
#print(m2)

m1=[2,3,3,4]
m3=[9,4,5,1]
m2=all([m1[i]<=m1[i+1] for i in range(len(m1)-1)])
m4=all([m3[i]>=m3[i+1] for i in range(len(m3)-1)])
print(m2)
print(m4)