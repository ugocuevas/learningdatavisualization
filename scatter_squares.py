import matplotlib.pyplot as plt


input_values = range(1, 1001)
squares = [x**2 for x in input_values]

#To plot a single point, use the scatter() method

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_values, squares, c='green', s=10) #The s argument is used to set the size of the dot
#To change the colour of the points, pass c to scatter and give the colour name in quotes or using tuples. For example c = (0, 0.8, 0) where maximum is 1

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14)

#Set the range for each axis
ax.axis([0, 1100, 0, 1100000]) #Requires four values: the minimum and maximum for x and the minimum and maximum for y

#Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize = 14)

plt.show()