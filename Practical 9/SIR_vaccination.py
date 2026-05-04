# ====== 0. import the relevant python libraries ======
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  # Imported to use the viridis colour map

# ====== 1. define the fixed variables and parameters =====
N = 10000
beta = 0.3
gamma = 0.05

# Set up the plot dimensions
plt.figure(figsize=(6, 4), dpi=150)

# ====== 2. Loop over vaccination rates from 0% to 100% ======
for v_rate in range(0, 101, 10):
    
    # Initial states
    I = 1
    R = 0
    
    # Calculate the number of vaccinated individuals
    V = int(N * (v_rate / 100))
    
    # FIX: Ensure V never exceeds the remaining uninfected population 
    # This prevents S from becoming -1 at 100% vaccination
    V = min(V, N - I - R)
    
    # Vaccinated people are removed from the susceptible pool
    S = N - I - R - V 
    
    # We only need to track the infected list for this plot
    I_list = [I]


    # ====== 3. loop over 1000 time points =======
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

        # record infected values
        I_list.append(I)

    # ====== 4. plot the results for the current vaccination rate ======
    # We divide v_rate by 100 to pass a value between 0.0 and 1.0 to the colormap
    if v_rate == 0:
        label_name = "0"
    else:
        label_name = f"{v_rate}%"
        
    plt.plot(I_list, label=label_name, color=cm.viridis(v_rate / 100))

# ====== 5. Finalize and show the plot ======
plt.xlabel("time")
plt.ylabel("number of people")
plt.title("SIR model with different vaccination rates")
plt.legend()
plt.show()