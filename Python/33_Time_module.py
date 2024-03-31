import time

# print(4)
# time.sleep(3)
# print("line is printed after 3 secs")

t=time.localtime()
print(t)
#strftime converts time to specified string format
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)




# The time module in Python provides various time-related functions. 
# It allows you to work with time in various formats, measure time intervals,
#  and perform other time-related operations. Here are some of the commonly used functions 
#  and constants in the time module:

# time.time(): Returns the current time in seconds since the Epoch (January 1, 1970, UTC).
# time.sleep(seconds): Suspends execution of the current thread for the given number of seconds.
# time.localtime([secs]): Converts a time expressed in seconds since the Epoch to a time tuple representing local time.
# time.gmtime([secs]): Similar to localtime(), but converts to a time tuple representing UTC time.
# time.strftime(format[, t]): Converts a time tuple or struct_time object (like those returned by localtime() 
    # and gmtime()) to a string according to the specified format.
# time.strptime(string, format): Parses a string representing a time according to the specified format and returns a time tuple.
# time.mktime(t): Takes a time tuple and returns the corresponding number of seconds since the Epoch.
# time.clock(): Returns the current processor time as a floating-point number expressed in seconds on Unix systems.
# time.process_time(): Returns the current CPU time as a floating-point number expressed in seconds on Unix systems.
# time.monotonic(): Returns the value (in fractional seconds) of a monotonic clock, which cannot go backward. Useful for measuring time intervals.
# time.perf_counter(): Returns the value (in fractional seconds) of a performance counter, which includes time elapsed during sleep.
# time.time_ns(): Returns the current time in nanoseconds.
# time.sleep_ns(nanoseconds): Suspends execution for the given number of nanoseconds.
