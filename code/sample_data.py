import pandas as pd
import numpy as np

data = pd.read_csv('data/final.csv')

data = data[data['subdivision'] == 'andhra pradesh']

data.to_csv('data/sample_data.csv')