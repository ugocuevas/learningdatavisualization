import matplotlib.pyplot as plt


input_values = range(1, 1001)
squares = [x**2 for x in input_values]

#To plot a single point, use the scatter() method

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c=squares, cmap = plt.cm.Reds, s = 10) #To use a colour map, pass the y-values to c. 
#The colour map makes the smaller values lighter and the larger values darker

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1100000]) #Requires four values: the minimum and maximum for x and the minimum and maximum for y

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()

#To automatically save plots, replace the plt.show() with a call to plt.savefig()
#For example plt.savefig('squares_plot.png', bbox_inches = 'tight'). bbox_inches trims extra whitespace from around the plot