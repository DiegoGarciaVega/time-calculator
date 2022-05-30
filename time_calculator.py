def add_time(start, duration, *day):
  #Auxiliary array for days of the week
  Week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday', 'Sunday']
  # Split first argument in time and meridium
  aux = start.split()
  time = aux[0]
  meridium = aux[1]
  # Split time in hours and minutes
  aux = time.split(":")
  StHours = int(aux[0])
  StMinutes = int(aux[1])
  # Split duration in hours and minutes
  aux = duration.split(":")
  DHours = int(aux[0])
  DMinutes = int(aux[1])

  #  Calculate time in 24h format
  if meridium == "PM":
    StHours += 12
  time = ""
  FMinutes = (DMinutes + StMinutes) % 60
  aux = (DHours + StHours + ((DMinutes + StMinutes) // 60))
  FHours = aux % 24
  #Transform in AM/PM format
  if FHours >= 12:
    meridium = " PM"
    if FHours > 12:
      FHours -= 12
  else:
    meridium = " AM"
  #Calculate days that have passed
  days = aux // 24
  #Format String
  if days == 0:
    Sdays = ""
  elif days == 1:
    Sdays = " (next day)"
  else:
    Sdays = " ({} days later)".format(days)
  if FHours == 0:
    FHours = 12
  new_time = "{:n}:{:02n}{}{}".format(FHours, FMinutes, meridium, Sdays)
  
  if bool(day):
    day = day[0].capitalize()
    day = Week[(Week.index(day) + days)%7]
    new_time = "{:n}:{:02n}{}, {}{}".format(FHours, FMinutes, meridium,day,Sdays)
  return new_time