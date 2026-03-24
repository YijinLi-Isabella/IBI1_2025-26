# Produce a list of the heart rates and calculate the mean value
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
mean_rate = sum(heart_rates) / len(heart_rates)
print("There are", len(heart_rates), f"patients in the dataset, and the mean heart rate is{mean_rate: .2f}.")
# Group the heart rates into 3 categories
low_count = 0
normal_count = 0
high_count = 0
for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif rate > 120:
        high_count += 1
    else:
        normal_count += 1
# Print the count of each catogory
print("There are", low_count, "measurements that fall into the low category.")
print("There are", normal_count, "measurements that fall into the normal category.")
print("There are", high_count, "measurements that fall into the high category.")
# Find the largest count and the category
largest_count = max(low_count, normal_count, high_count)
largest_category = None
if largest_count == low_count:
    largest_category = "low"
elif largest_count == normal_count:
    largest_category = "normal"
else:
    largest_category = "high"
print("The", largest_category, "category contains the largest number.")
# Produce the pie chart
import matplotlib.pyplot as plt
labels = ['low', 'normal', 'high']
sizes = [low_count, normal_count, high_count]
colors = ['#385a75', '#6192b5', '#98b4ce']
plt.figure(figsize=(8,6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title('Distribution of Heart Rate Categories')
plt.show()