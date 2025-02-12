"""

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
 Check if these points make a straight line in the XY plane.


Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

"""

# coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]

# print(len(coordinates))

x_val = coordinates[1][0]-coordinates[0][0]
y_val = coordinates[1][1]-coordinates[0][1]
# val = val1/val2

if len(coordinates)==2:
    print(True)
else:
    for i in range(1,len(coordinates)):
        x_val1 = coordinates[i][0]-coordinates[i-1][0]
        y_val1 = coordinates[i][1]-coordinates[i-1][1]
        if y_val*x_val1 != x_val*y_val1:
            print(False)
    print(True)

