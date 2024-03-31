import time
timestamp=time.strftime("%H:%M:%S")
print(timestamp)
timestamp2=int(time.strftime("%H"))
if(timestamp2<12):
 print("good morning")
elif(timestamp2>=12 & timestamp2<=4):
  print("good evening")
else:
 print("good night")

