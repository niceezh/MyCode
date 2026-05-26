class Clock:
    def __init__(self, hour, minute):
        self.minutes = (hour * 60 + minute) % 1440

    def __repr__(self):
        hour, minute = divmod(self.minutes, 60)
        return f'Clock({hour}, {minute})'

    def __str__(self):
        hour, minute = divmod(self.minutes, 60)
        return f'{hour:02d}:{minute:02d}'

    def __eq__(self, other):
        return self.minutes == other.minutes

    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)
