import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

path = r"D:\Semester 4\Machine Learning Lab\housing.csv"
BostonTrain = pd.read_csv(path)
print(BostonTrain.head())
BostonTrain.info()
BostonTrain.describe()
X = BostonTrain.drop('MEDV',axis=1)
y = BostonTrain['MEDV']
