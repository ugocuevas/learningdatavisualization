from calendar import c
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #Make a random walk instance
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',  s=1)
    #Emphasize the first and the last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none', c='red', s=100)

    #To turn off axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Make another walk? (Y/N): ")
    if keep_running.upper() == 'N':
        break