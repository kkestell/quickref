import time

# Get the current time in seconds since the epoch
current_time = time.time()
print(current_time)  # e.g. 1614130003.733982

# Convert seconds since epoch to a struct_time object (a named tuple)
time_tuple = time.gmtime(current_time)
print(time_tuple)  # e.g. time.struct_time(tm_year=2021, tm_mon=2, tm_mday=24, tm_hour=6, tm_min=20, tm_sec=3, tm_wday=2, tm_yday=55, tm_isdst=0)

# Convert a struct_time object to seconds since the epoch
time_in_seconds = time.mktime(time_tuple)
print(time_in_seconds)  # e.g. 1614130803.0

# Sleep for a certain number of seconds
time.sleep(1)  # sleep for 1 second

# Format a struct_time object as a string
time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print(time_string)  # e.g. 2021-02-24 06:20:03

# Parse a string representing a date/time to a struct_time object
time_string = "2021-02-24 06:20:03"
time_tuple = time.strptime(time_string, "%Y-%m-%d %H:%M:%S")
print(time_tuple)  # e.g. time.struct_time(tm_year=2021, tm_mon=2, tm_mday=24, tm_hour=6, tm_min=20, tm_sec=3, tm_wday=2, tm_yday=55, tm_isdst=-1)

# Get the CPU time in seconds since the start of the program
cpu_time = time.process_time()
print(cpu_time)  # e.g. 0.305871

# Get the CPU time in seconds since the start of the program (more precise than process_time())
cpu_time = time.perf_counter()
print(cpu_time)  # e.g. 69.0116906

# Get the CPU time in seconds since an arbitrary point in time
cpu_time = time.monotonic()
print(cpu_time)  # e.g. 52322.0816759
