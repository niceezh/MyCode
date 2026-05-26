from datetime import datetime, timedelta

def delivery_date(start, description):
    start_time = datetime.strptime(start, '%Y-%m-%dT%H:%M:%S')
    if description == 'NOW':
        end_time = start_time + timedelta(hours=2)
        return end_time.strftime('%Y-%m-%dT%H:%M:%S')
    if description == 'ASAP':
        if start_time.hour < 13:
            end_time = start_time.replace(hour=17, minute=0, second=0)
            return end_time.strftime('%Y-%m-%dT%H:%M:%S')
        end_time = start_time + timedelta(days=1)
        end_time = end_time.replace(hour=13, minute=0, second=0)
        return end_time.strftime('%Y-%m-%dT%H:%M:%S')
    if description == 'EOW':
        weekday = start_time.isoweekday()
        if weekday in [1, 2, 3]:
            end_time = start_time + timedelta(days=(5-weekday))
            end_time = end_time.replace(hour=17, minute=0, second=0)
            return end_time.strftime('%Y-%m-%dT%H:%M:%S')
        if weekday in [4, 5]:
            end_time = start_time + timedelta(days=(7-weekday))
            end_time = end_time.replace(hour=20, minute=0, second=0)
            return end_time.strftime('%Y-%m-%dT%H:%M:%S')
    if 'M' in description:
        target_month = int(description[:-1])
        month = start_time.month
        if target_month > month:
            end_time = start_time.replace(month=target_month, day=1, hour=8, minute=0, second=0)
        else:
            end_time = start_time.replace(year=start_time.year+1, month=target_month, day=1, hour=8, minute=0, second=0)
        weekday = end_time.isoweekday()
        if weekday in [6, 7]:
            end_time = end_time + timedelta(days=(8-weekday))
        return end_time.strftime('%Y-%m-%dT%H:%M:%S')
    if 'Q' in description:
        target_quarter = int(description[1:])
        target_month = target_quarter * 3
        target_day = 31 if target_month in [3, 12] else 30
        month = start_time.month
        if target_month >= month:
            end_time = start_time.replace(month=target_month, day=target_day, hour=8, minute=0, second=0)
        else:
            end_time = start_time.replace(year=start_time.year+1, month=target_month, day=target_day, hour=8, minute=0, second=0)
        weekday = end_time.isoweekday()
        if weekday in [6, 7]:
            end_time = end_time - timedelta(days=(weekday-5))
        return end_time.strftime('%Y-%m-%dT%H:%M:%S')
    return start

if __name__ == '__main__':
    print(delivery_date("2013-11-21T15:30:00", "11M"))
