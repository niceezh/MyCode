from datetime import date


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def meetup(year, month, week, day_of_week):
    WEEKDAYMAP = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    baseday = (WEEKDAYMAP[day_of_week] - date(year, month, 1).isoweekday()) % 7 + 1
    targetday = 0
    for _ in range(1):
        if week == 'first':
            targetday = baseday
            break
        if week == 'second':
            targetday = baseday + 7
            break
        if week == 'third':
            targetday = baseday + 14
            break
        if week == 'fourth':
            targetday = baseday + 21
            break
        if week == 'fifth':
            targetday = baseday + 28
            break
        if week == 'teenth':
            targetday = baseday + 7
            if targetday < 13:
                targetday += 7
            break
        if week == 'last':
            targetday = baseday + 28
            try:
                date(year, month, targetday)
            except:
                targetday -= 7
            break
    try:
        return date(year, month, targetday)
    except:
        raise MeetupDayException('That day does not exist.')


if __name__ == '__main__':
    print(meetup(2013, 1, 'first', 'Monday'))
