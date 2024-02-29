def add_time(start, duration, day="Nan"):

    day = day[0].upper() + day[1:].lower()

    arr_start = start.split(':')
    arr_duration = duration.split(':')

    arr_day = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    #Minutes Hours Days
    arr_new_time = [
        int(arr_start[1][:2]) + int(arr_duration[1][:2]),
        int(arr_start[0]) + int(arr_duration[0]),
        0 if day=='Nan' else arr_day.index(day)
    ]

    current_day = arr_new_time[2]

    if arr_start[1][-2:] == 'PM':
        arr_new_time[1] += 12
    
    arr_new_time[1] += arr_new_time[0]//60
    arr_new_time[0] %= 60

    arr_new_time[2] += arr_new_time[1]//24
    arr_new_time[1] %= 24

    #return new_time
    new_time = f"{ (arr_new_time[1]-1)%12+1}:{format(arr_new_time[0],'02d')} {'AM' if arr_new_time[1] < 12 else 'PM'}"

    if day != "Nan":
        new_time += f", {arr_day[arr_new_time[2]%7]}"

    arr_new_time[2] -= current_day

    if arr_new_time[2] == 1:
        new_time += " (next day)"
    elif arr_new_time[2] > 1:
        new_time += f" ({arr_new_time[2] - current_day} days later)"
    return new_time

if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tueSday"))
    print(add_time("6:30 PM", "205:12"))
    print(add_time("3:30 PM", "2:12", "Monday"))
    print(add_time("2:59 AM", "24:00", "saturDay"))
    print()
    print()
    print()
