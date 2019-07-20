import pandas as pd
import seaborn as sns



df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
gear_counts = df['# Gears'].value_counts()

print(gear_counts.plot(kind='bar'))
print(df.head())
print(sns.scatterplot(df['CombMPG']))
