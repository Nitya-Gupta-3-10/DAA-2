arr="aabcdd"
res=[]
for x in arr:
    if x not in res:
        res.append(x)
print(res)
