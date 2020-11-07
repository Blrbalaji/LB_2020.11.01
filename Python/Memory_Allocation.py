import math
n=int(input("Number of Edges of a Regular Polygon:\t"))

s=float(input("Length of the Edge: \t"))
p=n*s # Perimeter of a Polygon
a=s/(2*math.tan(180/n*math.pi/180)) # Apothem of a Polygon
area=round(p*a/2,2)
print(f"Area of Polygon: {area} sq units")
print(f"Apothem or Incircle of a Polygon: {round(a,2)} units")
print(f"Exterior Angle of the Polygon: {360/n} \u00B0")