#!/usr/bin/env python
# coding: utf-8

# <p>
#     <img src="https://s3.amazonaws.com/iotanalytics-templates/Logo.png" style="float:left;width:65px">
#     <h1 style="float:left;color:#1A5276;padding-left:15px;font-size:20px;">AWS IoT Analytics | Notebook</h1>
# </p>
# 

# When loading data from IoT Analytics datasets, the client should be initialized first:

# In[39]:


import boto3

# create IoT Analytics client
client = boto3.client('iotanalytics')

from IPython.display import HTML

HTML('''<script>
code_show=true; 
function code_toggle() {
 if (code_show){
 $('div.input').hide();
 } else {
 $('div.input').show();
 }
 code_show = !code_show
} 
$( document ).ready(code_toggle);
</script>
<form action="javascript:code_toggle()"><input type="submit" value="Click here to toggle on/off the raw code."></form>''')


# Starting to do analytics on data received from the devices

# In[40]:


# Create Sensor Data Objects
class sensor_data:
   def __init__(self, temp, humid, lux, time):
    self.temp = temp
    self.humid = humid
    self.lux = lux
    self.time = time


# In[41]:


from urllib.request import Request, urlopen
import gzip
import sys
import csv

dataset = "iot_analytics_sensor_data_set"
dataset_url = client.get_dataset_content(datasetName = dataset, versionId = '$LATEST')['entries'][0]['dataURI']
#print(dataset_url)

req = Request(dataset_url)
response = urlopen(req)
content = response.read()
decomp_req = content.splitlines()

reader = csv.reader(response, delimiter=",")
sortedlist = sorted(reader, key=lambda row: row[3], reverse=True)

att = decomp_req.pop(0).decode('utf8')
attributes = (att.replace('\"', ''))
#print(attributes)

humid = []
tem = []
lux = []
timestamp = []
data_arr = []

for line in decomp_req:
    li = line.decode('utf8').replace('\"', '')
    data = li.split(",")
    humid.append(float(data[0]))
    tem.append(float(data[1]))
    lux.append(float(data[2]))
    timestamp.append(int(float(data[3])))
    data_arr.append(sensor_data(float(data[0]),float(data[1]),float(data[2]),int(float(data[3]))))
    
#print(humid)
#print(tem)
#print(lux)
#print(timestamp)
    
    
# start working with the data


# <div style="height:60px;"><div style="height:7px;background-color:#20B3CD;width:100%;margin-top:20px;position:relative;"><img src="https://s3.amazonaws.com/iotanalytics-templates/Logo.png" style="height:50px;width:50px;margin-top:-20px;position:absolute;margin-left:42%;"></div></div>

# In[43]:


import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import matplotlib.dates as mdate

import numpy as np

# Convert to the correct format for matplotlib.
# mdate.epoch2num converts epoch timestamps to the right format for matplotlib
secs = mdate.epoch2num(timestamp)

# print(secs)
# print(humid)

#Setting Figure 1
plt.figure(1)
fig, ax = plt.subplots()

# Plot the date using plot_date rather than plot
ax.plot_date(secs, humid)

# Choose your xtick format string
date_fmt = '%d-%m-%y %H:%M:%S'

# Use a DateFormatter to set the data to the correct format.
date_formatter = mdate.DateFormatter(date_fmt)
ax.xaxis.set_major_formatter(date_formatter)

# Sets the tick labels diagonal so they fit easier.
fig.autofmt_xdate()

#Setting Figure 2
plt.figure(2)
fig2, ax2= plt.subplots()
ax2.plot_date(secs, tem)
ax2.xaxis.set_major_formatter(date_formatter)

fig2.autofmt_xdate()

#Setting Figure 3
plt.figure(3)
fig3, ax3= plt.subplots()
ax3.plot_date(secs, lux)
ax3.xaxis.set_major_formatter(date_formatter)

fig3.autofmt_xdate()

plt.show()


# In[37]:


# Sorting Data Objects

data_arr.sort(key=lambda x : x.time)
newlist = sorted(data_arr, key = lambda x : x.time)


# In[44]:



for dat in newlist:
    print("Temperature: " + str(dat.temp) + ", Humidity: " + str(dat.humid) 
          + ", Lux: " + str(dat.lux) + ", Timestamp: " + str(dat.time))


# In[ ]:





# In[ ]:




