# Create a set of cities and find the common vowels present in their names
def find_common_vowels(cities):
    vowels = set('aeiou')
    common_vowels = set()
    for city in cities:
        common_vowels.update(filter(lambda x: x in vowels, city.lower()))
    return common_vowels

#  set of cities
cities = {'Jaipur', 'Bikaner', 'Jodhpur', 'Ajmer', 'Udaipur'}

# Finding the common vowels in the city names
common_vowels = find_common_vowels(cities)

print("Common vowels in the city names:", common_vowels)