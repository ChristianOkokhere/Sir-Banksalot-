import datetime 



#this first function will tell when called will get the current date and time
def gettime():
  current_info = datetime.datetime.now()
  return((current_info.hour, (current_info.month, current_info.day)))







