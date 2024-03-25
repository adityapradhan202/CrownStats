import pandas as pd
import numpy as np

df = pd.read_csv('burger_king_data.csv')

df = df.rename({'Portion\nsize gm':'Quantity', 
                'Energy\nKcal':'Calories', 
                'Carbohyd\nrate gm':'Carbs',
                'Sugar gm':'Sugar', 
                'Fat gm':'Fat',
                'Saturated\nFat gm':'Saturated Fat',
                'Tran Fatty\nAcids gm':'Trans fat',
                'Protein\ngm':'Protein', 
                'Soduim\nContent gm':'Sodium'}, axis=1)

df['Quantity'] = df['Quantity'].str.replace('ml', '')
df['Quantity'] = df['Quantity'].str.replace('*', '')
df = df.drop_duplicates()

df['Sodium'] = pd.to_numeric(arg = df['Sodium'], errors='coerce')
df['Sodium'] = df['Sodium'].fillna(0.0)
df['Trans fat'] = df['Trans fat'].fillna(0.0)

df['Product'] = df['Product'].str.replace("( ", "(")
df['Product'] = df['Product'].str.replace("7 UP", "7up")
df['Product'] = df['Product'].str.replace("Pcs", "pcs")
df['Product'] = df['Product'].str.replace("shake", "Shake")

df = df.to_csv('preprocessed_data.csv')

