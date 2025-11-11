## Function
This Python function, add_time(start, duration, starting_day=None), calculates the time that results from adding a specified duration to a given start time. It can also calculate the resulting day of the week if a starting day is provided.

## Features
Handles time addition across the AM/PM boundary.
Correctly calculates the number of days elapsed ((next day) or (N days later)).
Optionally tracks and returns the resulting day of the week.

## Usage
**Function Signature:**
def add_time(start, duration, starting_day=None):
    # ... function implementation ...

## Parameters
Parameter	      Type	          Description
start	          str	            The starting time in 12-hour format (e.g., "3:00 PM", "11:40 AM").
duration	      str	            The duration to add, in "HH:MM" format (e.g., "1:00", "24:30").
starting_day	  str (Optional)	The starting day of the week (case-insensitive, e.g., "Monday", "tuesday").

## Returns
**Type	Description**
str   The new time in 12-hour format, including the new day and days later information as necessary.

## Implementation Details
1. **Parsing:** Splits the start and duration strings into hours, minutes, and AM/PM indicators.
2. **Conversion to Minutes:** Converts the start time to a total number of minutes from the beginning of the day (00:00 or 12:00 AM) using a 24-hour clock.
3. **Addition:** Adds the total duration minutes to the total start minutes.
4. **New Time Calculation:** The total minutes are used to calculate the new hour, minute, and the number of full days later.
   ***New 24-hour clock hour: (total_minutes / 60) mod(24)***
   ***Days later: total_minutes / (24 * 60)***
5. **Formatting:** The new 24-hour time is converted back to the 12-hour format with AM/PM.
6. **Day of the Week Calculation:** If a starting_day is provided, it calculates the new day's index using the formula: (starting_day_index + days_later) mod(7)
