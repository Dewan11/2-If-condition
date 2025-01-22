import math

center_x, center_y, radius = map(float, input("Enter center (x y) and radius: ").split())
point_x, point_y = map(float, input("Enter point (x y): ").split())


distance = math.sqrt(pow(point_x - center_x, 2) + pow(point_y - center_y, 2))
if distance < radius:
  position = "inside"
elif distance == radius:
  position = "on"
else:
  position = "outside"

print(f"The point is {position} the circle.")