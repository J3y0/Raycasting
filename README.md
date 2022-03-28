### 2D Raycasting in Python
The code aims at drawing luminous rays from a light source (controlled by the mouse position) and handling correctly the interaction
with obstacles (walls in this case).

For this purpose, we will create a light source, and when a ray intersects a wall then we will draw a line between the source position
and the point of the intersection.

To calculate the coordinates of this particular point, we will use a little maths: we can navigate on a segment between two points A(x1, y1) and B(x2, y2)
thanks to a coefficient t. Let take M(x, y) a point on the segment, its coordinates are M(x1 + t(x2-x1), y1 + t(y2 - y1)). But as it intersects with another
line, we can write the same thing with the coordinates of the 2 points defining the other segment. We can then solve the system of the two unknowns u and t.

However, one must be careful with several walls: we have to choose the closest point (else, the ray would go through the closest wall).


## Dependancies
This little program requires pygame to work properly. Indeed, I manage GUI thanks to this library.
