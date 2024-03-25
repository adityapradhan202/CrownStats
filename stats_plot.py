import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(3498)
# rows
years = [2019, 2020, 2021, 2022, 2023, 2024]
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']
sales_data = np.random.randint(250, 500, (6,12))
sales_df = pd.DataFrame(data=sales_data, index=years, columns=months)
sales_df = sales_df.reset_index()

x = sales_df['index']
def generate_plt(month1, month2, month3):
    fig,axes = plt.subplots(nrows=3, ncols=1, figsize=(10,25))
    # plots
    axes[0].plot(x, sales_df[month1], label=month1, marker='o', color='#7fa8eb', ls='--')
    axes[1].plot(x, sales_df[month2], label=month2, marker='o', color='#ffbd8a', ls='--')
    axes[2].plot(x, sales_df[month3], label=month3, marker='o', color='#a789e8', ls='--')
    # plot labels
    axes[0].set_xlabel('Last 6 years')
    axes[0].set_ylabel('Monthly sales data')
    axes[1].set_xlabel('Last 6 years')
    axes[1].set_ylabel('Monthly sales data')
    axes[2].set_xlabel('Last 6 years')
    axes[2].set_ylabel('Monthly sales data')
    # plot titles
    axes[0].set_title(f'Sales in {month1}')
    axes[1].set_title(f'Sales in {month2}')
    axes[2].set_title(f'Sales in {month3}')
    # legends
    axes[0].legend()
    axes[1].legend()
    axes[2].legend()

    plt.subplots_adjust(hspace=0.25)

    return fig
if __name__ == "__main__":

    myfig = generate_plt("January", "February", "March")
    plt.show()