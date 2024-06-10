# transforming date and time in a comapact 24 hr time to a 12 hr formmat
# Dhiya Ramadhar
# 19/04/2021

date_time = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")
am_pm = ""
suffix = ""
day = ""
month = ""
date_output = ""
temp2 = ''

if date_time[11:13]  >= '0' and date_time[11:13] < '12': # selects the hour part of the time and determines whether its am or pm
    am_pm = "am"
else:
    am_pm = "pm"

if date_time[8:10] == '11':
    suffix = 'th'
elif date_time[9:10] == '1': # Selects the last number in the date part and determines the suffix of the day ie first/second/third etc.
    suffix  = "st"
elif date_time[9:10] == '2':
    suffix = 'nd'
elif date_time[9:10] == '3':
    suffix = 'rd'
else:
    suffix = 'th'

if date_time[8:9] == '0': #omits the 0 from the day if the input starts with a zero
    day = date_time[9:10]
else:
    day = date_time[8:10]

if date_time[5:7] == '01': # Selects the month part of the input and converts it to text
    month = 'January'
elif date_time[5:7] == '02':
    month = 'February'
elif date_time[5:7] == '03':
    month = 'March'
elif date_time[5:7] == '04':
    month  = 'April'
elif date_time[5:7] == '05':
    month = 'May'
elif date_time[5:7] == '06':
    month = 'June'
elif date_time[5:7] == '07':
    month = 'July'
elif date_time[5:7] == '08':
    month = 'August'
elif date_time[5:7] == '09':
    month = 'September'
elif date_time[5:7] == '10':
    month = 'October'
elif date_time[5:7] == '11':
    month = 'November'
elif date_time[5:7] == '12':
    month = 'December'

if date_time[11:13]  > '00' and date_time[11:13] < '10': # Checks if the time entered is between 0 and 12
    date_output = date_time[12:16]
elif date_time[11:13] >= '10' and date_time[11:13] <= '12':
    date_output = date_time[11:16]
elif date_time[11:13] == '00':
    temp2 = str(int(date_time[11:13]) + 12)
    date_output = temp2 + date_time[13:16]
elif date_time[11:13] > '12':
    temp = str(int(date_time[11:13]) - 12) # converts the time to an integer value, subtracts 12 and reconverts the value to a string
    date_output = temp + date_time[13:16]
print(date_output, am_pm, "on the", day,end='')
print(suffix, "of", month, "\'",end='')
print(date_time[2:4])
