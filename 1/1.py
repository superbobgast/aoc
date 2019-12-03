# %%

import pandas as pd
import math

df = pd.read_csv('./1/input/input.csv')
df.head()

# %%

'''
a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
'''
def getFuel(df):
    mass = df.Mass
    return math.floor(mass / 3) - 2 

df['fuel'] = df.apply(lambda x: getFuel(x),axis=1)
df.head()

print("Fuel required = {}".format(df.fuel.sum()))

# %%

def getInfinateFuel(fuel):
    added = math.floor(fuel / 3) - 2
    if added <= 0:
        return 0
    else:
        return added + getInfinateFuel(added)

df['inf_fuel'] = df.apply(lambda x: getInfinateFuel(x['Mass']),axis=1)
df.head()


print("infinate Fuel required = {}".format(df.inf_fuel.sum()))


# %%
