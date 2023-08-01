A= {1,5,7,9}                #set first
B= {0,9,6}                  #set second
  
  #union
print(A.union(B))          # performing A union B using union()
print(A|B)                 #performing A unoin B using |

#intersection
print(A.intersection(B))  #using intersection()
print(A&B)                # using  &

#difference  - the difference between two sets A and B include 
# elements of set A that are not present on set B
print(A-B)                #using -
print(A.difference(B))    #using difference()

#set symmetric difference - the ssymmetric difference between two sets
# A and B includes all elements of A and B without common elements
print(A^B)               #using ^
print(A.symmetric_difference(B))     #using symmetric_difference()

# add items to  a set
num1 ={12,56,78,45}
print('initial set:',num1)
num1.add(76)
print('updated set:',num1)
 