import numpy as np
import pandas as pd
from sklearn import tree

input_file = "D:\Hopvinna\Machine_Learning\PastHires.csv"
#input_file = "D:\Hopvinna\Machine_Learning\Table-Youth-and-Adult-Literacy-Rate-updated-Oct.-2015_78.xlsx"
df = pd.read_excel(input_file,header=0)
print(df.head())