x_coords = []
y_coords = []

for _ in range(3):
    x, y = map(int, input().split())
    x_coords.append(x)
    y_coords.append(y)

if x_coords.count(x_coords[0]) == 1:
    fourth_x = x_coords[0]
elif x_coords.count(x_coords[1]) == 1:
    fourth_x = x_coords[1]
else:
    fourth_x = x_coords[2]

if y_coords.count(y_coords[0]) == 1:
    fourth_y = y_coords[0]
elif y_coords.count(y_coords[1]) == 1:
    fourth_y = y_coords[1]
else:
    fourth_y = y_coords[2]

print(fourth_x, fourth_y)
