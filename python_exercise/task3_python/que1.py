# Q1.WAP to count all unique values in the list

#METHOD_1
list=[3,5,7,8,9,3,5]
set=set(list)
count= len(set)    
print(count)

 #METHOD_2
list2=[1,3,5,6,1,6]
unique_list = []
unique_items = 0

for item in list2:
     if item not in unique_list:
         unique_list.append(item)
         unique_items += 1

print(unique_items)

#METHOD_3
dict = {'ramdom' : [9,7,4,8,9,4,1]}

unq_items = list({ele for val in dict.values() for ele in val})
count = len(unq_items)
print(count)