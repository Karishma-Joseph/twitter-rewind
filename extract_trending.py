import csv
import os

# accept year as input from user
year = input('Enter year: ')

# create output directories
try:
    os.makedirs('./Dataset/trending/'+str(year))
except Exception as e:
    print(e)

# extract the tweets that are trending each month and the top tweet everyday
for month in range(1,13):
    month_data = None
    top_of_month = set()
    file = './Dataset/' + str(year) + '/' + str(month).zfill(2)
    try:
        with open(file) as f:
            print('Month: ', month)
            reader = csv.reader(f,delimiter = ",")
            for row in reader:
                a = set(row)
                if not month_data:
                    month_data = a
                else:
                    month_data = month_data.intersection(a)
                if len(row) > 0:
                    top_of_month = top_of_month.union(set([row[0]]))
            month_data = month_data.union(top_of_month)
            with open('./Dataset/trending/'+ str(year) + '/'+ str(month),'w') as f:
                write = csv.writer(f)
                write.writerow(list(month_data))
    except Exception as e:
        print('Error: ',e)
        print('Upto date!')
        exit(0)
print('Done!')