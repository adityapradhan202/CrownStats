import pandas as pd
import numpy as np

df3 = pd.read_csv('preprocessed_data.csv')

def fat(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Fat'][series_index]

def carb(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Carbs'][series_index]

def sug(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Sugar'][series_index]

def sodi(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Sodium'][series_index]

def prot(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Protein'][series_index]

def qty(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Quantity'][series_index]

def cal(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Calories'][series_index]

def tfat(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Trans fat'][series_index]

def sfat(pname):
    series_index = list(df3['Product']).index(pname)
    return df3['Saturated Fat'][series_index]


if __name__ == "__main__":
    print(qty('Veg Supreme'))

# Trans fat