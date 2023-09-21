def add_time(start, duration):
    start_clr = start.replace(':', ' ')
    start_clr = start_clr.split()
    stat = start_clr[2]
    duration_clr = duration.split(':')
    hrs = int(start_clr[0]) + int(duration_clr[0])
    min = int(start_clr[1]) + int(duration_clr[1])
    if hrs > 12:
        hrs = hrs - 12
    if min < 10:
        minstr = '0' + str(min)
    if min >59:
        minstr = min % 60
        hrs += 1



    print(start_clr, duration_clr)
    new_time = stat, hrs, minstr

    return new_time