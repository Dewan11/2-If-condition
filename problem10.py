def compare(length, breadth):
  area = length * breadth
  perimeter = 2 * (length + breadth)
  return area > perimeter

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

if compare(length, breadth):
  print("Area of the rectangle > perimeter.")
else:
  print("Area of the rectangle < perimeter.")