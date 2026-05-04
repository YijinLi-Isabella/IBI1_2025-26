# ======= 0. import necessary libraries =======
import numpy as np
import matplotlib . pyplot as plt

# ======= 1. make arrays of all suspectible population =======
population = np.zeros((100, 100))   # a 100 * 100 array made of zeros

# ======= 2. choose a random point for outbreak =======
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1

# ======= 3. heat map =======
plt.figure(figsize = (6, 4), dpi = 150)
plt.imshow(population, cmap = "viridis", interpolation="nearest")
plt.show()

# ======= 4. set up the model parameters =======
N = 10000
I = 1
R = 0
S = N - I - R
beta = 0.3
gamma = 0.05

# ====== 5. create arrays for each variables =======
S_list = [S]
I_list = [I]
R_list = [R]

# ======= 6. loop over 100 time points =======
for day in range(100):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        # ======= 7. recovery =======
        # The currently infected individual has a probability (gamma) to recover (State 2)
        if np.random.choice([0, 1], p=[1-gamma, gamma]) == 1:
            population[x, y] = 2
    
    # ======= 8. plotting the outcome ===
    # We plot at days 10, 50, and 100 (which correspond to index 9, 49, and 99 in a 0-indexed loop)
    if day in [9, 49, 99]:
        plt.figure(figsize=(6, 4), dpi=150)
        # vmin and vmax lock the color scale so 0=purple, 1=blue-green, 2=yellow
        plt.imshow(population, cmap="viridis", interpolation="nearest", vmin=0, vmax=2)
        plt.title(f"Outbreak - Day {day + 1}")
        plt.show()