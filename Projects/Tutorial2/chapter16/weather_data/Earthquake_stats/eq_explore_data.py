import plotly.graph_objects as go
from pathlib import Path  
import json  

input_path = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\Earthquake_stats\eq_data_1_day_m1.geojson')
output_path = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\Earthquake_stats')

# Read the GeoJSON data
contents = input_path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Optionally write the readable version of the GeoJSON data
readable_contents = json.dumps(all_eq_data, indent=4)
output_path_geojson = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\Earthquake_stats\readable_eq_data.geojson')
output_path_geojson.write_text(readable_contents)

# Extract relevant earthquake data
all_eq_dicts = all_eq_data['features']
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Earthquake magnitude from the properties section
    lon = eq_dict['geometry']['coordinates'][0]  # Longitude from the geometry section (first element)
    lat = eq_dict['geometry']['coordinates'][1]  # Latitude from the geometry section (second element)
    eq_title = eq_dict['properties']['title']  # Earthquake title from the properties section

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
    
title = 'Global Earthquakes' 

# Create a 3D globe with Plotly
fig = go.Figure(go.Scattergeo(
    lat=lats, 
    lon=lons,  
    text=eq_titles,  # Show earthquake titles when hovering over points
    hoverinfo='text',  # Display text when hovering over points
    marker=dict(
        size=[mag * 10 for mag in mags],  # Earthquake magnitude determines the size of the points (scaled by 3)
        color=mags,  # Color points by magnitude
        colorscale='Viridis',  # Set color scale
        showscale=True,  # Show the color scale
    ),
))

# Update the layout for the globe
fig.update_layout(
    geo=dict(
        projection_type='orthographic',  # Set map projection to 'orthographic'
        showcoastlines=True,
        coastlinecolor='Black',
        showland=True,
        landcolor='lightgray',
        showocean=True,
        oceancolor='lightblue',
    ),
    title=title,
)

# Save the figure to the specified output path with a file name and .html extension
output_html_path = output_path / 'globetrotter.html'
fig.write_html(output_html_path)  # Pass the full path with the .html extension
