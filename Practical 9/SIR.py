# ====== 0. import the relevant python libraries ======
import numpy as np
import matplotlib.pyplot as plt

# ====== 1. define the variables and parameters =====
N = 10000
I = 1
R = 0
S = N - I - R
beta = 0.3
gamma = 0.05

# ====== 2. create arrays for each variables =======
S_list = [S]
I_list = [I]
R_list = [R]

# ====== 3. loop over 1000 time points =======

# we need new infections, new recoveries, and new suspectibles
for day in range(1000):

    # calculate the infection probability
    infection_probability = beta * I / N

    # calculate the new infections
    new_infections = np.random.choice(range(2), S, p=[1 - infection_probability, infection_probability])
    number_new_infections = np.sum(new_infections)

    # calculate the new recoveries
    new_recoveries = np.random.choice(range(2), I, p=[1 - gamma, gamma])
    number_new_recoveries = np.sum(new_recoveries)

    # update S, I, R
    S = S - number_new_infections
    I = I + number_new_infections - number_new_recoveries
    R = R + number_new_recoveries

    # record values
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# ====== 4. plot the results ======
plt.figure(figsize=(6, 4), dpi = 150)
plt.plot(S_list, label="Susceptible")
plt.plot(I_list, label="Infected")
plt.plot(R_list, label="Recovered")

plt.xlabel("Time")
plt.ylabel("Number of people")
plt.title("SIR model")
plt.legend()
plt.show()

