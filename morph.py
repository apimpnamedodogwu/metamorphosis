import rhinoscriptsyntax as rs
import math

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

def create_sphere():
    radius = 2
    choice = rs.GetPoint("Enter a point(centre)")
    if choice:
        centre = convert_to_point(choice)
        sphere = rs.AddSphere(centre, radius)
        return sphere, centre
    else:
        return None, None

def convert_to_point(user_input, default_value=5):
    if isinstance(user_input, tuple):
        return user_input  # It's already a point
    else:
        return default_value, default_value, default_value  # Default center

def morph_geometry(morph_factor, object_id, target_centre):
    if not target_centre or not object_id:
        return  # Missing required geometry

    obj_id_pts = get_object_corners(object_id)
    morphed_pts = []
    for point in obj_id_pts:
        # Calculate morphed point
        morphed_point = [(target_centre[x] * morph_factor + point[x] * (1 - morph_factor)) for x in range(3)]
        morphed_pts.append(morphed_point)


def get_object_corners(object_id):
    # Calculate the object's bounding box
    bbox = rs.BoundingBox(object_id)
    # bbox contains the corner points of the bounding box
    return bbox


def run():
    choice = rs.GetString("Choose 1 for square or 2 for circle", "1")
    if not choice:
        return
    
    morph_factor = rs.GetReal("Choose between 0 and 1 for your morph factor", 1, 0, 1)
    if choice == "1":
        object_id = create_square_random()
        _, target_centre = create_sphere()  # Assuming the sphere's center is the morph target
    else:
        object_id, target_centre = create_sphere()

    if object_id and target_centre:
        morph_geometry(morph_factor, object_id, target_centre)


run()