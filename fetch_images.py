from google_images_download import google_images_download
import csv
import re
from img_preprocess import img_preprocess
import os

# accept year as input from user
year = input("Enter the year: ")

# create output directories
try:
    os.makedirs(os.getcwd()+ '/Dataset/img')
except Exception as e:
    print(e)

# download the corresponding image to each trending tweet
def downloadimages(query, count):
	response = google_images_download.googleimagesdownload()
	arguments = {"keywords": query,
				"limit":1,
				"print_urls":True,
				"image_directory": str(year)}

	try:
		# paths = response.download(arguments)
		img_preprocess("./Dataset/img-black.jpg",query, count)

	# Handling File NotFound Error
	except FileNotFoundError:
		arguments = {"keywords": query,
					"format": "jpg",
					"limit":1,
					"print_urls":True,
					"image_directory": str(year),
					"size": "medium"}

		# Providing arguments for the searched query
		try:
			# Downloading the photos based
			# on the given arguments
			# paths = response.download(arguments)
			# img_preprocess(paths[0][query][0],query,count)
			img_preprocess("./Dataset/img-black.jpg",query, count)

		except:
			pass

count = 0
for month in range(1,13):
	file = './Dataset/trending/' + str(year) + '/' + str(month)
	try:
		with open(file) as f:
			print('Month: ', month)
			reader = csv.reader(f,delimiter = ",")
			for row in reader:
				# row_str = ','.join(row)
				for x in row:
					count += 1
					downloadimages(x, count)
	except Exception as e:
		print('Error in reading file: ',e)
		pass
# downloadimages("Dog")
print('Done!')
