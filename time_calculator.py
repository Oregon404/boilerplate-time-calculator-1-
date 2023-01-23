#start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive
def add_time(start, duration, *args):
  start = start.replace(' ', ':').split(':')
  duration = duration.split(':')
  t = (int(start[1]) + int(duration[1])) // 60
  m = (int(start[1]) + int(duration[1])) % 60
  h = (int(start[0]) + int(duration[0]) + t)
  end, day = start[2], ''
  if end == 'PM':
    h += 12
  t = h // 24
  if (h % 24) - 12 >= 0:
    end = 'PM'
  else:
    end = 'AM'
  h = h % 12
  if h == 0:
    h = 12
  if args:
    week = [
      'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
      'Saturday'
    ]
    day = f', {week[(week.index(str(args[0]).title()) + t) % 7]}'
  if t == 1:
    day = day + ' (next day)'
  if t > 1:
    day = day + f' ({t} days later)'
  return (f'{h}:{m:02d} {end}{day}')
