#num=[1,5,7,10,5,8,9,10]
#odd_index=[]
#even_index=[]
#for i in num:
#    if i%2==0:
#        even_index.append(i)
#    else:
#        odd_index.append(i)
#print(odd_index)
#print(even_index)

'''
def checknum(num):
    even_list=[ i for i in num if i%2==0]
    odd_list=[i for i in num if i%2==1]
    return even_list,odd_list
num=[1,2,3]
res_even,res_odd=checknum(num)
print("evens:",res_even,"odds:",res_odd)

'''
num=[1,2,3]
even_list=num[::2]
odd_list=num[1::2]
print("odd_list:",odd_list,"even_list:",even_list)