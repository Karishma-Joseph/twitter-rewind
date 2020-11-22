from google_images_download import google_images_download
import csv

year = input("Enter the year: ")

def downloadimages(query):
	response = google_images_download.googleimagesdownload() 
	arguments = {"keywords": query, 
				"limit":1,
				"print_urls":True,
				"image_directory": str(year)}

	try: 
		paths = response.download(arguments) 
		print(paths)
	
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
			response.download(arguments) 
		except: 
			pass


# for month in range(1,13):
# 	file = './Dataset/trending/' + str(year) + '/' + str(month)
# 	try:
# 		with open(file) as f:
# 			print('Month: ', month)
# 			reader = csv.reader(f,delimiter = ",")
# 			for row in reader:
# 				row_str = ','.join(row)
# 				# print(row_str)
# 				downloadimages(row_str)
# 			break
# 	except Exception as e:
# 		print('Error: ',e)
# 		exit(0)
downloadimages("dog, cat, cow")
print('Done!')
