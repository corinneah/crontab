#import packages 
import os
import sys 
import time
import pandas as pd
import json

# get current working directory
cwd = os.getcwd()
print(cwd)

#load API data 
Data = pd.read_json('https://health.data.ny.gov/resource/jbwf-vnai.json')
Data

#Export to CSV
Data.to_csv('data/Healthy_Neighborhoods_Program.csv')

# get the current time/ save as string
CurrentTime = time.time()
Time_Now = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(CurrentTime))
print('The Time Now Is: ', Time_Now)


# create a new file in the current working directory
with open(cwd + '/testFile_' + Time_Now + '.txt', 'w') as f:
    f.write(str(Data))