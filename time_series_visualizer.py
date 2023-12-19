import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data

df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
  fig, ax = plt.subplots(figsize=(16, 4))
  
  plt.plot(df['value'],color='red',linewidth=0.8)
  ax.set_xlabel('Date')
  ax.set_ylabel('Page Views')
  ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

  # Show the plot

 





    # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')
  return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar['Years'] = df_bar.index.year
  df_bar['Months'] = df_bar.index.month
  df_bar = df_bar.groupby(['Years', 'Months'])['value'].mean().reset_index()
  missing = {
     "Years": [2016, 2016, 2016, 2016],
            "Months": [1, 2, 3, 4],
            "value": [0, 0, 0, 0]
        }
  df_bar = pd.concat([pd.DataFrame(missing), df_bar])
  
  months=['January', 'February', 'March', 'April', 'May', 'June', 'July', 
               'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
  fig, ax = plt.subplots(figsize=(12, 8))
  
  x = np.arange(len(df_bar['Years'].unique()))
  width = 0.04  # the width of the bars
  multi = 0  
  month = df_bar['Months'].unique()
  for idx in month:
      offset = width * multi
      perbar = ax.bar(x + offset, df_bar.loc[df_bar['Months'] == idx, 'value'],
              width=width, label=months[idx-1])
      multi += 1

  ax.set_xticks(x + width/0.2)
  ax.set_xticklabels(df_bar['Years'].unique())
  ax.set_xlabel('Years', labelpad=15)
  ax.set_ylabel('Average Page Views')

  ax.legend(title= 'Months')


    # Save image and return fig (don't change this part)
  fig.savefig('bar_plot.png')
  return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
  
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16, 8))
  
    # boxplot1
    sns.boxplot(data=df_box, x="year", y="value", ax=ax1)
    ax1.set_title("Year-wise Box Plot (Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Page Views")
  
    # bloxplot 2
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x="month", y="value", order=months, ax=ax2)
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Page Views")
                       
  
  
  
  
  
  


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
