class TimeSpan:

    def __init__(self, hrs, mins):
        self.hours = hrs
        self.minutes = mins

    def show(self):
        print(f'{self.hours} hours and {self.minutes} minutes.')

    def add_hours(self, hrs):
        hours = self.hours + hrs
        print(f'{hours} hours and {self.minutes} minutes.')

    def add_minutes(self, mins):
        while self.minutes + mins > 60:
            self.hours = self.hours + 1
            mins = mins - 60
        self.minutes = self.minutes + mins
        print(f'{self.hours} hours and {self.minutes} minutes.')

    def change(self, ts):
        time_self = self.hours * 60 + self.minutes
        time_ts = ts.hours * 60 + ts.minutes
        difference = time_ts - time_self
        print(difference)

class TimeSpan2:

    def __init__(self, mins):
        self.minutes = mins

    def show(self):
        hours = self.minutes // 60
        mins = self.minutes % 60
        print(f'{hours} hours and {mins} minutes.')

    def add_hours(self, hrs):
        hours = (self.minutes // 60)  + hrs
        mins = self.minutes % 60
        print(f'{hours} hours and {mins} minutes.')

    def add_minutes(self, mins):
        # hours = (self.minutes // 60)
        # self.minutes = self.minutes % 60
        # while self.minutes + mins > 60:
        #     hours = hours + 1
        #     mins = mins - 60
        # minutes = self.minutes + mins
        self.minutes += mins
        hours = self.minutes // 60
        minutes = self.minutes % 60
        print(f'{hours} hours and {minutes} minutes.')

    def change(self, ts):
        difference = ts.minutes - self.minutes
        print(difference)