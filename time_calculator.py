#start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive
def add_time(start, duration, *arg):
  start = start.replace(' ', ':').split(':')
  h, m, end = start[0], start[1], start[2]
  



    return new_time