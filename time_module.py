# *************************************************************************
import time
# *************************************************************************
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time
print("*" * 100)
# *************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
time_object = time.localtime() # local time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(local_time)
time_object = time.gmtime()  # UTC time
utc_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
print(utc_time)
print("*" * 100)
# *************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)
print("*" * 100)
# *************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)
print("*" * 100)
# *************************************************************************
#time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)
print("*" * 100)
# *************************************************************************