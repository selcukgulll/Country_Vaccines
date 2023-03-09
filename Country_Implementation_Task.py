# -*- coding: utf-8 -*-
# This code implementation works with a csv file, it fills the missing data
# in daily_vaccinations column per country with the minimum daily vaccination number of relevant countries.  

#imports the pandas library
import pandas as pd 

#Iimports the csv file that was downloaded. For this specific situation the address of the csv file was:
# C:\\Users\\Honor\\Desktop\\PIWorks\\country_vaccination_stats.csv
df = pd.read_csv("C:\\Users\\Honor\\Desktop\\PIWorks\\country_vaccination_stats.csv")

#Fills the daily_vaccinations coloumn with the minimum daily_vaccinations value of the country
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(df.groupby('country')['daily_vaccinations'].transform('min'))

#exports to the changed dataFrame to specified address as version 2.
df.to_csv('C:\\Users\\Honor\\Desktop\\PIWorks\\country_vaccination_stats_v2.csv', index=False)