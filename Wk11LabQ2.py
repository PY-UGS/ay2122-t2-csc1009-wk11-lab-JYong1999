class clockTime:

    def __init__(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def setHours(self, hours):
        if(hours <= 9):
            self.hours = "0" + str(hours)
        else: 
            self.hours = str(hours)

    def setMinutes(self, mins):
        if(mins <= 9):
            self.mins = "0" + str(mins)
        else: 
            self.mins = str(mins)

    def setSeconds(self, secs):
        if(secs <= 9):
            self.secs = "0" + str(secs)
        else: 
            self.secs = str(secs)

    def setTime(self, hours, mins, secs):
        self.setHours(hours)
        self.setMinutes(mins)
        self.setSeconds(secs)

    def showTime(self):
        print("Time now is " + self.hours + ":" + self.mins + ":" + self.secs)

clock = clockTime(0,0,0)
hours = int(input("\nSet Hours(0-23): "))
mins = int(input("Set Minutes(0-59): "))
secs = int(input("Set Seconds(0-59): "))
clock.setTime(hours,mins,secs)
clock.showTime()