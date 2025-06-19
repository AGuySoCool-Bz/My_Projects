import time
ts = int(time.strftime('%H'))
print(ts)


if ts<12:
  print('GOOD MORNING!!!')
elif ts>=12 and ts<17:
  print('GOOD AFTERNOON!!!')
elif ts>=17:
  print('GOOD EVENING!!!')

  
