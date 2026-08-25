arr=[1,1,2,2,1,4,6,1,2,3,4]
res=[]
for x in arr:
    if x not in res:
        res.append(x)
print(res)
