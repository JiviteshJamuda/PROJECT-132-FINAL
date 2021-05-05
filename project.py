import pandas as pd
import csv
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
# print(df.head(10))
# print(df.shape)
# name = df['name'].tolist()
mass = df['mass'].tolist()
radius = df['radius'].tolist()
distance = df['distance'].tolist()
gravity = df['gravity'].tolist()
# print(mass)
mass.sort()
radius.sort()
distance.sort()
gravity.sort()
print(mass)

plt.title('Radius-Mass')
plt.xlabel('Radius')
plt.ylabel('Mass')
plt.plot(radius, mass)
plt.show()

plt.title('Mass-Gravity')
plt.xlabel('mass')
plt.ylabel('Gravity')
plt.plot(mass, gravity)
plt.show()