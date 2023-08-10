'''You are developing a program that analyzes weather data. Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
Input
temperature_readings = [25, 28, 21, 24, 27]
Output:
Average Temperature: 25.0
Highest Temperature: 28
Lowest Temperature: 21
'''
def analyze_weather_data(data):
    avg_temp= sum(data)/ len(data)
    highest_temp= max(data)
    lowest_temp= min(data)
    return avg_temp,highest_temp,lowest_temp

data=[25,28,21,24,27]
result= analyze_weather_data(data)
print("the avg,highest and lowest temp is:", result)