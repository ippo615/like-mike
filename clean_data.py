import json 
import csv
import os
import pandas as pd
import re
import sys


df = pd.read_csv('data-set1.csv')


df['diff_x'] = ''
df['diff_y'] = ''
df['diff_z'] = ''

#find difference

for rownum, row in df.iterrows():
	if rownum ==0:
		next
	else:
		diff_x = row['x'] - df.loc[rownum-1, 'x']
		df.loc[rownum, 'diff_x']= diff_x
		diff_y = row['y'] - df.loc[rownum-1, 'y']
		df.loc[rownum, 'diff_y']= diff_y
		diff_z = row['z'] - df.loc[rownum-1, 'z']
		df.loc[rownum, 'diff_z']= diff_z

df['time'] = ''
df['hour'] = ''
df['minute'] = ''
df['second'] = ''


#parse time and & find rows for every minute
for rownum, row in df.iterrows():
	# print row['created']
	# print type(row['created'])
	time = re.findall(r'(\d+:\d+:\d+)', str(row['created']))
 	df.loc[rownum, 'time']= time[0]

for rownum, row in df.iterrows():
	hour = re.findall(r'((\d+))', str(row['time']))
	df.loc[rownum, 'hour']= int(hour[0][0])

for rownum, row in df.iterrows():
	minute = re.findall(r':(\d+)', str(row['time']))
	df.loc[rownum, 'minute']= int(minute[0])

for rownum, row in df.iterrows():
	second = re.findall(r':\d+:(\d+)', str(row['time']))
	df.loc[rownum, 'second']= int(second[0])





# os.chdir('Stats.data/stats/tennis/wta')

# f = open('sample.json') 
# data = json.load(f) 
# f.close()
# f = open('data.csv') 
# csv_file = csv.writer(f) 
# for item in data: 
#     f.writerow(item) 
# f.close()

# data.keys()

# try:
# 	del data['this']
# except KeyError:
# 	pass

# for key in data:
# 	print key

# test = data['with']

# test2 = pd.DataFrame(test)

# # df2 = test2['content']
# # df = pd.concat(df2, axis=1)
# df = pd.DataFrame(test2)


# # separate the tilt values into separate columns

# df['tilt_z'] = ''
# df['tilt_x'] = ''
# df['tilt_y'] = ''

# for rownum, row in df.iterrows():
# 	# print row
# 	tilt_z = re.findall(r'tilt_z\': (\d*)', str(row['content']))
# 	df.loc[rownum, 'tilt_z']= tilt_z
# 	tilt_x = re.findall(r'tilt_x\': (\d*)', str(row['content']))
# 	df.loc[rownum, 'tilt_x']= tilt_x
# 	tilt_y = re.findall(r'tilt_y\': (\d*)', str(row['content']))
# 	df.loc[rownum, 'tilt_y']= tilt_x


# #convert to numeric values

# for rownum, row in df.iterrows():
# 	try:
# 		if len(row['tilt_z'])== 1:
# 			tilt_z = float(row['tilt_z'][0])
# 			df.loc[rownum, 'tilt_z']= tilt_z
# 	else:
# 		df.loc[rownum, 'tilt_z']= 0


# 		if len(row['tilt_x']) == 1:
# 			tilt_x = float(row['tilt_x'][0])
# 			df.loc[rownum, 'tilt_x']= tilt_x
# 		if len(row['tilt_y'])==1:
# 			tilt_y = float(row['tilt_y'][0])
# 			df.loc[rownum, 'tilt_y']= tilt_y
# 	except:
# 		# print e
# 		next

# #loop across the 4 rows in a seocnd in compute the difference 

# ##replace the empty values with 0
# for rownum, row in df.iterrows:
# 	print row['created']


# 	if row['tilt_z'] == '[]':
# 		print row['tilt_z']

# df['diff_x']

# for rownum, row in df.iterrows():
# 	i = 0
# 	if rownum ==0:
# 		next
# 	else:
# 		print row['tilt_x']
# 		print type(row['tilt_x'])
# 			if type(row['tilt_x'] == <type 'float'> & )
# 		diff_x = row['tilt_x'] - df[rownum-1]['tilt_x']
# 		df.loc[rownum, 'diff_x']= diff_x

# def clean_data(column):


# 		if len(row['tilt_x']) == 1:
# 			tilt_x = float(row['tilt_x'][0])
# 			df.loc[rownum, 'tilt_x']= tilt_x
# 		if len(row['tilt_y'])==1:
# 			tilt_y = float(row['tilt_y'][0])
# 			df.loc[rownum, 'tilt_y']= tilt_y
# 	except:
# 		# print e
# 		next

# #loop across the 4 rows in a seocnd in compute the difference 

# ##replace the empty values with 0
# for rownum, row in df.iterrows:
# 	print row['created']


# 	if row['tilt_z'] == '[]':
# 		print row['tilt_z']

# df['diff_x']

# for rownum, row in df.iterrows():
# 	i = 0
# 	if rownum ==0:
# 		next
# 	else:
# 		print row['tilt_x']
# 		print type(row['tilt_x'])
# 			if type(row['tilt_x'] == <type 'float'> & )
# 		diff_x = row['tilt_x'] - df[rownum-1]['tilt_x']
# 		df.loc[rownum, 'diff_x']= diff_x


