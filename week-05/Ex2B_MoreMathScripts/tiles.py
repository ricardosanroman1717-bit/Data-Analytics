# Calculate tile boxes needed for a room

import math

# Room dimensions in feet
length = 10
width = 12

# Calculate room area
area = length * width

# Calculate boxes needed without extra tiles
tiles_needed = math.ceil(area)
boxes_needed = math.ceil(tiles_needed / 12)

# Add 10% extra tiles for waste
extra_tiles_needed = math.ceil(tiles_needed * 1.10)
total_boxes = math.ceil(extra_tiles_needed / 12)

# Display results
print(f"Room area: {area} square feet")
print(f"Boxes without extra tiles: {boxes_needed}")
print(f"Boxes with 10% extra tiles: {total_boxes}")