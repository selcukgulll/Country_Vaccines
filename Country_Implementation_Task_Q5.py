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

#Fills the daily_vaccinations coloumn with 0 if the country has no records.
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)

#Lists the medians of each country and saves in a new dataFrame.
med_df = df.groupby('country').median()

#Sorts the medians of the countries and saves in a new dataFrame.
sorted_median=med_df.sort_values(by="daily_vaccinations",ascending=False)

#Selects the countries with top 3 medians and saves in a new dataFrame.
result_dataFrame=sorted_median.head(3)

#exports to the changed dataFrame to specified address.
result_dataFrame.to_csv('C:\\Users\\Honor\\Desktop\\PIWorks\\country_vaccination_stats_Q5.csv', index=False)