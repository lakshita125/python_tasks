'''Create a Time class and initialize it with hours and minutes.
Create a method addTime which should take two Time objects and add them.
E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime which should print the time.
Also create a method displayMinute which should display the total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minutes.'''
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        total_minutes = self.hours * 60 + self.minutes + other_time.hours * 60 + other_time.minutes
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)

    def displayTime(self):
        print(f"{self.hours} hr {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(total_minutes, "minutes")



time1 = Time(2, 50)
time2 = Time(1, 20)


result_time = time1.addTime(time2)
print("Resultant Time:")
result_time.displayTime()   


time3 = Time(1, 2)
print("Total minutes in time3:")
time3.displayMinute()        
