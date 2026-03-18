# Priduce a dictionary of the populations
population = {
    "UK": {"pop_2020": 66.7, "pop_2024": 69.2}, 
    "China": {"pop_2020": 1426, "pop_2024": 1410}, 
    "Italy": {"pop_2020": 59.4, "pop_2024": 58.9}, 
    "Brazil": {"pop_2020": 208.6, "pop_2024": 212.0}, 
    "USA": {"pop_2020": 331.6, "pop_2024": 340.1}
}
country_percentage = [] # Prepare a list to save the country and its population percentage change 
for country in population:
    pop_2024 = population[country]['pop_2024']
    pop_2020 = population[country]['pop_2020']
    percentage_change = (pop_2024 - pop_2020) / pop_2020 * 100
    country_percentage.append((country, percentage_change))
    print("The population change in", country, f"is {percentage_change: .2f}%")
# Change list into descending order
country_percentage.sort(key=lambda x: x[1]) # Sort the list according to the percentage
country_percentage.reverse()
print("The population changes in descending order:")
for country, change in country_percentage:
    print(f"{country}:{change: .2f}%")
# Identify the largest increase and decrease
print(f"The largest increase: {country_percentage[0][0]}({country_percentage[0][1]:.2f}%))")
print(f"The largest decrease: {country_percentage[-1][0]}({country_percentage[-1][1]:.2f}%))")
# Produce the bar chart
import matplotlib.pyplot as plt
categories = []
values = []
for country, change in country_percentage:
    categories.append(country)
    values.append(change)
plt.figure(figsize = (8, 6))
plt.bar(categories, values, color = "#7BC0CD")
plt.xlabel("Country")
plt.ylabel("Population change (%)")
plt.title("Population Growth Rate Change for Each Country")
plt.show()