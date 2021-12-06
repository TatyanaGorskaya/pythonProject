seconds = int(input('Please input seconds: '))

hours = seconds // 3600

minutes = (seconds // 60) - hours * 60

seconds = seconds - hours * 3600 - minutes * 60

Time = str(hours)+':'+str(minutes)+':'+str(seconds)

print('')
print('Time is:', Time)
