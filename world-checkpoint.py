import folium
# Create a Folium Map centered at a location of your choice
world_map = folium.Map(location=[0, 0], zoom_start=2)

# List of points with latitude and longitude coordinates
points = [(37.7749, -122.4194),  # San Francisco, USA
          (51.509865, -0.118092),  # London, UK
          (-23.550520, -46.633308)]  # São Paulo, Brazil

# Add markers for each point
for point in points:
    folium.Marker(location=point, popup='Sample Point').add_to(world_map)

# Save the map as an HTML file
world_map.save('points_on_map.html')