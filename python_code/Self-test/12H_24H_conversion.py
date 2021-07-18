from datetime import datetime

def time_conversion(s):
    if s[-2:] == "AM":
        if s[0:2] == "12":
            date_string1 = "00" + s[2:-2]
        else:
           date_string1 = s[0:-2]
    elif s[-2:] == "PM":
        if s[0:2] == "12":
            date_string1 = s[0:-2]
        else:
            hrs = int(s[0:2]) + 12
            date_string1 = str(hrs) + s[2:-2]

    print(date_string1)

if __name__ == '__main__':
    s = '09:00:00PM'
    time_conversion(s)
