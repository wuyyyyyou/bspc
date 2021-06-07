class OperationTime:
    def __init__(self, year: str, month: str, day: str, hour: str, minuit: str):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minuit = minuit

    def __repr__(self):
        return "[{},{},{},{},{}]".format(self.year, self.month, self.day, self.hour, self.minuit)

    def __str__(self):
        return "[{},{},{},{},{}]".format(self.year, self.month, self.day, self.hour, self.minuit)