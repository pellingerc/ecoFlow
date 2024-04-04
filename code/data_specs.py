import pandas as pd

cols = ['Jan-Feb','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC', 'Flood Count']
data  = pd.read_csv('data/final.csv')


for i in cols:
    #get range of each column
    print(i)
    print (data[i].max())
    print (data[i].min())