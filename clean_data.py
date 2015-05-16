import json 
import csv
import os
import pandas as pd
import re
import sys


os.chdir('Stats.data/stats/tennis/wta')

f = open('sample.json') 
data = json.load(f) 
f.close()
f = open('data.csv') 
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

test = data['with']

test2 = pd.DataFrame(test)

# df2 = test2['content']
# df = pd.concat(df2, axis=1)
df = pd.DataFrame(test2)


# separate the tilt values into separate columns

df['tilt_z'] = ''
df['tilt_x'] = ''
df['tilt_y'] = ''

for rownum, row in df.iterrows():
	# print row
	tilt_z = re.findall(r'tilt_z\': (\d*)', str(row))
	df.loc[rownum, 'tilt_z']= tilt_z
	tilt_x = re.findall(r'tilt_x\': (\d*)', str(row))
	df.loc[rownum, 'tilt_x']= tilt_x
	tilt_y = re.findall(r'tilt_y\': (\d*)', str(row))
	df.loc[rownum, 'tilt_y']= tilt_x


#convert to numeric values

for rownum, row in df.iterrows():
	try:
		if len(row['tilt_z'])== 1:
			tilt_z = float(row['tilt_z'][0])
			df.loc[rownum, 'tilt_z']= tilt_z
		if len(row['tilt_x']) == 1:
			tilt_x = float(row['tilt_x'][0])
			df.loc[rownum, 'tilt_x']= tilt_x
		if len(row['tilt_y'])==1:
			tilt_y = float(row['tilt_y'][0])
			df.loc[rownum, 'tilt_y']= tilt_y
	except:
		# print e
		next


