# Start with 5 infected individuals
# The growth rate is 40%
# The total number of the students is 91
initial_infected = 5
growth_rate = 0.4
total_students = 91
days = 0
current_infected = initial_infected
print(initial_infected, "students are infected on day", days)
# Calculate and print the number of infected students on each day
while current_infected < total_students:
    current_infected = current_infected * 1.4
    days += 1
    print(current_infected, "students are infected on day", days)
print(days, "days", "were taken to infect all the students")