l=['emoji','cheems',12,1000,2900]
print(l)
l.append(500)  #adds the given element in the end of list
print(l)

l.insert(2,'laksh')  #insert the value at specified position
print(l)

a=[47,'apple','mango',59]
b=[1,5,'banana']

#add b to a

a.extend(b) # add the  items of list 2 to list 1
print(a)

c=[8,9,6]
c.reverse() #reverse the elements of list
print(c)

m=[1,9,4,4,7,4,4]
print(m.count(4))  #calculates the occurrence of given element