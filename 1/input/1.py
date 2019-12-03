# %%

import pandas as pd
import math

df = pd.read_csv('input.csv')
df.head()

# %%

'''
a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
'''
def getFuel(df):s
    mass = df.Mass
    return math.floor(mass / 3) - 2 

df['fuel'] = df.apply(lambda x: getFuel(x),axis=1)
df.head()

print("Fuel required = {}".format(df.fuel.sum()))

# %%
