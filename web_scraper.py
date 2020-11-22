import re
from urllib.request import urlopen
import csv
import contextlib

# dictonary mapping number of days to each month
days_per_month = {'01':'31','02':None,'03':'31','04':'30','05':'31','06':'30','07':'31','08':'31','09':'30','10':'31','11':'30','12':'31'}

# accept year as input from user
year = input("Enter the year: ")

# check if leap year 
if int(year)%4 == 0:
    days_per_month['02'] = 29
else:
    days_per_month['02'] = 28

# fetch the top 50 trends for everyday of that year
for month,days in days_per_month.items():
    res_month = []
    for day in range(1,int(days)+1):
        print("month: ",month," day: ",str(day).zfill(2))
        url = "https://us.trend-calendar.com/trend/"+str(year)+'-'+month+'-'+str(day).zfill(2)+'.html'
        try:
            with contextlib.closing(urlopen(url)) as page:
            # page = urlopen(url)
                html = page.read().decode("utf-8")
                pattern = "<li><a.*?twitter.*?>.*?</li>"
                match_results = re.findall(pattern,html, re.IGNORECASE)
                res_day = []
                for x in match_results:
                    res_day.append(re.sub("<.*?>","",x))
                res_month.append(res_day)
        except Exception as e:
            print("error: "e)
            if len(res_month) > 0:
                with open(month,'w') as f:
                    write = csv.writer(f)
                    write.writerows(res_month)
                print('Upto date')
            exit(0)
    with open(month,'w') as f:
        write = csv.writer(f)
        write.writerows(res_month)
print('done!')


        