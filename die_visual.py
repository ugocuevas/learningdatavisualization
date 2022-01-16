from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#Create a D6, that is a die with six sides
die1 = Die()
die2 = Die()

#Roll dice and store in a list
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
    
#Analyse the frequencies
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
#Visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}

my_layout = Layout(title='Results of rolling two D6 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')