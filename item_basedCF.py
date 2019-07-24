import pandas as pd
import numpy as np

r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('C:/Users/Arun/Downloads/MLCourse/MLCourse/ml-100k/u.data', sep='\t', names = r_cols, usecols=range(3), encoding='ISO-8859-1')


m_cols = ['movie_id', 'title']
movies = pd.read_csv('C:/Users/Arun/Downloads/MLCourse/MLCourse/ml-100k/u.item', sep='|', names = m_cols, usecols=range(2), encoding='ISO-8859-1')

ratings = pd.merge(movies, ratings)

print(ratings.head())
userRatings = ratings.pivot_table(index=['user_id'], columns=['title'],values=['rating'])
print(userRatings.head())

corrMatrix = userRatings.corr()
corrMatrix = userRatings.corr(method="pearson",min_periods=100)

myRatings = userRatings.loc[0].dropna()
print(myRatings)

simCandidates = pd.Series()
for i in range(0, len(myRatings.index)):
    print ("Adding sims for " + myRatings.index[i] + "...")
    sims = corrMatrix[myRatings.index[i]].dropna()
    sims = sims.map(lambda x: x * myRatings[i])

    simCandidates = simCandidates.append(sims)

print("Sorting..")
simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head())

simCandidates = simCandidates.groupby(simCandidates.index).sum()

simCandidates.sort_values(inplace = True, ascending = False)
print(simCandidates.head())
