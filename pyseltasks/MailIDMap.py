# Project:pyseltask2_MailIDMap
# Author:Vijaykumar Sambanni (798705)

import logging
import time

# calculating execution time
start_time = time.time()
logging.basicConfig(level=logging.INFO)
# Log info start
logging.info("Code execution started")

# names.txt file loaded to directory

# read names and provide reference
names = open("names.txt", "r")

# list for names
namelist = [names]

# Replace empty spaces with underscore
namelist = names.read().replace(" ", "_").lower().split()

# To remove duplicates
temp = []
for x in namelist:
    if x not in temp:
        temp.append(x)

namelist = temp
print(namelist)

# Create Mail IDs
def email(namelist):
    return namelist + "@pydemo.com"

MailIDs = list(map(email, namelist))
print (MailIDs)

# Write into names_updated
with open("names_updated.txt", "w") as updatedfile:
    for i in MailIDs:
        updatedfile.write(i+ '\n')

names.close()
# Log info end
logging.info("Code Ran Successfully")

# time taken for execution
print("Execution time -- %s seconds --" % (time.time() - start_time))
print('time in seconds{0:.2f}'.format((time.time() - start_time)))