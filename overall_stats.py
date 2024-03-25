import pandas as pd
import numpy as np

df2 = pd.read_csv('preprocessed_data.csv')
stats_df2 = df2.describe().transpose()


# Overal stats data
fat_avg = round(stats_df2['mean']['Fat'],2)
sugar_avg = round(stats_df2['mean']['Sugar'],2)
carbs_avg = round(stats_df2['mean']['Carbs'],2)
qty_avg = round(stats_df2['mean']['Quantity'],2)
cal_avg = round(stats_df2['mean']['Calories'],2)
sodium_avg = round(stats_df2['mean']['Sodium'],2)
protein_avg = round(stats_df2['mean']['Protein'],2)
transfat_avg = round(stats_df2['mean']['Trans fat'],2)
satfat_avg = round(stats_df2['mean']['Saturated Fat'],2)

# percentile stats - calories, carbs, protein, fats (4*2=8 lines)
# stats with percentile(50)
cal50 = round(stats_df2['50%']['Calories'],2)
carb50 = round(stats_df2['50%']['Carbs'],2)
fat50 = round(stats_df2['50%']['Fat'],2)
prot50 = round(stats_df2['50%']['Protein'],2)
sod50 = round(stats_df2['50%']['Sodium'],2)

# stats with percentile(75)
cal75 = round(stats_df2['75%']['Calories'],2)
carb75 = round(stats_df2['75%']['Carbs'],2)
fat75 = round(stats_df2['75%']['Fat'],2)
prot75 = round(stats_df2['75%']['Protein'],2)
sod75 = round(stats_df2['50%']['Sodium'],2)

if __name__ == "__main__":

    print(stats_df2)

    print("Quantity Average:", qty_avg)
    print("Calories Average:", cal_avg)
    print("Carbs Average:", carbs_avg)
    print("Sugar Average:", sugar_avg)
    print("Fat Average:", fat_avg)
    print("Saturated Fat Average:", satfat_avg)
    print("Trans Fat Average:", transfat_avg)
    print("Protein Average:", protein_avg)
    print("Sodium Average:", sodium_avg)