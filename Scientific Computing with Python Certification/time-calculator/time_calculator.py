def add_time(start, duration, day=None):
    hour, minutes = start.split(':')
    minutes, am_pm = minutes.split()
    add_hour, add_min = duration.split(":")
    hour = int(hour)
    minutes = int(minutes)
    add_hour = int(add_hour)
    add_min = int(add_min)
    n = add_hour // 24
    rem_hour = add_hour % 24
    new_min = minutes + add_min
    extra_hour = new_min // 60
    new_min = new_min % 60
    new_min = str(new_min).rjust(2, '0')
    rem_hour = rem_hour + extra_hour
    extra_n = rem_hour // 24
    rem_hour = rem_hour % 24
    n = n + extra_n
    new_hour = hour + rem_hour
    changes = new_hour // 12
    final_hour = new_hour % 12
    if changes == 0:
        am_pm = am_pm
    elif changes == 1:
        if am_pm == 'AM':
            am_pm = 'PM'
        else:
            am_pm = 'AM'
            n = n + 1
    elif changes == 2:
        am_pm = am_pm
        n = n + 1
    if day is not None:
        day = day.lower()
        weekdays = {'monday': 0, 'tuesday': 1, "wednesday": 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
        day = weekdays[day] + n
        day = day % 7
        day = list(weekdays.keys())[list(weekdays.values()).index(day)]
        day = day.capitalize()
    if final_hour == 0:
        final_hour = 12
    if not n and day is None:
        return f"{final_hour}:{new_min} {am_pm}"
    if n and day is None:
        if n == 1:
            return f"{final_hour}:{new_min} {am_pm} (next day)"
        else:
            return f"{final_hour}:{new_min} {am_pm} ({n} days later)"
    if not n and day:
        return f"{final_hour}:{new_min} {am_pm}, {day}"
    if n and day:
        if n == 1:
            return f"{final_hour}:{new_min} {am_pm}, {day} (next day)"
        else:
            return f"{final_hour}:{new_min} {am_pm}, {day} ({n} days later)"
