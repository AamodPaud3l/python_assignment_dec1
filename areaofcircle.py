#Program to calculate area of circle
def area_of_circle(radius):
    return 22/7 * radius**2

radius = input('Enter radius of cirlce:')

area = area_of_circle(float(radius))

print("\nRadius of circle = {0}cm\nArea of circle = {1:.3f}sq.cm".format(radius,area))