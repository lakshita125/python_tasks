#  QUE 3: list1=[[6,1,4],[9,8,14],[8,9,7]]
#         Result=[[6,4,1],[14,9,8],[9,8,7]]   Reverse sorting

list1=[[6,1,4],[9,8,14],[8,9,7]]
result=[]
for x in list1:
    n=len(x)
    for i in range(n):
        for j in range(n):
            if(x[i] > x[j]):
                (x[i], x[j]) = (x[j], x[i])

    result.append(x)

print("reverse list :", result)