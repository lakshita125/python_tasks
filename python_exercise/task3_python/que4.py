#  que4. search all elements from a list of lists
list1= [[67,6,9],[5,6,7],[8,2,9,7]]
count = 0
Search_for_element=int(input("enter the desired input: "))
for i in list1:
    for j in i:
        if Search_for_element==j:
            count+=1
      

if(count>0):
    print(Search_for_element , "is present")
    print("count :-", count)

else:
    print(Search_for_element ,"not present")