# ''' Q2.list1=[[2,4],[7,8],[9,10]]
#  list2=[[4,2],[8,9],[9,10]]
#  Find all the uncommon pairs'''
  

def find_the_uncommon_pairs(list1, list2):
    uncommon = [element for element in list1 if element not in list2] + [element for element in list2 if element not in list1]
    return uncommon


list1 = [[2, 4], [7, 8], [9, 10]]
list2 = [[4, 2], [8, 9], [9, 10]]

set_laksh = set()
uncommon = find_the_uncommon_pairs(list1, list2)
for element in uncommon:
    set_laksh.add(tuple(sorted(element)))
    
print("uncommon")  
for element in set_laksh:
    print(element)  
