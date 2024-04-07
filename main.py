import rhinoscriptsyntax as rs
import math



def run():
    choice = rs.GetString("Choose 1 for square or 2 for circle", "1")
    morph_factor = rs.GetInteger("Choose between 0 and 1 for your morph factor", 1)





def create_square_random():
    points = []

    for s in range(2):
                for t in range(4):
                    x = math.cos(math.radians(45 + 90 * t)) * math.sqrt(2)
                    y = math.sin(math.radians(45 + 90 * t)) * math.sqrt(2)
                    z = -1 + 2 * s
                    point = (x, y, z)
                    points.append(point)
    square = rs.AddBox(points)

    return square

square_id = create_square_random()

def create_sphere():
     radius = 5
     choice = rs.GetPoint("Enter a point(centre)")
     centre = convert_to_point(choice)
     sphere = rs.AddSphere(centre, radius)
     return sphere, centre

def convert_to_point(user_input, default_value= 5):
    try:
        # Try converting the input to a list of floats (assuming comma-separated or space-separated values)
        coordinates = [float(x) for x in user_input.split(",") or user_input.split()]
        if len(coordinates) == 1:
            # If only one value, replicate it for x, y, and z
            return coordinates[0], coordinates[0], coordinates[0]
        elif len(coordinates) == 2:
            # If two values, assume x and y, set z to default
            return coordinates[0], coordinates[1], default_value
        else:
            return tuple(coordinates)  # Valid 3D point
    except ValueError:
        # Handle conversion errors (not numerical input)
        return "An error occurred!"


sphere, sphere_centre = create_sphere()

def morph_geometry(morph_factor, sphere_centre):
      obj_id_pts = get_object_points(square_id)
      sphere
      for point in obj_id_pts:
           cube_point = obj_id_pts[point]
           morphed_point = [sphere_centre[x] * morph_factor + cube_point[x] * (1 - morph_factor) for x in range(3)]
           rs.AddPoint(morphed_point)
        # rs.rebui


def get_object_points(object_id):
  # Explode the object into its components
  components = rs.ExplodeObject(object_id)
  points = []
  for component in components:
    # Check if the component is a surface (cubes are made of surfaces)
    if rs.IsSurface(component):
      # Extract points from the surface using rs.SurfacePoints
      surface_points = rs.SurfacePoints(component)
      points.append(surface_points)  # Add surface points to the list
  return points



