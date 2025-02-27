from pathlib import Path  
import json  
import plotly.express as px  



input_path = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\Earthquake_stats\eq_data_1_day_m1.geojson')
output_path = Path(r'C:\Users\nurop\OneDrive\Desktop\pYTHON COURSE\Projects\Tutorial2\chapter16\weather_data\Earthquake_stats\readable_eq_data.geojson')

# Read the contents of the input GeoJSON file
contents = input_path.read_text(encoding='utf-8')

# Parse the string content of the GeoJSON file into a Python dictionary
all_eq_data = json.loads(contents)

# Create a more human-readable version of the data by indenting the JSON structure.
readable_contents = json.dumps(all_eq_data, indent=4)

# Write the formatted (readable) JSON data into a new output file.
output_path.write_text(readable_contents)

# Extract earthquake data from the 'features' key in the GeoJSON dictionary.
# This key contains the list of individual earthquake data records.
all_eq_dicts = all_eq_data['features']

print(f"Total Earthquakes: {len(all_eq_dicts)}")

mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']  # Earthquake magnitude from the properties section
    lon = eq_dict['geometry']['coordinates'][0]  #  from the geometry section (first element)
    lat = eq_dict['geometry']['coordinates'][1]  # Latitude from the geometry section (second element)
    eq_title = eq_dict['properties']['title']  # Earthquake title from the properties section

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

#test
print(f"First 10 magnitudes: {mags[:10]}")
print(f"First 5 longitudes: {lons[:5]}")
print(f"First 5 latitudes: {lats[:5]}")
title = 'Global Earthquakes'

# - The 'projection' argument sets the map projection (natural earth in this case).
fig = px.scatter_geo(
    lat=lats, 
    lon=lons,  
    size=mags,  # Earthquake magnitude determines the size of the points
    title=title, 
    color=mags,  
    color_continuous_scale='Viridis',  
    labels={'color': 'Magnitude'},  
    projection='natural earth',  # Set map projection to 'natural earth'
    hover_name=eq_titles  # Show the earthquake titles when hovering over points
    )


fig.write_html('Maps.html')
