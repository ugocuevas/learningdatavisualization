import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
    
all_eq_dicts = all_eq_data['features']

mags, longs, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    long = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    longs.append(long)
    lats.append(lat)
    
#Map the earthquakes
data = [{'type': 'scattergeo',
         'lon': longs,
         'lat': lats,
         'marker': {'size':[5*mag for mag in mags],
            }
        }]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquales.html')
