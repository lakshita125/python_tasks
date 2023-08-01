# Create a set {1,2,3}, make it immutable
laksh={1,2,3}
'''Set elements are immutable but the set itself is a mutable object,
 so in order to make an immutable set, we use the concept of frozenset.
 The frozen set returns an immutable version of a Python set object.
 We can modify the elements of a set at any time by adding or deleting elements,
 but frozen sets do not allow any modification after its creation. '''

set1 = {1, 2, 3,}

new_set = frozenset(set1)

print("Immutable set using frozenset: ", new_set)