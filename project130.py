import pandas as pd
#import numpy as np
df = pd.read_csv("Final_130.csv")

#df.replace('',np.nan)

del df["Luminosity"]
del df["radius"]
del df["distance"]
del df["star_names"]

df.to_csv('Final_129.csv')

#deleting all the nan values would delete almost every row of the csv file, we can try by removing all the comments</Thankyou>