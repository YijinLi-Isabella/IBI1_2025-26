# ====== 0. import the libraries ======
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ====== 1. set the working directory ======
os.chdir("/Users/liyijin/Desktop/26_Spring/IBI1/IBI1_2025-26/IBI1_2025-26/Practical 10")

# ====== 2. check the directory ======
print("The directory is:", os.getcwd())
print("The files are:", os.listdir())

# ====== 3. read the dataset (dataframe) ======
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ====== 4. look at the data frame ======
print("=== The first 5 rows: ===")
print(dalys_data.head(5))

print("=== The data types: ===")
print(dalys_data.info())

# statistical values for numeric columns 
# (including count, mean, sd, quantiles...)
print("=== Statistical values: ===")
print(dalys_data.describe())

# ====== 5. access the values (by row and column) ======
# use iloc (index location)
# the 3rd and 4th columns for the first 10 rows
first_10 = dalys_data.iloc[0:10, 2:4]
print("The third and fourth columns for the first 10 rows ")
print(first_10)
afghanistan_10 = dalys_data.iloc[0:10]
max_year = afghanistan_10.loc[afghanistan_10['DALYs'].idxmax(), 'Year']
print(f"\nThe maximum DALYs across the first 10 years: {max_year}")
# The maximum DALYs across the first 10 years is 1998

# use loc (location using column names)
year_col = dalys_data["Year"]
is_zimbabwe = dalys_data["Entity"] == "Zimbabwe"
zim = dalys_data.loc[is_zimbabwe, "Year"]
print(f"\n=== Years where Entity is Zimbabwe ===")
print(zim)
# The first year for Zimbabwe: 1990
# The last year for Zimbabwe: 2019

# ======= 6. Country with the highest/lowest DALYs in 2019 ======
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_country = recent_data.loc[recent_data['DALYs'].idxmax(), 'Entity']
min_country = recent_data.loc[recent_data['DALYs'].idxmin(), 'Entity']
print(f"\nCountry with the highest DALYs in 2019: {max_country}")
print(f"Country with the lowest DALYs in 2019: {min_country}")
# Country with the highest DALYs in 2019: Lesotho
# Country with the lowest DALYs in 2019: Singapore

# ====== 7. Plot the data over time (for Lesotho) ======
country_plot = dalys_data[dalys_data["Entity"] == max_country]
plt.plot(country_plot.Year, country_plot.DALYs, 'b+')
plt.xticks(country_plot.Year, rotation=-90)
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs over time: {max_country}")
plt.show()

# ====== 8. An interesting question ======
# Question: What was the distribution of DALYs across all countries in 2019?
plt.boxplot(recent_data["DALYs"].dropna())
plt.title("2019 Global DALYs Distribution")
plt.ylabel("DALYs")
plt.show()