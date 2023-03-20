import os
from tkinter import *
import random
from connector import *

def convertToBinaryData(filename):
	# Convert digital data to binary format
	with open(filename, 'rb') as file:
		binaryData = file.read()
	return binaryData


def insertBLOB(id, photo):
	#Connecting to sql server
		
		connection = connectDb()

		if (connection):
			cursor = connection.cursor()
			sql_insert_blob_query = """ INSERT INTO allImages
							(images_id, img) VALUES (%s,%s)"""

			picture = convertToBinaryData(photo)

			# Convert data into tuple format
			insert_blob_tuple = (id, picture)
			result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
			connection.commit()
			#inserting image as blob into the database

		if connection.is_connected():
			cursor.close()
			connection.close()
			#Closing the MySQL connection


def write_file(data, filename):
	# Convert binary data to proper format and write it on Hard Disk
	with open(filename, 'wb') as file:
		file.write(data)


def readBLOB(id, photo):
	#Connecting to sql database to read blob data from database

	connection = connectDb()

	if connection:
		cursor = connection.cursor()
		sql_fetch_blob_query = """SELECT img from allImages where images_id = %s"""
		sql_fetch_count_images_query = """SELECT count(images_id) from allImages where images_id = %s"""

		cursor.execute(sql_fetch_count_images_query, (id,))
		record = cursor.fetchall()

		count = record[0][0]

		img_no = random.randint(0,count-1)

		cursor.execute(sql_fetch_blob_query, (id,))
		record = cursor.fetchall()

		# print(img_no)
		image = record[img_no][0]
		#Retrieving a random image from the database of each category
		#Writing the file onto a temp file
		write_file(image, photo)

	if connection.is_connected():
		cursor.close()
		connection.close()
		#Closing the Database connection

# directory = r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\Images\tomatoes"

# for filename in os.listdir(directory):
# 	f = os.path.join(directory, filename)
# 	insertBLOB(3,f)


directory = r"C:\Users\pvedk\Desktop\programming\miniProject_Sem_III\dispImages"

dispOrder = random.sample(range(1,10), 9)

f=[]

for filename in os.listdir(directory):
	f.append(os.path.join(directory, filename))

posImgID={}

temp = 0
for i in dispOrder:
	readBLOB(i, f[temp])
	posImgID[temp+1]=i
	temp += 1
