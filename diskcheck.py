import shutil

total, used, free = shutil.disk_usage("/")
print("Total Gb:", total // (2**30))
print("used Gb:", total // (2**30))
print("free Gb:", free // (2**30))  
