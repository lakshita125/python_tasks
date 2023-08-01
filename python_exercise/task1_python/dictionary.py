#dictionary creation :
# we create dictionary by placing key:value pairs inside curly brackets{} , separated by commas
personal_details ={
    
    "Name" : " Lakshita Sinha" ,
    "Age"  : "21",
    "City" : "bikaner",
    "college"   : "arya college"
     }

#printing the dictionary
print(personal_details)
print(len(personal_details)) #it will give the length of the dictionary

#get() - it will return the value of the specified key
Age = personal_details.get("Age")
print(Age)

#items() - this method will return all the entries of the dictionary in a list
items = personal_details.items()
print(items)

#keys() - this will return all the keys in the dictionary.it returns the keys in a tuple
keys = personal_details.keys()
print(keys)

#values() - this will return all the values in a  tuple
values = personal_details.values()
print(values)

#pop() - this will remove a key-value pair from the dictionary.
personal_details.pop("college")
print(personal_details)

#popitem()  - this method is similar to pop(). the difference is taht it removes the last item in the dictionary
personal_details.popitem()
print(personal_details)

