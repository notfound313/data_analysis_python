import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
  plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],  c='blue',s=5)


    # Create first line of best fit
  yr_2050 = np.array([int(i) for i in range(1880, 2051)])
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']
  slope, intercept, r_value, p_value, std_err = linregress(x, y)
  yr_plot =  intercept + slope*yr_2050
  plt.plot(yr_2050,yr_plot)
  


    # Create second line of best fit
  df_2000 = df[df['Year'] >= 2000]
  x_1 = df_2000['Year']
  y_2 = df_2000['CSIRO Adjusted Sea Level']
  slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = linregress(x_1, y_2)
  yr_2000 = np.array([int(i) for i in range(2000, 2051)])
  yr_plot2 =  intercept_1 + slope_1*yr_2000
  plt.plot(yr_2000,yr_plot2)


    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
 
  

    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()