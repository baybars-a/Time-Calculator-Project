def add_time(start, duration, starting_day=None):
    def convert_to_24_hour(hour, am_pm):
        if am_pm == "PM" and hour != 12:
            return hour + 12
        elif am_pm == "AM" and hour == 12:
            return 0
        else:
            return hour

    def convert_to_12_hour(hour):
        if hour == 0:
            return 12, "AM"
        elif hour < 12:
            return hour, "AM"
        elif hour == 12:
            return 12, "PM"
        else:
            return hour - 12, "PM"

    start_parts = start.split()
    start_hour, start_minute = map(int, start_parts[0].split(':'))
    start_am_pm = start_parts[1]

    start_hour_24 = convert_to_24_hour(start_hour, start_am_pm)

    duration_hour, duration_minute = map(int, duration.split(':'))

    total_start_minutes = start_hour_24 * 60 + start_minute
    total_duration_minutes = duration_hour * 60 + duration_minute
    total_minutes = total_start_minutes + total_duration_minutes

    new_hour_24 = (total_minutes // 60) % 24
    new_minute = total_minutes % 60

    days_later = total_minutes // (24 * 60)

    new_hour, new_am_pm = convert_to_12_hour(new_hour_24)

    new_time = f"{new_hour}:{new_minute:02d} {new_am_pm}"

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
