import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

"""
A simple function to invert a string, so pyplot will print Hebrew the right way.
"""
def invert(string):
    return string[::-1]

#Loading the data.
df_pop = pd.read_csv(r'C:\Users\User\Documents\Projects\Daily Excess Deaths\israel pop by age 2000-2019.csv', index_col = 'Year')
df_deaths = pd.read_csv(r'C:\Users\User\Documents\Projects\Daily Excess Deaths\deaths per day by age israel.csv')

"""
Sources:
    https://www.cbs.gov.il/he/publications/LochutTlushim/2020/p-1.xlsx
    https://www.cbs.gov.il/he/publications/LochutTlushim/2020/%D7%90%D7%95%D7%9B%D7%9C%D7%95%D7%A1%D7%99%D7%99%D7%942019-2000.xlsx
"""

#Reindexing with DateTime.
df_deaths['Date'] = pd.to_datetime(df_deaths['Date'])
df_deaths.set_index('Date', inplace = True)
df_deaths.sort_index(inplace = True)

#Creating an empty DataFrame for the results.
df_results = pd.DataFrame(columns = df_deaths.columns, index = df_deaths.index)

"""
Calculating the expected deaths of the population
Calculation according to https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3406211/
"""
for year in df_pop.index:   
    df_temp = df_deaths[str(year)]
    df_results[str(year)] = df_temp/df_pop.loc[year, :]
    df_results[str(year)] *= df_pop.loc[2008, :]

#Calculating the sum of expected deaths and the age-adjusted death rate.
df_results['Total'] = df_results.sum(axis = 'columns')
df_results['Total'] /= df_pop.loc[2008, :].sum() / 1000000
df_results.sort_index(inplace = True)

#Pivoting the data to atable where each column is a calanderic year.
df_pivoted = pd.DataFrame(index = list(range(0,366)))
for year in range(2000,2021):
    df_temp = df_results.loc[str(year), :]
    if year in [2000,2004,2008,2012,2016]:
        df_temp['Index'] = list(range(0,366))
    elif year == 2020:
        df_temp['Index'] = list(range(0,274))
    else:
        df_temp['Index'] = list(range(0,365))
    df_temp.set_index('Index', inplace = True)
    df_pivoted[str(year)] = df_temp['Total']

#Rearranging the data to insert an empty cell in years without 29/2.
years = ['2001','2002','2003','2005','2006','2007','2009', '2010', '2011', '2013', '2014', '2015', '2017', '2018', '2019']
for year in years:
    df_temp = pd.DataFrame()
    df_temp['Data'] = df_pivoted[year].truncate(before = 60, after = 364)
    df_temp['Index'] = df_temp.index + 1
    df_temp.set_index('Index', inplace = True)
    df_pivoted.loc[61:365, year] = df_temp['Data']
    df_pivoted.loc[60, year] = np.nan

#Creating a fictious date range for use later.
df_pivoted['Date'] = pd.date_range('1/1/2020', '31/12/2020', freq = 'D')

#Exporting the data.
df_pivoted.to_csv(r'C:\Users\User\Documents\Projects\Daily Excess Deaths\excess deaths results.csv')
